# %%writefile app.py
 
import pickle
import streamlit as st
 
# loading the trained model
pickle_in = open('predictor.pkl', 'rb') 
predictor = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(Gender,Age,Urea,Cr,HbA1c,Chol,TG,HDL,LDL,VLDL,BMI):
     # Pre-processing user input    
    if Gender == "Male":
        Gender = 1
    else:
        Gender = 0
 
    # Making predictions 
    prediction = predictor.predict( 
        [[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
     
    if prediction == 0:
        pred = 'Non-Diabetic'
    elif prediction == 1:
        pred = 'Predict-Diabetic'
    else:
        pred = 'Diabetic'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:blue;padding:13px"> 
    <h1 style ="color:white;text-align:center;">Diabetes Screening Test</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction
    Gender = st.selectbox('Gender',("Male","Female"))
    Age = st.number_input("Age", value = 0)
    Urea = st.number_input("Urea")
    Cr = st.number_input("Creatinine ratio")
    HbA1c = st.number_input("Hemoglobin A1c measure")
    Chol = st.number_input("Cholesterol")
    TG = st.number_input("Triglyceride level")
    HDL = st.number_input("HDL Cholesterol level")
    LDL = st.number_input("LDL cholesterol level")
    VLDL = st.number_input("VLDL cholesterol level")
    BMI = st.number_input("BMI")
    
    
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(Gender,Age,Urea,Cr,HbA1c,Chol,TG,HDL,LDL,VLDL,BMI) 
        st.success('Patient diagnosis is {}'.format(result))
             
if __name__=='__main__': 
    main()
# %%
