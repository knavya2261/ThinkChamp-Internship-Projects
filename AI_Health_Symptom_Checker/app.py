from symptom_checker import check_symptoms
from data_analysis import analyze_data
from visualizations import create_charts
from report_generator import generate_report

print("="*50)
print("     AI HEALTH SYMPTOM CHECKER")
print("="*50)

print("\nEnter your symptoms")
print("(Type Yes or No)\n")

fever = input("Fever : ")
cough = input("Cough : ")
headache = input("Headache : ")
bodypain = input("Body Pain : ")

disease = check_symptoms(fever, cough, headache, bodypain)

print("\nPossible Disease :", disease)

analyze_data()

create_charts()

generate_report(fever, cough, headache, bodypain, disease)

print("\nHealth report generated successfully.")