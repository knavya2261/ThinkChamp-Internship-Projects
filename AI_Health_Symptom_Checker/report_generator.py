def generate_report(fever, cough, headache, bodypain, disease):

    file = open("reports/health_report.txt", "w")

    file.write("AI HEALTH SYMPTOM CHECKER REPORT\n")
    file.write("="*40 + "\n\n")

    file.write("Symptoms Entered\n")
    file.write(f"Fever      : {fever}\n")
    file.write(f"Cough      : {cough}\n")
    file.write(f"Headache   : {headache}\n")
    file.write(f"Body Pain  : {bodypain}\n\n")

    file.write(f"Predicted Disease : {disease}\n\n")

    file.write("Suggestion:\n")

    if disease == "Flu":
        file.write("Drink plenty of water and take proper rest.\n")

    elif disease == "Dengue":
        file.write("Consult a doctor immediately.\n")

    elif disease == "Cold":
        file.write("Take warm fluids and get enough sleep.\n")

    elif disease == "Migraine":
        file.write("Take rest in a quiet room and consult a doctor if needed.\n")

    else:
        file.write("No major disease detected.\n")

    file.close()