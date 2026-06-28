def scope_args_kwargs():
    def add(*args):
        return sum(args)

    print(add(10,20,30))

    def sub(*args):
        total = sum(args)
        return total
    print(sub(10,6.2,3.55))

    def para(*args):
        return args
    print(para("Hello",9.5,6,True))


    def docs(*doc):
        return " ".join(doc)
    print(docs("Hello","World"))

    def kwarg(*doc,**docs):
        return docs,doc

    print(kwarg(20,34,name = "Protagonist",age = 20))


    x = 10
    def outer():
        print(x)
    
    y = 20
    def outer_v2():
        y = 10
        print(y)
    
    z = 30
    def outer_v3():
        global z
        z =40
    outer_v3()
    print(z)
    
    def nonlocal_v1():
        a = 12
        def inner():
            nonlocal a
            a = 30
        inner()
        return a
    print(nonlocal_v1())

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def barks(self):
        print(self.name, "says woof") 
    def food(self):
        print(self.name,"likes chicken")
        
class SuperAgent:
    def thinking(self,agent):
        print(f"Agent {agent} is thinking...")
    def task(self , agent,type):
        if agent == "Lucia":
            print(f"Agent {agent} is working with a customer as it is {type} agent")
        else:
            print(f"Agent {agent} is sending an email as it is a {type}")
class Agent(SuperAgent):
    def __init__(self,agent_name , agent_type):
        self.name = agent_name
        self.type = agent_type
    def intro(self):
        print(f"Agent says... Hello, My name is {self.name}")
    def kind(self):
        print(f"Agent says... I am a {self.type} agent")

agent = Agent("Marcus","Email Automator")
agent_v2 = Agent("Lucia","Customer Service Assistant")

agent_v2.kind()
agent_v2.intro()
agent_v2.thinking(agent_v2.name)
agent_v2.task(agent_v2.name,agent_v2.type)