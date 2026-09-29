import streamlit as st

st.set_page_config(page_title="CareRoute - Smart Hospital AI", page_icon="🏥")
st.title("🏥 CareRoute: Patient Registration & Doctor Suggestion")
st.caption("By Kalpana Singhmar | MCA, Panjab University | VJ Hackathon 2026")

# MODULAR RULES - Easy to extend to CSV/SQLite
DOCTOR_RULES = {
    "General Physician": ["fever", "cold", "cough", "flu", "viral"],
    "Cardiologist": ["chest pain", "heart pain", "chest tightness", "bp high"],
    "Orthopedic": ["bone pain", "joint pain", "fracture", "knee pain", "back pain"],
    "Dermatologist": ["rash", "skin", "itching", "acne"],
    "ENT Specialist": ["throat pain", "ear pain", "cold", "sinus"]
}

URGENCY_KEYWORDS = ["chest pain", "breathing difficulty", "unconscious", "severe bleeding", "heart attack"]

def normalize_symptom(symptom):
    # Synonym & spelling handling
    symptom = symptom.lower().strip()
    replacements = {"feever": "fever", "jont pain": "joint pain", "hart pain": "heart pain", "skinn": "skin"}
    for wrong, correct in replacements.items():
        symptom = symptom.replace(wrong, correct)
    return symptom

def suggest_doctors(symptom_text):
    symptom_text = normalize_symptom(symptom_text)
    scores = {}
    found_symptoms = []

    for specialty, keywords in DOCTOR_RULES.items():
        for kw in keywords:
            if kw in symptom_text:
                scores[specialty] = scores.get(specialty, 0) + 1
                found_symptoms.append(kw)

    # Ranked suggestions
    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    # Urgency check
    urgency = any(u in symptom_text for u in URGENCY_KEYWORDS)

    if not ranked:
        return [("General Physician", "No specific match, routine first contact")], False, found_symptoms

    # Add explanation
    result = []
    for specialty, count in ranked[:2]: # Top 2
        result.append((specialty, f"Matched keywords: {', '.join(found_symptoms)}"))

    return result, urgency, found_symptoms

# UI
st.header("Patient Registration")
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Patient Name")
with col2:
    age = st.number_input("Age", 1, 100, 22)

symptom = st.text_area("Enter Symptoms (e.g. fever with rash, chest pain and cough)")

if st.button("Suggest Doctor"):
    if name == "" or symptom == "":
        st.warning("Please fill both Name and Symptoms!")
    else:
        doctors, is_urgent, matched = suggest_doctors(symptom)

        if is_urgent:
            st.error("⚠️ URGENCY FLAG: Your symptoms need immediate medical attention. Please visit ER / Emergency immediately. This is not a diagnosis.")

        st.success(f"Hello {name}, Here is AI Navigation Support:")
        for doc, reason in doctors:
            st.write(f"**Suggested: {doc}**")
            st.caption(f"Why? {reason}")

        st.info("Note: This is navigation support, not a medical diagnosis. Please consult a qualified doctor.")
        st.balloons()

st.divider()
st.write("Project: CareRoute | Prototype: mq5jvukyqnwj3dxcqlhsnw.streamlit.app")
