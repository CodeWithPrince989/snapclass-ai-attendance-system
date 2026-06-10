# SnapClass - AI-Powered Attendance System

## 🚀 Quick Start

### **Option 1: One-Click Launch (Windows)**
Double-click `run.bat` - This will:
- Activate the virtual environment
- Install dependencies
- Start the Streamlit app on `http://localhost:8501`

### **Option 2: Manual Setup**

1. **Activate Virtual Environment:**
   ```powershell
   .\venv311\Scripts\Activate.ps1
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application:**
   ```bash
   streamlit run app.py
   ```

4. **Open Landing Page:**
   - Open `index.html` in your browser
   - Click "🚀 Launch App" button to access the attendance system

---

## 📋 Project Structure

```
SNAP-CLASS/
├── app.py                 # Main Streamlit application
├── index.html             # Landing page (open in browser)
├── run.bat                # One-click startup script
├── requirements.txt       # Python dependencies
├── main.py                # Secondary script
├── README.md              # This file
├── Workflow.txt           # Development workflow
├── src/                   # Source code
│   ├── screens/           # Home, Teacher, Student screens
│   └── components/        # Reusable components
└── venv311/               # Virtual environment
```

---

## ✨ Features

- **👤 Face Recognition** - AI-powered facial recognition for automatic attendance
- **⚡ Lightning Fast** - Mark attendance in under 30 seconds
- **🎓 Teacher Dashboard** - Manage classes and view reports
- **📊 Analytics** - Detailed attendance insights
- **🔐 Secure** - Encrypted database with Supabase
- **🌐 Easy Enrollment** - QR code based class joining

---

## 🛠️ Technology Stack

- **Python** - Core backend
- **Streamlit** - Web interface
- **Face Recognition** - dlib, scikit-learn
- **Database** - Supabase
- **Security** - bcrypt
- **Data Processing** - Pandas, NumPy
- **Audio Processing** - librosa

---

## 📱 How to Use

### For Teachers:
1. Login with teacher credentials
2. Create a class and generate QR code
3. Students scan QR to join
4. During class, click "Take Attendance"
5. Snap a photo - system automatically recognizes all faces
6. View attendance reports in real-time

### For Students:
1. Click "Join Class" 
2. Enter join code or scan QR
3. Register your face
4. Attendance is marked automatically when teacher takes a photo

---

## 📌 Important Notes

- Ensure your virtual environment is activated before running
- Make sure all dependencies are installed (`pip install -r requirements.txt`)
- The Streamlit app runs on `http://localhost:8501` by default
- For best face recognition results, ensure good lighting during attendance

---

## 🎯 Next Steps

1. **Landing Page**: Open `index.html` to see the project overview
2. **Demo**: Click "Launch App" button to start the system
3. **Development**: Modify files in `src/` folder for custom features

---

Made with ❤️ for the education sector
