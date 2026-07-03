import pandas as pd
import numpy as np

def analyze_data():

    print("\nAnalyzing Dataset...")

    data = pd.read_csv("datasets/health_dataset.csv")

    print("\nTotal Records :", len(data))

    print("Total Diseases :", data["Disease"].nunique())

    print("\nDisease Count")

    print(data["Disease"].value_counts())

    average = np.mean(data["Fever"])

    print("\nAverage Fever Value :", average)