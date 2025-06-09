
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Load data
df = pd.read_csv("student_lifestyle_dataset.csv")

st.title("🎓 Student Lifestyle & Performance Dashboard📚")

# Sidebar filters
st.sidebar.header("Filter by Stress Level")
stress_filter = st.sidebar.multiselect("Choose Stress Levels", options=df["Stress_Level"].unique(), default=df["Stress_Level"].unique())
filtered_df = df[df["Stress_Level"].isin(stress_filter)]

# Tabs for each objective
tab1, tab2, tab3 = st.tabs([" 🗂️Academic Performance", " 🗂️Stress Levels", " 🗂️Time Allocation"])

# ---------------- OBJECTIVE 1 ----------------
with tab1:
    st.subheader("Objective 1: Impact of Daily Activities on GPA")

  

    # Scatter plots
    st.markdown("####  GPA vs. Activity Hours")
    for col in ["Study_Hours_Per_Day", "Sleep_Hours_Per_Day", "Extracurricular_Hours_Per_Day", "Social_Hours_Per_Day", "Physical_Activity_Hours_Per_Day"]:
        fig = px.scatter(df, x=col, y="GPA", title=f"GPA vs. {col.replace('_', ' ')}")
        st.plotly_chart(fig)



# ---------------- OBJECTIVE 2 ----------------
with tab2:
    st.subheader("Objective 2: Stress Levels vs. Lifestyle")

    # Distribution plots
    st.markdown("####  Activity Distribution by Stress Level")
    for col in ["Study_Hours_Per_Day", "Sleep_Hours_Per_Day", "Physical_Activity_Hours_Per_Day"]:
        fig = px.histogram(filtered_df, x=col, color="Stress_Level", barmode="overlay", nbins=20, title=f"{col.replace('_', ' ')} Distribution")
        st.plotly_chart(fig)

    
# ---------------- OBJECTIVE 3 ----------------
with tab3:
    st.subheader("Objective 3: Time Allocation & Optimization")

    # Average time usage pie chart
    st.markdown("####  Average Time Usage")
    time_cols = ["Study_Hours_Per_Day", "Sleep_Hours_Per_Day", "Extracurricular_Hours_Per_Day", "Social_Hours_Per_Day", "Physical_Activity_Hours_Per_Day"]
    avg_time = df[time_cols].mean()
    fig = px.pie(values=avg_time, names=avg_time.index, title="Average Daily Time Allocation")
    st.plotly_chart(fig)

    # Compare High vs. Low GPA earners
    st.markdown("####  High vs. Low GPA Time Allocation")
    top_gpa = df[df["GPA"] >= df["GPA"].quantile(0.75)][time_cols].mean()
    low_gpa = df[df["GPA"] <= df["GPA"].quantile(0.25)][time_cols].mean()
    compare_df = pd.DataFrame({"High GPA": top_gpa, "Low GPA": low_gpa})
    st.bar_chart(compare_df)

    
