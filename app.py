import streamlit as st
# Set page title and icon 
st.set_page_config(page_title="Smart Hospital AI", page_icon="🏥")
st.title("🏥 Smart Hospital AI System")
st.caption("By Kalpana Singhmar | IBM Certified")
# AI Logic to suggest doctor on symptoms
def suggest_doctor(symptom):
  symptom=symptom.lower() # Convert to lowercase
  #For fever/cold ->General Physician
  if "fever" in symptom or "cold" in symptom:
    return "Dr. Sharma (General Physician)"
  #For heart/chest -> Cardiologist
  elif "heart" in symptom or "chest" in symptom:
    return "Dr. Verma(Cardiologist)"
  #For bone/joint -> Orthopedic
  elif "bone" in symptom or "joint" in symptom:
    return "Dr. Singh (Orthopedic)"
  #For other symptom -> General Physician
  else:
    return "Dr. Gupta (General Physician)"
#Patient registration form UI
st.header("Patient Registration")
name=st.text_input("Patient Name") # Input for patient name
age=st.number_input("Age", 1, 100, 22) #input for age
symptom = st.text_area("Enter Symptom- e.g. fever, chest pain")#input for symptom
#When button is clicked , AI will suggest doctor
if st.button("Suggest Doctor"):
  #Validation check
  if name == "" or symptom == "":
    st.warning("Please fill both Name and Symptoms!")
  else:
    #Call AI function 
    doctor = suggest_doctor(symptom)
    st.success(f"Hello {name}, AI Suggested Doctor: {doctor}")
    st.balloons() #CElebration effect
st.divider()
st.write("Project Files: day1.py to day5,py + hospital.py uploaded✅")
