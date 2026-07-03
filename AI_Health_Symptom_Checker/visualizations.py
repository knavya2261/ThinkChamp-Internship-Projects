import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_charts():

    data = pd.read_csv("datasets/health_dataset.csv")

    # Bar Chart
    disease_count = data["Disease"].value_counts()

    plt.figure(figsize=(6,4))
    disease_count.plot(kind="bar")
    plt.title("Disease Count")
    plt.xlabel("Disease")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("images/bar_chart.png")
    plt.close()

    # Pie Chart
    plt.figure(figsize=(6,6))
    disease_count.plot(kind="pie", autopct="%1.1f%%")
    plt.ylabel("")
    plt.title("Disease Distribution")
    plt.tight_layout()
    plt.savefig("images/pie_chart.png")
    plt.close()

    # Heatmap
    plt.figure(figsize=(6,4))
    sns.heatmap(data.corr(numeric_only=True), annot=True, cmap="Blues")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig("images/heatmap.png")
    plt.close()

    print("\nCharts saved inside Images folder.")