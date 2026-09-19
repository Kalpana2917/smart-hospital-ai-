import sqlite3
def suggest_doctor(symptom):
    #AI Logic
    symptom=symptom.lower()
    if "fever" in symptom:
        return "Dr. Gupta - Fever Specialist"
    elif "chest" in symptom or "heart" in symptom:
        return "Dr. Sharma - Heart Specialist"
    elif "cold" in symptom or "cough" in symptom:
        return "Dr. Singh - ENT Specialist"
    else:
        return "DR. General - General Physician"
def save_patient(name, symptom, doctor):
    conn=sqlite3.connect("hospital.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS patients (name TEXT, symptom TEXT, doctor TEXT)")
    cur.execute("INSERT INTO patients VALUES (?, ?, ?)", (name, symptom, doctor))
    conn.commit()
    conn.close()
    print(f"Saved: {name} | Symptom: {symptom} -> Suggested: {doctor}")
#Testing AI
patient_name="Aman"
patient_symptom="chest pain"
#AI is thinking
doctor = suggest_doctor(patient_symptom)
#Saving
save_patient(patient_name, patient_symptom, doctor)
print(f"\nAI Result :For '{patient_symptom}', you should meet{doctor}")
