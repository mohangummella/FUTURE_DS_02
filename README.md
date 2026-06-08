# 📊 Telco Customer Churn Analysis

## 📖 Project Overview

Customer churn is one of the biggest challenges faced by telecom companies. Understanding why customers leave can help businesses improve customer satisfaction, reduce churn rates, and increase revenue.

This project analyzes customer churn data from a telecom company using Python. The analysis explores customer demographics, contract types, payment methods, internet services, tenure, and other factors that influence customer retention.

Using data visualization and exploratory data analysis (EDA), the project identifies key patterns and business insights that can help companies make data-driven decisions.

---

## 🎯 Project Objectives

The primary objectives of this project are:

* Analyze customer churn behavior
* Identify factors contributing to customer churn
* Calculate important business KPIs
* Visualize churn trends and customer characteristics
* Generate reports for business decision-making
* Provide insights to improve customer retention

---

## 📂 Dataset Information

The project uses the **Telco Customer Churn Dataset**, which contains information about telecom customers and their subscription details.

### Key Features

| Column          | Description                       |
| --------------- | --------------------------------- |
| customerID      | Unique customer identifier        |
| gender          | Customer gender                   |
| SeniorCitizen   | Senior citizen status             |
| Partner         | Whether customer has a partner    |
| Dependents      | Whether customer has dependents   |
| tenure          | Number of months with the company |
| PhoneService    | Phone service subscription        |
| InternetService | Internet service type             |
| Contract        | Contract type                     |
| PaymentMethod   | Payment method used               |
| MonthlyCharges  | Monthly billing amount            |
| TotalCharges    | Total amount charged              |
| Churn           | Customer churn status             |

---

## 🧹 Data Cleaning & Preparation

To ensure accurate analysis, the following preprocessing steps were performed:

✔ Converted TotalCharges to numeric format

✔ Handled invalid values using coercion

✔ Removed missing records

✔ Verified data quality and consistency

✔ Prepared data for visualization and KPI analysis

---

## 📊 Key Performance Indicators (KPIs)

The project calculates several important business metrics:

* 👥 Total Customers
* ✅ Active Customers
* ❌ Churned Customers
* 📉 Customer Churn Rate (%)

These KPIs provide a quick overview of customer retention performance.

---

## 📈 Analysis Performed

### 1️⃣ Customer Churn Count

Analyzes the number of customers who stayed versus those who left.

### 2️⃣ Churn Percentage Analysis

Calculates churn percentages for better business understanding.

### 3️⃣ Contract Type vs Churn

Examines how contract duration affects customer retention.

### 4️⃣ Payment Method vs Churn

Identifies payment methods associated with higher churn rates.

### 5️⃣ Tenure vs Churn

Studies how customer loyalty changes over time.

### 6️⃣ Monthly Charges vs Churn

Analyzes the relationship between monthly bills and churn behavior.

### 7️⃣ Total Charges vs Churn

Examines overall spending patterns of churned customers.

### 8️⃣ Senior Citizen Analysis

Explores churn behavior among senior customers.

### 9️⃣ Internet Service Analysis

Compares churn across different internet service types.

### 🔟 Gender Analysis

Studies churn distribution based on gender.

### 1️⃣1️⃣ Partner Status Analysis

Evaluates how partner status influences retention.

### 1️⃣2️⃣ Tech Support Analysis

Determines the impact of technical support on churn.

### 1️⃣3️⃣ Online Security Analysis

Examines whether online security services improve retention.

### 1️⃣4️⃣ Correlation Analysis

Uses a heatmap to identify relationships between numerical variables.

---

## 📷 Visualizations Generated

The project automatically generates and saves the following charts:

### Customer Churn Analysis

* Churn Count
* Churn Percentage

### Service-Based Analysis

* Contract vs Churn
* Payment Method vs Churn
* Internet Service vs Churn
* Tech Support vs Churn
* Online Security vs Churn

### Customer Demographics

* Gender vs Churn
* Senior Citizen vs Churn
* Partner vs Churn

### Financial Analysis

* Monthly Charges vs Churn
* Total Charges vs Churn

### Advanced Analytics

* Tenure vs Churn
* Correlation Heatmap

All visualizations are saved inside the **images/** folder.

---

## 📁 Project Structure

```text
Telco-Customer-Churn-Analysis/
│
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├── images/
│   ├── churn_count.png
│   ├── contract_churn.png
│   ├── payment_method_churn.png
│   ├── tenure_vs_churn.png
│   ├── monthly_charges_vs_churn.png
│   ├── total_charges_churn.png
│   ├── senior_citizen_churn.png
│   ├── internet_service_churn.png
│   ├── gender_churn.png
│   ├── partner_churn.png
│   ├── tech_support_churn.png
│   ├── online_security_churn.png
│   └── correlation_heatmap.png
│
├── reports/
│   └── churn_report.txt
│
├── telco_customer_churn_analysis.py
│
└── README.md
```

---

## 🛠️ Technologies Used

* Python
* Pandas
* Matplotlib
* Seaborn
* NumPy

---

## ⚙️ Installation

Install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn
```

---

## ▶️ How to Run the Project

### Clone the Repository

```bash
git clone https://github.com/mohangummella/telco-customer-churn-analysis.git
```

### Navigate to the Project Directory

```bash
cd telco-customer-churn-analysis
```

### Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn
```

### Run the Script

```bash
python telco_customer_churn_analysis.py
```

---

## 📄 Output

After running the project:

### Generated Visualizations

Stored in:

```text
images/
```

### Generated Report

Stored in:

```text
reports/churn_report.txt
```

### Console Output

Displays:

* Dataset Summary
* Missing Value Analysis
* Customer Churn Statistics
* KPI Metrics
* Contract Analysis
* Payment Method Analysis
* Customer Retention Insights

---

## 💡 Key Business Insights

This analysis helps answer critical business questions:

* Why are customers leaving?
* Which contract types have the highest churn?
* Does technical support improve retention?
* How do payment methods affect churn?
* Which customer groups are most likely to churn?
* What services contribute to customer loyalty?

These insights can help telecom companies design better retention strategies and improve customer satisfaction.

---

## 🚀 Future Enhancements

Potential improvements for this project include:

* Machine Learning Churn Prediction Models
* Customer Segmentation Analysis
* Feature Importance Analysis
* Interactive Dashboard using Power BI
* Tableau Visualization Dashboard
* Customer Lifetime Value Analysis
* Real-Time Churn Monitoring System

---

## 🎓 Skills Demonstrated

This project showcases practical skills in:

* Data Cleaning
* Exploratory Data Analysis (EDA)
* Customer Analytics
* Business Intelligence
* Data Visualization
* KPI Reporting
* Telecom Data Analysis
* Python Programming

---

## 👨‍💻 Author

**Mohan Gummella**

GitHub: https://github.com/mohangummella

Passionate about Data Analytics, Data Science, Business Intelligence, and Python-based Analytics Projects.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub. Contributions, suggestions, and feedback are always welcome.
