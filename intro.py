import streamlit as st
st.title("Welcome to the Streamlit App created by karthik")
st.write("Welcome! this app calculates square root of a number")
st.header("Enter a number to calculate its square root")
number=st.slider("pick a number",0,50,3) #min max default
st.subheader("Result")
squared_number=number*number
st.write(f"The square root of **{number}** is **{squared_number}**.")