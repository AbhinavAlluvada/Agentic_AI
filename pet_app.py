from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.tools import tool
from langchain.agents import create_agent
import wikipedia
load_dotenv()

llm = ChatOpenAI(
    model="meta-llama/llama-3.1-8b-instruct",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    temperature=0.5,
)


def generate_pet_name(animal_type, color_type):

    prompt_template_name = PromptTemplate(
        input_variables=["animal_type", "color_type"],
        template="I have a {animal_type} pet and of color {color_type}, i want a cool name for it.Suggest me five cool names for my pet.Keep it just to the name and only names list.",
    )
    chain = prompt_template_name | llm
    response = chain.invoke({"animal_type": animal_type, "color_type": color_type})
    return response.content
@tool
def multiply_by_two(number : float) -> float:
    """Multiply a number by two"""
    return number * 2

@tool
def wiki_search(search : str) -> str:
    """Search wikipedia for a short summary"""
    try:
        return wikipedia.summary(search,sentences = 12)
    except Exception as e:
        return f"Hello Hermano! Welcome to Except block , btw this is your exception {e}"
    
def langchain_agent():
    question = "What is the average age of humans(male) in india , and multiply it with 2"
    agent = create_agent(
        model=llm,
        tools=[multiply_by_two,wiki_search]
    )
    response =agent.invoke(
        {
            "messages":[
                {
                    "role":"user",
                    "content": question
                }
            ]
        }
    )
    return response["messages"][-1].content

    

if __name__ == "__main__":
    print(langchain_agent())
    # animal_type = input("What kind of pet? ")
    # color_type = input("What color is it? ")
    # print(generate_pet_name(animal_type, color_type))
