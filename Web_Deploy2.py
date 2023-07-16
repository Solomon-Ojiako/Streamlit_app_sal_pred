import streamlit as st
import pickle
import numpy as np
r = open("regression.pkl", "rb")
regressor = pickle.load(r)
exp = st.number_input("Experience in Years ", 0,42,1)
exp = np.array(exp).reshape(1,-1)
prediction = regressor.predict(exp)[0]
if st.button("Salary Prediction"):
        st.write(f'{prediction}')

#you can clearly see that we have only used the pickle file and opened it, created an interactive interface to 
#collect number of years of experience, reshaped it and insert it into our model and then used the button()
# to produce the output for any given exp value. 

#This is the model we will deploy. Notice that pickling takes the data, here it is the model in its state(we are
# satisfied with the model's performance and stores that state for use anytime we open it only)

#We will then deploy to Github and other places