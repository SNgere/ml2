%%writefile app.py
 
import pickle
import streamlit as st
 
# loading the trained model
pickle_in = open('predictor.pkl', 'rb') 
predictor = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(Gender, Married, ApplicantIncome, LoanAmount, Credit_History):   
 
    # Making predictions 
    prediction = predictor.predict( 
        [[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
     
    if prediction == 0:
        pred = 'Not Diabetic'
    else:
        pred = 'Diabetic'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit diabetes diagnosis ML App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction
    Pregnancies = st.number_input("Pregnancies")
    Glucose = st.number_input("Glucose")
    BloodPressure = st.number_input("BloodPressure")
    SkinThickness = st.number_input("SkinThickness")
    Insulin = st.number_input("Insulin")
    BMI = st.number_input("BMI")
    DiabetesPedigreeFunction = st.number_input("DiabetesPedigreeFunction")
    Age = st.number_input("Age")
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age) 
        st.success('Your diagnosis is {}'.format(result))
             
if __name__=='__main__': 
    main()