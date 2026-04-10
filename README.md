# 💪 BMI Calculator & Tracker (Streamlit App)

## 📌 Overview

This project is a simple and interactive **BMI (Body Mass Index) Calculator & Tracker** built using **Python and Streamlit**.
It allows users to:

* Calculate their BMI
* View their BMI category
* Store and track BMI history
* Visualize BMI trends over time

---

## 🚀 Features

* ✅ User-friendly interface using Streamlit
* ✅ BMI calculation based on weight and height
* ✅ Automatic BMI category detection:

  * Underweight
  * Normal
  * Overweight
  * Obese
* ✅ Stores user data in a CSV file
* ✅ Displays previous records
* ✅ Shows BMI trend graph

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* Matplotlib
* OS module

---

## 📂 Project Structure

```
project_folder/
│
├── app.py              # Main Streamlit application
├── bmi_data.csv        # Stores user BMI records (auto-created)
└── README.md           # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Install Required Libraries

Run the following command:

```
pip install streamlit pandas matplotlib
```

---

### 2. Run the Application

Navigate to the project folder and run:

```
streamlit run app.py
```

---

### 3. Open in Browser

The app will automatically open at:

```
http://localhost:8501
```

---

## 🧮 How BMI is Calculated

BMI Formula:

```
BMI = Weight (kg) / (Height (m))²
```

---

## 📊 BMI Categories

| BMI Range   | Category    |
| ----------- | ----------- |
| < 18.5      | Underweight |
| 18.5 – 24.9 | Normal      |
| 25 – 29.9   | Overweight  |
| ≥ 30        | Obese       |

---

## 📈 Data Storage

* All user entries are stored in **bmi_data.csv**
* Data includes:

  * Name
  * Weight
  * Height
  * BMI

---

## 🔥 Future Improvements

* Add login system
* Add date/time tracking
* Improve UI design
* Add health suggestions based on BMI
* Deploy app online (Streamlit Cloud)

---

## 👨‍💻 Author

Developed as a beginner-friendly **Streamlit project** for learning and practice.

---

## 📜 License

This project is free to use for educational purposes.
