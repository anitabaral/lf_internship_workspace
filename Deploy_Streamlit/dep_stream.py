
import pandas as pd
import numpy as np
import joblib
import streamlit as st


classifier = joblib.load("model.pkl")

def prediction(sepal_length, sepal_width, petal_length, petal_width):

    prediction = classifier.predict(
        [[sepal_length, sepal_width, petal_length, petal_width]])
    print(prediction)
    return prediction

def main():
    st.title("Iris Flower Prediction")

    sepal_length = st.text_input("Sepal Length", "Type Here")
    sepal_width = st.text_input("Sepal Width", "Type Here")
    petal_length = st.text_input("Petal Length", "Type Here")
    petal_width = st.text_input("Petal Width", "Type Here")
    result =""

    if st.button("Predict"):
        result = prediction(sepal_length, sepal_width, petal_length, petal_width)
    st.success('The output is {}'.format(result))

if __name__=='__main__':
    main()
