import streamlit as st
from datetime import datetime, date

st.title("🎂 Age & Birthday Countdown Calculator")

# User input: Name
name = st.text_input("Enter your Name")

# User input: Date of Birth
dob = st.date_input("Select your Date of Birth")

# Button to calculate age
if st.button("Calculate Age & Countdown"):
    if name.strip() == "":
        st.warning("Please enter your name!")
    else:
        today = date.today()

        # Age calculation
        age_years = today.year - dob.year
        if (today.month, today.day) < (dob.month, dob.day):
            age_years -= 1

        # Next birthday calculation
        next_birthday_year = today.year
        if (today.month, today.day) >= (dob.month, dob.day):
            next_birthday_year += 1

        next_birthday = date(next_birthday_year, dob.month, dob.day)
        days_left = (next_birthday - today).days

        # Results
        st.success(f"🎉 Hello {name}!")
        st.info(f"🧮 You are {age_years} years old.")
        st.warning(f"⏳ {days_left} days left until your next birthday!")

        # Optional: If today is birthday!
        if days_left == 0:
            st.balloons()
            st.success("🎈🎉 Happy Birthday! 🎉🎈")

st.write("Made with ❤️ using Streamlit")
