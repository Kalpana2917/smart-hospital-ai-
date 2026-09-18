import sqlite3
#Connect to database
conn=sqlite3.connect("hospital.db")
cursor=conn.cursor()
#Create table (only once)
cursor.execute("CREATE TABLE IF NOT EXISTS PATIENTS (name TEXT, symptom TEXT, doctor TEXT)")
#Function to save patient
def save_patient(name, symptom,doctor):
    cursor.execute("INSERT INTO patients VALUES(?, ?, ?)", (name, symptom, doctor))
    conn.commit()
    print(f"Saved: {name} -> {doctor}")
#Test it
save_patient("Aman", "fever", "Dr. Gupta")
print("All patients in Database:")
for row in cursor.execute("SELECT * FROM patients"):
    print(row)
