import streamlit as st
st.title("streamlit app ")
st.write("this is my new app ")
button1 = st.button("click me ")
if button1:
    st.write("you clicked the button ")

st.header ("start ckeckbox stction ")
like = st.checkbox("do you like this app ?")
button2= st.button("submit ")
if button2:
    if like:
        st.write("thanks i like it to ")
    else:
        st.write ("i im sorry to have bad tastes")
st.header ("start radio button ")

animal= st.radio ("what type of animal do you like ", ("tiger", "lion", "cat", "Dog", "horse"))
button3 = st.button ("submit animal")
if button3:
    st.write(animal)
    if animal=='cat':
        st.header("wow")

st.header("select box section ")
animal2= st.selectbox("what type of animal do you like ", ("tiger", "lion", "cat", "Dog", "horse"))
button4= st.button("click box ")
if button4:
    st.write(animal2)
    if animal2=='lion':
        st.header("wow")
st.header("multiselect box")
options = st.multiselect("what type of animal do you like ", ("tiger", "lion", "cat", "Dog", "horse"))
button5 = st.button("print animal")
if button5:

    st.write(options)
st.header("slider section ")
epoch_no = st.slider(" how many epochs   ")
if st.button ("epoch button "):
    st.write(epoch_no)

st.header("text input section :")
movie = st.text_input("whats your favourit movie ")
user_no= st.number_input("Enter the no ")

def run_sentiment_analysis (txt):
    st.write("analysis done ")
txt= st.text_area ("enter  something  in the text area  ")

if st.button("movie button "):
    st.write (movie)
    st.write(user_no)
    st.write ("sentiment : ", run_sentiment_analysis (txt))

