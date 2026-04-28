import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# Load Data
# ---------------------------
df = pd.read_csv("students.csv")

st.title("Student Performance Dashboard")


# ---------------------------
# Basic Stats
# ---------------------------
st.subheader("Summary Statistics")
st.write(df.describe())

# ---------------------------
# Grade Distribution (Pie Chart)
# ---------------------------
st.subheader("Grade Distribution")

grade_counts = df['Grade'].value_counts()

fig1, ax1 = plt.subplots()
ax1.pie(grade_counts, labels=grade_counts.index, autopct='%1.1f%%')
ax1.set_title("Grade Distribution")

st.pyplot(fig1)

# ---------------------------
# Marks per Student (Bar Chart)
# ---------------------------
st.subheader("Marks per Student")

fig2, ax2 = plt.subplots()
ax2.bar(df['StudentID'], df['Marks'])
ax2.set_xlabel("Student ID")
ax2.set_ylabel("Marks")

st.pyplot(fig2)

# ---------------------------
# Study Hours vs Marks (Scatter Plot)
# ---------------------------
st.subheader("Study Hours vs Marks")

fig3, ax3 = plt.subplots()
ax3.scatter(df['StudyHours'], df['Marks'])
ax3.set_xlabel("Study Hours")
ax3.set_ylabel("Marks")

st.pyplot(fig3)

# ---------------------------
# Attendance vs Marks (Scatter)
# ---------------------------
st.subheader("Attendance vs Marks")

fig4, ax4 = plt.subplots()
ax4.scatter(df['Attendance'], df['Marks'])
ax4.set_xlabel("Attendance")
ax4.set_ylabel("Marks")

st.pyplot(fig4)

# ---------------------------
# Top Performers
# ---------------------------
st.subheader("Top 5 Students")

top_students = df.sort_values(by="Marks", ascending=False).head(5)
st.write(top_students)

# ---------------------------
# Filter Option
# ---------------------------
st.subheader("Filter by Grade")

grade_option = st.selectbox("Select Grade", df['Grade'].unique())
filtered = df[df['Grade'] == grade_option]

st.write(filtered)