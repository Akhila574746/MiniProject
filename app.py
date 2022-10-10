import streamlit as st
import joblib
model_nb = joblib.load('Fake_job_postings')
st.title('Fake Job Detection') #creates a title in web app
ip = st.text_input('Enter Job Description:') #creates a text box in web app
ip_text = vect.transform([ip])
op = model_nb.predict([ip_text])
if st.button('Predict'):
  st.title(op[0])
  if (op[0]==1):
    print('Fraudulant Job')
  else:
    print('Real Job')
  
  
  
  
  
 

