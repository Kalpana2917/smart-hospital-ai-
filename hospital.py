patients=[
    {"id": "P1", "name":"Annu", "age":23, "symptom":"fever"},
    {"id":"P2", "name":"Sagun", "age":27, "symptom":"headache"}
]
doctors={
    "fever":"Dr. Arvi - Fever Specialization",
    "headache":"Dr. Zelda - Neuro Specialist"
}
def get_doctor(symptom):
    return doctors.get(symptom, "General Doctor")
for p in patients:
    doctor=get_doctor(p["symptom"])
    print(f"{p['name']} will get-> {doctor}")
