import pickle
import streamlit as st

# Load the model
pickle_in = open('windspeed1.pkl', 'rb')
clf = pickle.load(pickle_in)

# Define the prediction and interpretation functions
def predict(Maximum_Temperature, Minimum_Temperature, Dry_Bulb_Temperature, Wet_Bulb_Temperature, Dew_point_Temperature):
    prediction = clf.predict([[Maximum_Temperature, Minimum_Temperature, Dry_Bulb_Temperature, Wet_Bulb_Temperature, Dew_point_Temperature]])
    return int(prediction[0])

def interpret_wind_speed(wind_speed):
    if wind_speed < 15:
        return "Wind will blow at low level and Electricity will be generated approx 225 kilowatt 
    elif 50 <= wind_speed <= 60:
        return "Wind will generate at full capacity and Electricity will be generated approx 2 Megawatt "
    elif wind_speed > 80:
        return "Turn off wind mill,Because of hard weather weather conditions"
    else:
        return "Wind speed is in a normal range"

# Streamlit UI
st.header("Streamlined Wind Speed Forecasting: A Web-Based Machine Learning Approach for Wind Mill Operators with Real-Time Data Using Streamlit")
nav = st.sidebar.radio('Navigation', ["Home", 'Prediction'])

if nav == "Home":
    st.write("The utilization of wind energy has become increasingly prevalent in the global pursuit of sustainable and renewable energy sources. Wind mills, serving as pivotal infrastructures in this endeavor, rely heavily on accurate wind speed forecasting to optimize their operational efficiency and energy output. However, traditional forecasting methods often encounter limitations in adapting to real-time data and providing user-friendly interfaces for wind mill operators.")
    st.write("In response to these challenges, we present Streamlined Wind Speed Forecasting, an innovative approach leveraging web-based machine learning techniques and the Streamlit framework. This approach aims to empower wind mill operators with real-time wind speed predictions, enabling them to make informed decisions and maximize energy generation.")
    st.write("By integrating machine learning models with Streamlit's interactive web application capabilities, wind speed forecasting becomes more accessible and user-friendly. Wind mill operators can conveniently access and visualize forecasted wind speeds, facilitating proactive adjustments to turbine operations and energy management strategies.")
    st.write("This paper explores the development and implementation of our web-based machine learning approach, highlighting its potential to revolutionize wind speed forecasting for wind mill operators. Through a combination of advanced algorithms, real-time data integration, and user-centric design principles, we strive to enhance the efficiency and sustainability of wind energy production.")
    st.image("download.jpeg",width=500)

if nav == "Prediction":
    st.write("<h2 style='text-align: center;'>Input Parameters</h2>", unsafe_allow_html=True)
    Maximum_Temperature = st.number_input("Maximum Temperature", min_value=0, max_value=100, value=0)
    Minimum_Temperature = st.number_input("Minimum Temperature", min_value=0, max_value=100, value=0)
    Dry_Bulb_Temperature = st.number_input("Dry Bulb Temperature", min_value=0, max_value=100, value=0)
    Wet_Bulb_Temperature = st.number_input("Wet Bulb Temperature", min_value=0, max_value=100, value=0)
    Dew_point_Temperature = st.number_input("Dew point Temperature", min_value=0, max_value=100, value=0)

    if st.button('Predict'):
        prediction = predict(Maximum_Temperature, Minimum_Temperature, Dry_Bulb_Temperature, Wet_Bulb_Temperature, Dew_point_Temperature)
        interpretation = interpret_wind_speed(prediction)
        st.header('Predicted Wind Speed: ' + str(prediction) + ' km/hr')
        st.write('Interpretation:',interpretation)
