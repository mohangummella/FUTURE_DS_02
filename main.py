import pandas as pd
import matplotlib.pyplot as pl
import seaborn as sb
import os

# =========================================
# CREATE FOLDERS
# =========================================

os.makedirs("images", exist_ok=True)
os.makedirs("reports", exist_ok=True)

# =========================================
# LOAD DATASET
# =========================================

df = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

print("Dataset Loaded Successfully\n")

print(df.head())

print("\nDataset Information:\n")
print(df.info())

print("\nMissing Values:\n")
print(df.isnull().sum())

print("\nChurn Count:\n")
print(df["Churn"].value_counts())

# =========================================
# DATA CLEANING
# =========================================

df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

df.dropna(inplace=True)

print("\nMissing Values After Cleaning:\n")
print(df.isnull().sum())

# =========================================
# KPI METRICS
# =========================================

total_customers = len(df)

active_customers = df[df["Churn"] == "No"].shape[0]

churned_customers = df[df["Churn"] == "Yes"].shape[0]

churn_rate = (churned_customers / total_customers) * 100

print("\n===== KPI METRICS =====")

print("Total Customers:", total_customers)
print("Active Customers:", active_customers)
print("Churned Customers:", churned_customers)
print("Churn Rate:", round(churn_rate, 2), "%")

# =========================================
# CHURN COUNT
# =========================================

sb.countplot(x="Churn", data=df)

pl.title("Customer Churn Count")
pl.xlabel("Churn")
pl.ylabel("Customer Count")

pl.tight_layout()
pl.savefig("images/churn_count.png")
pl.show()

# =========================================
# CHURN PERCENTAGE
# =========================================

churn_percentage = (
    df["Churn"].value_counts(normalize=True) * 100
)

print("\nChurn Percentage:\n")
print(churn_percentage)

# =========================================
# CONTRACT VS CHURN
# =========================================

contract_churn = pd.crosstab(
    df["Contract"],
    df["Churn"]
)

print("\nContract Wise Churn:\n")
print(contract_churn)

contract_churn.plot(
    kind="bar",
    figsize=(10, 6)
)

pl.title("Contract-wise Churn Analysis")
pl.xlabel("Contract Type")
pl.ylabel("Customer Count")

pl.tight_layout()
pl.savefig("images/contract_churn.png")
pl.show()

# =========================================
# PAYMENT METHOD VS CHURN
# =========================================

payment_churn = pd.crosstab(
    df["PaymentMethod"],
    df["Churn"]
)

print("\nPayment Method Churn:\n")
print(payment_churn)

payment_churn.plot(
    kind="bar",
    figsize=(12, 6)
)

pl.title("Payment Method Churn Analysis")
pl.xlabel("Payment Method")
pl.ylabel("Customer Count")

pl.tight_layout()
pl.savefig("images/payment_method_churn.png")
pl.show()

# =========================================
# TENURE VS CHURN
# =========================================

pl.figure(figsize=(10, 6))

sb.histplot(
    data=df,
    x="tenure",
    hue="Churn",
    multiple="stack",
    bins=30
)

pl.title("Tenure vs Churn")
pl.xlabel("Tenure (Months)")
pl.ylabel("Customer Count")

pl.tight_layout()
pl.savefig("images/tenure_vs_churn.png")
pl.show()

# =========================================
# MONTHLY CHARGES VS CHURN
# =========================================

pl.figure(figsize=(10, 6))

sb.boxplot(
    x="Churn",
    y="MonthlyCharges",
    data=df
)

pl.title("Monthly Charges vs Churn")

pl.tight_layout()
pl.savefig("images/monthly_charges_vs_churn.png")
pl.show()

# =========================================
# TOTAL CHARGES VS CHURN
# =========================================

pl.figure(figsize=(10, 6))

sb.boxplot(
    x="Churn",
    y="TotalCharges",
    data=df
)

pl.title("Total Charges vs Churn")

pl.tight_layout()
pl.savefig("images/total_charges_churn.png")
pl.show()

# =========================================
# SENIOR CITIZEN VS CHURN
# =========================================

senior_churn = pd.crosstab(
    df["SeniorCitizen"],
    df["Churn"]
)

print("\nSenior Citizen Churn:\n")
print(senior_churn)

senior_churn.plot(
    kind="bar",
    figsize=(8, 5)
)

pl.title("Senior Citizen Churn Analysis")
pl.xlabel("Senior Citizen")
pl.ylabel("Customer Count")

pl.tight_layout()
pl.savefig("images/senior_citizen_churn.png")
pl.show()

# =========================================
# INTERNET SERVICE VS CHURN
# =========================================

internet_churn = pd.crosstab(
    df["InternetService"],
    df["Churn"]
)

internet_churn.plot(
    kind="bar",
    figsize=(10, 6)
)

pl.title("Internet Service vs Churn")
pl.xlabel("Internet Service")
pl.ylabel("Customer Count")

pl.tight_layout()
pl.savefig("images/internet_service_churn.png")
pl.show()

# =========================================
# GENDER VS CHURN
# =========================================

gender_churn = pd.crosstab(
    df["gender"],
    df["Churn"]
)

gender_churn.plot(
    kind="bar",
    figsize=(8, 5)
)

pl.title("Gender vs Churn")
pl.xlabel("Gender")
pl.ylabel("Customer Count")

pl.tight_layout()
pl.savefig("images/gender_churn.png")
pl.show()

# =========================================
# PARTNER VS CHURN
# =========================================

partner_churn = pd.crosstab(
    df["Partner"],
    df["Churn"]
)

partner_churn.plot(
    kind="bar",
    figsize=(8, 5)
)

pl.title("Partner vs Churn")
pl.xlabel("Partner")
pl.ylabel("Customer Count")

pl.tight_layout()
pl.savefig("images/partner_churn.png")
pl.show()

# =========================================
# TECH SUPPORT VS CHURN
# =========================================

tech_churn = pd.crosstab(
    df["TechSupport"],
    df["Churn"]
)

tech_churn.plot(
    kind="bar",
    figsize=(10, 5)
)

pl.title("Tech Support vs Churn")
pl.xlabel("Tech Support")
pl.ylabel("Customer Count")

pl.tight_layout()
pl.savefig("images/tech_support_churn.png")
pl.show()

# =========================================
# ONLINE SECURITY VS CHURN
# =========================================

security_churn = pd.crosstab(
    df["OnlineSecurity"],
    df["Churn"]
)

security_churn.plot(
    kind="bar",
    figsize=(10, 5)
)

pl.title("Online Security vs Churn")
pl.xlabel("Online Security")
pl.ylabel("Customer Count")

pl.tight_layout()
pl.savefig("images/online_security_churn.png")
pl.show()

# =========================================
# CORRELATION HEATMAP
# =========================================

numeric_df = df.copy()

numeric_df["Churn"] = numeric_df["Churn"].map(
    {"No": 0, "Yes": 1}
)

pl.figure(figsize=(10, 6))

sb.heatmap(
    numeric_df.select_dtypes(include="number").corr(),
    annot=True,
    cmap="coolwarm"
)

pl.title("Correlation Heatmap")

pl.tight_layout()
pl.savefig("images/correlation_heatmap.png")
pl.show()

# =========================================
# REPORT GENERATION
# =========================================

with open("reports/churn_report.txt", "w") as report:

    report.write("TELCO CUSTOMER CHURN ANALYSIS REPORT\n")
    report.write("=" * 50 + "\n\n")

    report.write(f"Total Customers: {total_customers}\n")
    report.write(f"Active Customers: {active_customers}\n")
    report.write(f"Churned Customers: {churned_customers}\n")
    report.write(f"Churn Rate: {round(churn_rate,2)}%\n\n")

    report.write("Contract-wise Churn Analysis\n\n")
    report.write(contract_churn.to_string())

print("\nProject Completed Successfully!")
print("Graphs saved in images folder.")
print("Report saved in reports folder.")