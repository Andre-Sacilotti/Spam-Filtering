from Classification import PredictEmail
import streamlit as st

st.title("Spam or Not? Verify your Email here!")


text = st.text_area(label="Copy and Paste your email, SMS, Business Whatsapp Message and even an online publicity")

btn = st.button("Verify!")

if btn == True:
    pred = PredictEmail(str(text))

    if pred[0] == 0:
        st.markdown("<p style='font-size:25px''>Not Spam</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:15px''>Your text has " + str(round((pred[1][0][0])*100,2))+"% chances of being Not Spam</p>", unsafe_allow_html=True)

    else:
        st.markdown("<p style='font-size:25px''>Spam</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:15px''>Your text has " + str(round((pred[1][0][1]) * 100, 2)) + "% chances of being Spam</p>", unsafe_allow_html=True)


st.text(' ')
st.text(' ')
st.text(' ')
st.text("Author: André Sacilotti")
st.markdown('<a href="https://br.linkedin.com/in/andré-sacilotti-84a69a173" target="_blank"><img src="https://img.icons8.com/material/24/000000/linkedin--v1.png"/></a>', unsafe_allow_html=True)
st.text(' ')
st.markdown('<a href="https://github.com/Andre-Sacilotti/" target="_blank"><img src="https://img.icons8.com/material/24/000000/github.png"/></a>', unsafe_allow_html=True)
st.text(' ')