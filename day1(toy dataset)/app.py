import streamlit as st
import numpy as np
st.title("placement predictor")
import pickle as pkl
model=pkl.load(open('model.pkl','rb'))

cgpa=st.number_input("CGPA")
iq=st.number_input("IQ")

if st.button('Predict'):
    query=np.array([cgpa,iq]).reshape(1,2)
    st.title(model.predict(query[0]))