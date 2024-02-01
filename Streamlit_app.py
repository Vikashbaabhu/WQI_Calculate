import numpy as np
import pickle
import pandas as pd
import streamlit as st 

from PIL import Image


pickle_in = open("model.pkl","rb")
classifier=pickle.load(pickle_in)

with open('style.css') as f :
      st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def welcome():
    return "Welcome All"

def predict_note_authentication(year,temp,do,ph,con,bod,n,fc,tc):
     
    prediction=classifier.predict([[year,18,temp,5,do,6,ph,200,con,2.5,bod,0.3,n,500,fc,1000,tc]])
    print(prediction)
    return prediction



def main():
    html_temp = """
    <div style="background-color:skyblue;padding:10px;border-radius:5px">
    <h2 style="color:white;text-align:center;font-family:Callibri;"><b>Water Quality Index Calculation</b></h2>
    </div>
    <br></br>
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    #temp min - 18s
    temp = col1.number_input("Temperature")
    # do min - 5.5
    do = col2.number_input("Dissolved Oxygen")
    #ph min - 7.2
    ph = col3.number_input("pH")
    #con min - 275
    con = col1.number_input("Conductivity ")
    #bod min - 3
    bod = col2.number_input("Bio-chemical Oxygen Demand")
    #n min - 0.5
    n = col3.number_input("Nitrate")
    #fc min- 2830
    fc = col1.number_input("Fecal Coliform ")
    #tc min - 8000
    tc = col3.number_input("Total Coliform ")
    result=""
    col2.text("")
    col2.text("")
    if col2.button("Calculate"):
        result=predict_note_authentication(2024,temp,do,ph,con,bod,n,fc,tc)
        st.success('The Water Quality Index of the river is {:.2f}'.format(result[0]))
        if result <= 25 :
          st.success('The quality of the water is excellent')  
          image = Image.open('Excellent.jpg')
          st.image(image, caption='Excellent')
        elif result >= 25 and result <= 50:
          st.success('The quality of the water is good')  
          image = Image.open('Good.jpg')
          st.image(image, caption='Good')
        elif result >= 50 and result <= 75:
          st.success('The quality of the water is poor')
          image = Image.open('Poor.jpg')
          st.image(image, caption='Poor')
        else:
          st.success('The quality of the water is very poor')
          image = Image.open('Very Poor.jpg')
          st.image(image, caption='Very Poor')

if __name__=='__main__':
    main()
    