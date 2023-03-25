import streamlit as st

# Setting up the webpage title
st.title("ＢＯＤＹ ＭＡＳＳ ＩＮＤＥＸ(ＢＭＩ) ＣＡＬＵＣＵＬＡＴＯＲ")

# Adding input controls for Name, Gender, Age, Address, Hobbies, Weight, and Height
name = st.text_input("Name")
gender = st.radio("Gender", ("Male", "Female"))
age = st.number_input("Age")
address = st.text_input("Address")
hobbies = st.multiselect("Hobbies", ["Doing gym", "Travelling", "Music", "Sports","Watching movies"])
weight = st.number_input("Weight (in kg)")
height = st.number_input("Height (in cm)")

# BMI Calculation
if st.button("Calculate BMI"):
    bmi = weight / ((height/100) ** 2)
    st.write("BMI: ", bmi)

# Displaying the inputs provided by the user
st.write("Name: ", name)
st.write("Gender: ", gender)
st.write("Age: ", age)
st.write("Address: ", address)
st.write("Hobbies: ", hobbies)
st.write("Weight: ", weight)
st.write("Height: ", height)
primaryColor = "purple"
