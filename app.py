import streamlit as st
import joblib
import numpy as np

# Load model and scaler
model = joblib.load("models/student_model.pkl")
scaler = joblib.load("models/scaler.pkl")

st.title("🎓 Student Performance Prediction App")
st.write("Enter student details to predict Pass or Fail")

# User Inputs
study_hours = st.number_input("Study Hours", min_value=0.0, max_value=24.0, step=0.5)
sleep_hours = st.number_input("Sleep Hours", min_value=0.0, max_value=24.0, step=0.5)
attendance = st.number_input("Attendance (%)", min_value=0.0, max_value=100.0, step=1.0)
previous_scores = st.number_input("Previous Scores", min_value=0, max_value=100, step=1)

if st.button("Predict"):

    # Create input array
    input_data = np.array([[study_hours, sleep_hours, attendance, previous_scores]])

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)
    probability = model.predict_proba(input_scaled)[0][1]

    if prediction[0] == 1:
        st.success(f"✅ Likely to PASS")
    else:
        st.error(f"❌ Likely to FAIL")

    st.write(f"📊 Pass Probability: {probability*100:.2f}%")
