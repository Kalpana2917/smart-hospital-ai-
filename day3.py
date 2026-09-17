doctors={
    "fever":"Dr. Arvi - Fever Specialization",
    "headache":"Dr. Zelda - Neuro Specialist",
    "cough":"Dr. Rohan -Lung Specialist"
}
print("---Welcome to Smart Hospital AI---")
name=input("Enter patient name:")
symptom=input("Enter symptom (fever/headache/cough):").lower()
doctor=doctors.get(symptom, "General Doctor")
print(f"\n{name} will get->{doctor}")
