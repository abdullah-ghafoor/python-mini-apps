import streamlit as st

st.title("Our Calculator")
st.text("This is a simple calculator which performs basic arithmetic operation")



num1 = st.number_input("Enter first Number ")
num2 = st.number_input("Enter second Number ")

operation = st.selectbox("Pick operation you want to perform:",  ["Select","+", "-", "*", "/"])
calculate = st.button("Calculate")

if calculate:

    if operation=='+':
        st.write(f'The Sum of {num1} and {num2} is {num1+num2} ')
    elif operation=='-':
        st.write(f'The subtraction of {num1} and {num2} is {num1-num2} ')
    elif operation=="*":
        st.write(f'The multiplication of {num1} and {num2} is {num1*num2} ')
    elif operation=="/":
        st.write(f'The division of {num1} and {num2} is {num1/num2} ')
    else:
        st.write("Enter correct options")


