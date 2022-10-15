import streamlit as st
import pickle
import joblib

model_nb = joblib.load('Fake_job_postings')
cv = pickle.load(open("vectorizer","rb"))

def main():
  st.title('Fake Job Detection') #creates a title in web app
  ip = st.text_input('Enter Job Description:') #creates a text box in web app
  if st.button('Predict'):
    data=[ip]
    vect=cv.transform(data).toarray()
    prediction=model_nb.predict(vect)
    result=prediction[0]
    if result==0:
      st.error("Fraudulant Job")
    else:
      st.success("Real Job")
   
main()  
  
  
  
  
  
  
 

