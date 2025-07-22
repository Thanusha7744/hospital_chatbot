import streamlit as st
from chatbot import get_specializations, get_doctors_by_specialization, book_appointment

st.set_page_config(page_title="Hospital Chatbot", page_icon="🏥")

st.title("🏥 Hospital Chatbot")
st.write("Welcome! How can I help you today?")

menu = ["See Available Doctors", "Book Appointment", "Hospital Info"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "See Available Doctors":
    st.header("🔍 Available Doctors by Specialization")
    specs = get_specializations()
    selected_spec = st.selectbox("Choose Specialization", specs)
    if selected_spec:
        doctors = get_doctors_by_specialization(selected_spec)
        if doctors:
            for doc, slot in doctors:
                st.write(f"👨‍⚕ *{doc}* — 🕒 {slot}")
        else:
            st.warning("No available doctors for this specialization currently.")

elif choice == "Book Appointment":
    st.header("📅 Book an Appointment")
    specs = get_specializations()
    selected_spec = st.selectbox("Choose Specialization", specs)
    if selected_spec:
        doctors = get_doctors_by_specialization(selected_spec)
        if doctors:
            doctor_names = [doc for doc, _ in doctors]
            selected_doctor = st.selectbox("Choose Doctor", doctor_names)
            patient_name = st.text_input("Your Name")
            phone = st.text_input("Phone Number")
            symptoms = st.text_area("Describe your symptoms")

            if st.button("Book"):
                if patient_name and phone and symptoms:
                    result = book_appointment(selected_doctor, patient_name, phone, symptoms)
                    st.success(result)
                else:
                    st.error("Please fill all the details to book an appointment.")
        else:
            st.warning("No available doctors to book currently.")

elif choice == "Hospital Info":
    st.header("🏥 Hospital Information")
    st.write("""
    📍 Location: 123 Main Street, Your City  
    🕒 Opening Hours: 8:00 AM - 8:00 PM  
    ☎ Contact: +91-9876543210
    """)