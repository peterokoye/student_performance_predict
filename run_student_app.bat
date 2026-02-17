@echo off
REM Activate the conda environment
call C:\Users\HP\anaconda3\Scripts\activate.bat student_performance

REM Navigate to your project folder
cd C:\Users\HP\Desktop\AI stuffs\Projects\student_performance_project

REM Launch Streamlit app
streamlit run app.py

REM Keep the terminal open after the app closes
pause
