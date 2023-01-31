# %%writefile app.py
 
import pickle
import streamlit as st
import streamlit.components.v1 as components
 
# loading the trained model
pickle_in = open('model.pkl', 'rb') 
predictor = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):   
 
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
    html_temp = components.html("""
    <!DOCTYPE html>

        <div class="description">
            <p class="title">Diabetes Checker</p>

            <div class="parent">
                <div class="character">
                    <img src="/character_1.png" alt="" id="character1" width="520px"
                    height="500px">
                </div>

                <div class="description1">
                    <p>
                        Get to evaluate your health your health based on personal medical history and 
                        factors and seek immediate medical care.
                    </p>

                    <p>Complete the form below to get your results:</p>
                    <a href="">
                        <script src="https://cdn.lordicon.com/ritcuqlt.js"></script>
                        <lord-icon
                            src="https://cdn.lordicon.com/eoabunbr.json"
                            trigger="loop"
                            style="width:70px;height:70px">
                        </lord-icon>
                    </a>
                </div>
            </div>
        </div>

        <div class="footer">

        </div>

    """)
      
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
        st.success('Patient diagnosis is {}'.format(result))
             
if __name__=='__main__': 
    main()
