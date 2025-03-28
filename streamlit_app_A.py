import streamlit as st
import numpy as np
import pickle

with open("student_performance_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Student Performance Prediction")

region = st.selectbox("Region", ["Urban", "Rural"])
gender = st.selectbox("Gender", ["Male", "Female"])
enrollment_type = st.selectbox("Enrollment Type", ["Regular", "Private"])
subject_group = st.selectbox("Subject Group", ["Science", "Commerce", "Arts"])
ssc_i_marks = st.number_input("SSC I Marks", min_value=0, max_value=100)
ssc_ii_marks = st.number_input("SSC II Marks", min_value=0, max_value=100)
hssc_i_marks = st.number_input("HSSC I Marks", min_value=0, max_value=100)
attendance_rate = st.slider("Attendance Rate (%)", min_value=0, max_value=100)
parent_education = st.selectbox("Parent Education Level", ["Primary", "Secondary", "Higher"])
parent_income = st.number_input("Parent Income (USD)", min_value=0, max_value=100000)
study_hours = st.slider("Daily Study Hours", min_value=0, max_value=12)
extra_tuition = st.selectbox("Extra Tuition", ["Yes", "No"])
school_type = st.selectbox("School Type", ["Public", "Private"])
previous_failures = st.number_input("Previous Failures", min_value=0, max_value=5)
co_curricular = st.selectbox("Co-Curricular Activities", ["Yes", "No"])
exam_attempts = st.number_input("Exam Attempts", min_value=1, max_value=5)
hssc_ii_grade = st.selectbox("HSSC II Grade", ["A", "B", "C", "D", "E"])

region_dict = {"Urban": 1, "Rural": 0}
gender_dict = {"Male": 1, "Female": 0}
enrollment_dict = {"Regular": 1, "Private": 0}
subject_dict = {"Science": 1, "Commerce": 2, "Arts": 3}
education_dict = {"Primary": 1, "Secondary": 2, "Higher": 3}
tuition_dict = {"Yes": 1, "No": 0}
school_dict = {"Public": 1, "Private": 0}
activity_dict = {"Yes": 1, "No": 0}
grade_dict = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}

input_features = np.array([
    region_dict[region],
    gender_dict[gender],
    enrollment_dict[enrollment_type],
    subject_dict[subject_group],
    ssc_i_marks,
    ssc_ii_marks,
    hssc_i_marks,
    attendance_rate,
    education_dict[parent_education],
    parent_income,
    study_hours,
    tuition_dict[extra_tuition],
    school_dict[school_type],
    previous_failures,
    activity_dict[co_curricular],
    exam_attempts,
    grade_dict[hssc_ii_grade]
]).reshape(1, -1)

if st.button("Predict Performance"):
    prediction = model.predict(input_features)
    st.write(f"Predicted Performance Score: {prediction[0]:.2f}")
