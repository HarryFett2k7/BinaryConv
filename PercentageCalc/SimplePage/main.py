import streamlit as st

st.header("Binary Convertor", divider="rainbow" )
st.subheader("A simple tool to convert numbers to and from binary.")

st.markdown('''
    This is a test while the website is under development
''')

itob = st.toggle("Integer to binary")
btoi = st.toggle("Binary to integer")

if itob:
    number = st.text_input("Enter your number: ", value = 1)
    binary = bin(int(number))
    st.markdown("Binary number: " + str(binary[2:]))

if btoi:
    number = st.text_input("Enter binary value: ", value = 1)
    integer = int(number, 2)
    st.markdown("Integer is: " + str(integer))
