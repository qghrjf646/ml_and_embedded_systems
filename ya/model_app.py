import streamlit as st
import joblib

model = joblib.load("regression.joblib")
size = st.number_input("How big is the house ?")
n_bedrooms = st.number_input("How many bedrooms are in the house ?")
has_garden = st.number_input("Does the house have a garden ? 1 for yes, 0 for no.")
result = model.predict([[size, n_bedrooms, has_garden]])[0]
st.write("The predicted price is: ", result)
