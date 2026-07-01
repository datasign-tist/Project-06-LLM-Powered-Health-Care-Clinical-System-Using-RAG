import random
import pandas as pd
import os

def generate_patient_data(num_records):
    # Pre-defined clinical profiles to keep data logically consistent
    clinical_profiles = [
        {
            "diagnosis": "Type 2 Diabetes",
            "medications": ["Metformin 500mg", "Glipizide 5mg", "Empagliflozin 10mg"],
            "notes": [
                "Patient reports frequent urination and thirst. Blood glucose levels elevated. Advised diet control.",
                "Routine follow-up for diabetes management. HbA1c is stable at 6.8%.",
                "Patient complains of mild neuropathy in toes. Adjusted medication and referred to podiatry."
            ]
        },
        {
            "diagnosis": "Hypertension",
            "medications": ["Lisinopril 10mg", "Amlodipine 5mg", "Losartan 50mg"],
            "notes": [
                "Routine checkup. BP is {sys}/{dia}. Patient complains of occasional mild headaches.",
                "BP remains elevated. Advised low-sodium diet and increased cardiovascular exercise.",
                "Patient is responding well to medication. No reported side effects. Continue current regimen."
            ]
        },
        {
            "diagnosis": "Asthma",
            "medications": ["Albuterol Inhaler", "Fluticasone Propionate", "Budesonide"],
            "notes": [
                "Patient experienced shortness of breath during exercise. Prescribed rescue inhaler for symptom management.",
                "Asthma exacerbation triggered by seasonal allergies. Increasing corticosteroid dosage.",
                "Symptoms are well controlled. Nighttime awakenings are rare. Refilled prescriptions."
            ]
        },
        {
            "diagnosis": "Osteoarthritis",
            "medications": ["Ibuprofen 400mg", "Naproxen 500mg", "Meloxicam 7.5mg"],
            "notes": [
                "Chronic joint pain in both knees. Recommended physical therapy and prescribed NSAIDs.",
                "Patient reports morning stiffness lasting about 30 minutes. X-rays show joint space narrowing.",
                "Pain is managed well with PRN medication. Discussed weight loss to reduce joint load."
            ]
        }
    ]

    data = []

    for i in range(1, num_records + 1):
        patient_id = f"P{i:06d}" # Updated to 6 digits to accommodate 100,000+ records cleanly
        age = random.randint(25, 85)
        gender = random.choice(["Male", "Female"])
        
        # Select a random clinical profile
        profile = random.choice(clinical_profiles)
        diagnosis = profile["diagnosis"]
        medication = random.choice(profile["medications"])
        note = random.choice(profile["notes"])
        
        # Add dynamic blood pressure numbers for Hypertension notes
        if diagnosis == "Hypertension" and "{sys}/{dia}" in note:
            systolic = random.randint(130, 160)
            diastolic = random.randint(85, 100)
            note = note.format(sys=systolic, dia=diastolic)
            
        data.append({
            "Patient_ID": patient_id,
            "Age": age,
            "Gender": gender,
            "Diagnosis": diagnosis,
            "Current_Medications": medication,
            "Clinical_Notes": note
        })

    # Convert to a DataFrame
    df = pd.DataFrame(data)
    return df

# --- Execution ---
if __name__ == "__main__":
    # 1 Lakh records = 100,000
    number_of_patients = 100000 
    
    # --- UPDATE YOUR FOLDER PATH HERE ---
    # For Windows use a raw string like: r"C:\Users\Name\Desktop\DataFolder"
    # For Mac/Linux use: "/Users/Name/Desktop/DataFolder"
    folder_path = r"/Users/abhisheksharma/Documents/Data Science Projects/Project-06-LLM-Powered-Health-Care-Clinical-System-Using-RAG/data" 
    
    file_name = "synthetic_patients.csv"
    
    # Safely combine the folder path and file name
    full_file_path = os.path.join(folder_path, file_name)
    
    print(f"Generating {number_of_patients} records... This might take a few moments.")
    synthetic_df = generate_patient_data(number_of_patients)
    
    # Create the directory if it doesn't already exist
    os.makedirs(folder_path, exist_ok=True)
    
    # Export the generated data to the specific path
    synthetic_df.to_csv(full_file_path, index=False)
    
    # Display the first few rows in the console
    print("\n--- Preview of Generated Data ---")
    print(synthetic_df.head())
    print(f"\n✅ Data successfully generated and saved to: {full_file_path}")