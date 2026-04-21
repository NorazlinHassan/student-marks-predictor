import streamlit as st
import numpy as np
import pickle
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title = 'Student Marks Predictor', page_icon='👨‍🎓', layout = 'centered')
st.title('👨‍💻 Student Marks Predictor 👨‍🎓')
st.write('Enter the Number of Hours Studied ⏰  (1-10) and **Click Predict** to See the Predicted Marks')

# Load the Model
def load_model(model):
    with open(model,'rb') as f:
        slr = pickle.load(f)
    return slr

try:
    model = load_model('slr.pkl')
except Exception as e:
    st.error ('Your Pickle File Not Found')
    st.exception("Failed to Load the Model : ".e)
    st.stop()


hours = st.number_input('Hours Studied', 
                        min_value=1.0, 
                        max_value=10.0, 
                        value=4.0, 
                        step=0.1,   # to enable the -+ buttons readily available
                        format='%.1f')

if st.button('🔮 Predict'):
    try:
        x = np.array([[hours]])  # making the independent variable into 2D
        predictions = model.predict(x)
        predictions = predictions[0]  # [0] is so that our output only display the marks without the []
        st.success(f'🔮 Predicted Marks : {predictions: .1f}')
        st.write('⚠️ Note: This is a ML Model Prediction **Actual Results May Vary**')
    except Exception as e:
        st.error(f'Prediction Failed : {e}')




                