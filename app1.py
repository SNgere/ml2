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
    
    components.html(
     """
     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
    <link rel="stylesheet" href="style.css">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@300&display=swap" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@700&display=swap" rel="stylesheet">
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
     
    """
    
)

          
    # display the front end aspect
    # st.markdown(html_temp, unsafe_allow_html = True) 
      
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
