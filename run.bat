@echo off
REM SnapClass - Quick Start Script

echo.
echo ================================================
echo   SnapClass - AI Attendance System
echo ================================================
echo.

REM Activate Virtual Environment
echo [1/3] Activating virtual environment...
call venv311\Scripts\activate.bat

REM Install/Update requirements
echo [2/3] Installing dependencies...
pip install -q -r requirements.txt

REM Start Streamlit App
echo [3/3] Starting Streamlit Application...
echo.
echo ========================================
echo App is starting at http://localhost:8501
echo Landing page is at index.html
echo ========================================
echo.

streamlit run app.py

pause
