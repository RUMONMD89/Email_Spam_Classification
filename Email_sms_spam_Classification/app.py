import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
from PIL import Image

ps = PorterStemmer()

image = Image.open('email_filter1.png')
st.image(image)

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


tfidf = pickle.load(open('tfidf_vectorizer.pkl', 'rb'))
model = pickle.load(open('mnb_model.pkl', 'rb'))

st.title("Email/SMS Spam Classifier")

# input_sms = st.text_area("Enter the message")

input_sms = st.text_input("Email/Message", "Typing....")
st.write("The current typing Email/Message is: ", input_sms)

if st.button('Predict'):

    # 1. preprocess
    transformed_sms = transform_text(input_sms)
    # 2. vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3. predict
    result = model.predict(vector_input)[0]
    # 4. Display
    if result == 1:
        st.header("Spam")
        st.image("spam.png", caption="This is a spam Email or message")
    else:
        st.header("No Spam")
        st.image("no spam.png", caption="This is not a spam Email or message")
