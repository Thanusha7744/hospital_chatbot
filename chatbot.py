import pandas as pd

# Load doctors CSV
doctors_df = pd.read_csv("doctors.csv")

def get_specializations():
    return doctors_df['Specialization'].unique().tolist()

def get_doctors_by_specialization(spec):
    df = doctors_df[(doctors_df['Specialization'].str.lower() == spec.lower()) & (doctors_df['Availability'] == "Yes")]
    return df[['Doctor', 'Timeslot']].values.tolist()

def book_appointment(doctor_name, patient_name, phone, symptoms):
    # In real app you’d save to DB or file; here we just confirm
    confirmation = f"✅ Appointment booked with *{doctor_name}* for *{patient_name}*.\n\n📞 Contact: {phone}\n🩺 Symptoms: {symptoms}"
    return confirmation