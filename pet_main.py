import pet_app as pn
import streamlit as st

st.title("Pet Name Generator")
animal_type = st.sidebar.selectbox(
    "What is your pet?", ("Cat", "Dog", "Cow", "Hamster", "Falcon")
)

if animal_type == "Cat":
    pet_color = st.sidebar.text_area("What color is your cat?", max_chars=10)

if animal_type == "Dog":
    pet_color = st.sidebar.text_area("What color is your dog?", max_chars=10)

if animal_type == "Cow":
    pet_color = st.sidebar.text_area("What color is your cow?", max_chars=10)

if animal_type == "Hamster":
    pet_color = st.sidebar.text_area("What color is your hamster?", max_chars=10)

if animal_type == "Falcon":
    pet_color = st.sidebar.text_area("What color is your falcon?", max_chars=10)


if pet_color:
    response = pn.generate_pet_name(animal_type, pet_color)
    st.text(response)
