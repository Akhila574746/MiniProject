import streamlit as st
import joblib
model_nb = joblib.load('Fake_job_postings')
st.title('Fake Job Detection') #creates a title in web app
ip = st.text_input('Enter Job Description:') #creates a text box in web app
op = model_nb.predict([ip])
if st.button('Predict'):
  st.title(op[0])
  
  
  
  
  
