# -*- coding: utf-8 -*-
"""
Created on Sun May 31 09:52:55 2026

@author: SANTOSH KUMAR SHARMA
"""

# Student Performance Analysis Project 🚀

import pandas as pd
import matplotlib.pyplot as plt

# =========================
# Student Dataset
# =========================

data = {
    "Name": ["Mohan", "Das", "Karam", "Chand", "Gandhi"],
    "English": [78, 90, 65, 64, 68],
    "Math": [88, 65, 75, 86, 62],
    "Science": [84, 85, 77, 66, 86],
    "Art": [88, 59, 90, 92, 76]
}

# Create DataFrame

df = pd.DataFrame(data)

# Save dataset to CSV

df.to_csv("student_performance.csv", index=False)

print("Student dataset created successfully.")
print("=" * 70)

# Read CSV file

df = pd.read_csv("student_performance.csv")

print("Student Dataset:")
print(df)
print("=" * 70)

# =========================
# Data Analysis
# =========================

# Calculate total marks

df["Total"] = (
    df["English"] +
    df["Math"] +
    df["Science"] +
    df["Art"]
)

# Calculate percentage

df["Percentage"] = (df["Total"] / 400) * 100

# Find topper

topper = df[df["Total"] == df["Total"].max()]

print("Top Scorer:")
print(topper)
print("=" * 70)

# Students scoring above 80%

high_performers = df[df["Percentage"] > 80]

print("Students Scoring Above 80%:")
print(high_performers)
print("=" * 70)

# =========================
# Grade Calculation
# =========================

grades = []

for percentage in df["Percentage"]:

    if percentage >= 90:
        grades.append("A")

    elif percentage >= 75:
        grades.append("B")

    elif percentage >= 60:
        grades.append("C")

    else:
        grades.append("Fail")

# Add grade column

df["Grade"] = grades

print("Final Student Report:")
print(df)
print("=" * 70)

# =========================
# Data Visualization
# =========================

plt.figure(figsize=(8, 5))

plt.bar(df["Name"], df["Total"])

plt.xlabel("Students")
plt.ylabel("Total Marks")
plt.title("Student Performance Analysis")

plt.show()