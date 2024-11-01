import streamlit as st

st.title("Simple Streamlit App with a Button")

st.write("Hello, welcome to my Streamlit application!")

# Add a button
if st.button("Click Me"):
    st.write("Button was clicked!")
else:
    st.write("Button not clicked yet.")
