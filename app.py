import streamlit as st
from PIL import Image

img = Image.open("Con1.jpg")
st.sidebar.image(img.resize((100,150)))
curr = ["Naira","Pounds","Dollar","Euro","Yen","Cedi"]
conv = [1,2000,1750,1800,120,75]

#write a user define function that will power the app
def convert (num,initial,final):
    ini_id = curr.index(initial)
    fin_id = curr.index(final)
    value1 = conv[ini_id]
    value2 = conv[fin_id]

    result = num * value1/value2
    return round(result,2)




num = st.number_input ("How are you converting?")
initial = st.selectbox("what is your initial currency?",curr)
final = st.selectbox("what currency are you converting to?", curr)

amount = convert (num,initial,final)

if st.button("Convert"):
    st.write(amount)
    



