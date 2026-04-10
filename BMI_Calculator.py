import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# File to store data
DATA_FILE = "bmi_data.csv"

# Title
st.title("💪 BMI Calculator & Tracker")
st.write("Calculate your BMI and track your history!")

# User Input
name = st.text_input("Enter your name")
weight = st.number_input("Enter weight (kg)", min_value=1.0, max_value=300.0)
height = st.number_input("Enter height (meters)", min_value=0.5, max_value=2.5)

# BMI Calculation Function
def calculate_bmi(weight, height):
    return weight / (height ** 2)

# BMI Category Function
def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Button
if st.button("Calculate BMI"):
    if name == "":
        st.warning("Please enter your name")
    else:
        bmi = calculate_bmi(weight, height)
        category = get_category(bmi)

        st.success(f"Your BMI is {bmi:.2f}")
        st.info(f"Category: {category}")

        # Save Data
        new_data = pd.DataFrame({
            "Name": [name],
            "Weight": [weight],
            "Height": [height],
            "BMI": [bmi]
        })

        if os.path.exists(DATA_FILE):
            old_data = pd.read_csv(DATA_FILE)
            updated_data = pd.concat([old_data, new_data], ignore_index=True)
        else:
            updated_data = new_data

        updated_data.to_csv(DATA_FILE, index=False)

# Show History
st.subheader("📊 BMI History")

if os.path.exists(DATA_FILE):
    data = pd.read_csv(DATA_FILE)
    st.dataframe(data)

    # Graph
    if name != "":
        user_data = data[data["Name"] == name]

        if not user_data.empty:
            st.subheader("📈 BMI Trend")

            plt.figure()
            plt.plot(user_data["BMI"], marker='o')
            plt.xlabel("Entries")
            plt.ylabel("BMI")
            plt.title(f"{name}'s BMI Trend")

            st.pyplot(plt)
else:
    st.write("No data available yet.")