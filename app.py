import streamlit as st
st.title("student performance analysis ")
st.subheader("welcome to my project")
st.write("this project analyze student performance using python")
import pandas as pd 
df=pd.read_csv("dataset/student-mat.csv",sep=";")
st.subheader("student dataset")
st.dataframe(df)
st.write("Column Names:", df.columns.tolist())
st.metric("total student ",df.shape[0])
average=df["G3"].mean()
st.metric("average final marks",round(average,2))
total_students=df.shape[0]
st.metric("total students",total_students)
highest_marks=df["G3"].max()
st.metric("highest marks",highest_marks)
lowest_marks=df["G3"].min()
st.metric("lowest marks",lowest_marks)
st.subheader("Average Marks Comparision")
average_marks=df[["G1","G2","G3"]].mean()
st.bar_chart(average_marks)
import matplotlib.pyplot as plt
st.subheader("Marks Distribution")
plt.hist(df["G3"],bins=10)
plt.xlabel("Final marks")
plt.ylabel("Number of students")
st.pyplot(plt)
plt.clf()
st.subheader("Student Performance Insights")
passed_students=df[df["G3"]>=10]
st.metric("Students scoring 10 or above",len(passed_students))
st.subheader("Pass and Fail Analysis")
failed_students = df[df["G3"] < 10]
total_passed = len(passed_students)
total_failed = len(failed_students)
pass_percentage = (total_passed / len(df)) * 100
st.metric("Failed Students", total_failed)
st.metric("Pass Percentage", round(pass_percentage, 2))
st.subheader("Pass vs Fail Students")
labels = ["Passed", "Failed"]
values = [total_passed, total_failed]
plt.pie(values, labels=labels, autopct="%1.1f%%",
        startangle=90)
st.pyplot(plt)
plt.clf()
st.subheader("Subject-wise Performance")
subject_avg = df[["G1", "G2", "G3"]].mean()
st.write("Average Marks in Each Grade")
st.bar_chart(subject_avg)
st.subheader("Gender-wise Performance")
gender_avg = df.groupby("sex")["G3"].mean()
st.bar_chart(gender_avg)
st.subheader("Student Performance Filter")
gender=st.selectbox("select sex",["All","M","F"])
if gender == "All": 
        filtered_df=df
else:
        filtered_df=df[df["sex"]==gender]
st.subheader("Filtered Student Analysis")
average_marks = filtered_df["G3"].mean()
st.metric("Average Final Marks", round(average_marks, 2))
total_students = len(filtered_df)
st.metric("Total Students", total_students)
st.subheader("Student Details")
st.dataframe(filtered_df)
st.subheader("Subject-wise Average Marks")
avg_g1 = filtered_df["G1"].mean()
avg_g2 = filtered_df["G2"].mean()
avg_g3 = filtered_df["G3"].mean()
col1, col2, col3 = st.columns(3)
col1.metric("G1 Average", round(avg_g1, 2))
col2.metric("G2 Average", round(avg_g2, 2))
col3.metric("G3 Average", round(avg_g3, 2))
st.subheader("Subject Average Comparison")
average_data = {
    "Subject": ["G1", "G2", "G3"],
    "Average Marks": [avg_g1, avg_g2, avg_g3]
}
average_df = pd.DataFrame(average_data)
st.bar_chart(average_df.set_index("Subject"))
best_subject = max(
    avg_g1,
    avg_g2,
    avg_g3
)
if best_subject == avg_g1:
    st.success("G1 has the highest average marks!")
elif best_subject == avg_g2:
    st.success("G2 has the highest average marks!")
else:
    st.success("G3 has the highest average marks!")
st.subheader("Performance Summary")
highest_marks = filtered_df["G3"].max()
lowest_marks = filtered_df["G3"].min()
col1, col2 = st.columns(2)
col1.metric("Highest Marks", highest_marks)
col2.metric("Lowest Marks", lowest_marks)
st.subheader("Student Performance Overview")
st.write("Total Students:", len(df))
st.write("Average Final Marks:", df["G3"].mean())
st.write("Highest Final Marks:", df["G3"].max())
st.write("Lowest Final Marks:", df["G3"].min())
st.write("Lowest Final Marks:", df["G3"].min())
st.subheader("Grade-wise Student Analysis")
def grade(marks):
    if marks >= 15:
        return "Excellent"
    elif marks >= 10:
        return "Good"
    else:
        return "Needs Improvement"
df["Grade"] = df["G3"].apply(grade)
st.write(df["Grade"].value_counts())
st.bar_chart(df["Grade"].value_counts())
st.subheader("Absences vs Final Marks")
st.scatter_chart(
    df,
    x="absences",
    y="G3"
)
st.subheader("Absences vs Final Marks")
st.subheader("Average Marks by Absence Group")
def attendance_group(days):
    if days <= 5:
        return "Low Absence"
    elif days <= 10:
        return "Medium Absence"
    else:
        return "High Absence"
df["Attendance Group"] = df["absences"].apply(attendance_group)
avg_marks = df.groupby("Attendance Group")["G3"].mean()
st.write(avg_marks)
st.bar_chart(avg_marks)
st.subheader("Student Marks Progress Analysis")
avg_g1 = df["G1"].mean()
avg_g2 = df["G2"].mean()
avg_g3 = df["G3"].mean()
st.write("Average G1 Marks:", round(avg_g1, 2))
st.write("Average G2 Marks:", round(avg_g2, 2))
st.write("Average G3 Marks:", round(avg_g3, 2))
progress = pd.DataFrame({
    "Exam": ["G1", "G2", "G3"],
    "Average Marks": [avg_g1, avg_g2, avg_g3]
})
st.line_chart(progress.set_index("Exam"))
st.subheader("Top 10 Performing Students")
top_students = df.sort_values(
    by="G3",
    ascending=False
).head(10)
st.write(top_students[["G1", "G2", "G3"]])
st.bar_chart(
top_students.set_index(top_students.index)["G3"]
)
st.subheader("Interactive Exam Analysis")
selected_exam = st.selectbox(
    "Select Exam",
    ["G1", "G2", "G3"]
)
st.write("Average Marks:", round(df[selected_exam].mean(), 2))
st.write("Highest Marks:", df[selected_exam].max())
st.write("Lowest Marks:", df[selected_exam].min())
exam_data = df[selected_exam].value_counts().sort_index()
st.bar_chart(exam_data)
st.subheader("Study Time vs Performance")
study_analysis = df.groupby("studytime")["G3"].mean()
st.write("Average Marks According to Study Time")
st.write(study_analysis)
st.bar_chart(study_analysis)
st.subheader("Previous Failures Analysis")
failure_analysis = df.groupby("failures")["G3"].mean()
st.write("Average Marks by Previous Failures")
st.write(failure_analysis)
st.bar_chart(failure_analysis)
st.subheader("Age-wise Performance Analysis")
age_analysis = df.groupby("age")["G3"].mean()
st.write("Average Marks According to Age")
st.write(age_analysis)
st.bar_chart(age_analysis)
st.subheader("Dataset Information")
st.write("Dataset Shape:", df.shape)
st.write("Missing Values:")
st.write(df.isnull().sum())
st.write("Duplicate Rows:", df.duplicated().sum())
duplicate_count = df.duplicated().sum()
df = df.drop_duplicates()
st.subheader("Data Cleaning Results")
st.write("Duplicate Records Found:", duplicate_count)
st.write("Total Records After Cleaning:", len(df))
st.subheader("Missing Values Handling")
missing_values = df.isnull().sum()
st.write("Missing Values Before Cleaning:")
st.write(missing_values)
df = df.dropna()
st.write("Total Records After Removing Missing Values:", len(df))
st.write("Missing Values After Cleaning:")
st.write(df.isnull().sum())
st.subheader("Data Type Verification")
st.write("Column Data Types:")
st.write(df.dtypes)
st.write("Dataset Information:")
df.info()
st.subheader("Dataset Statistical Summary")
st.write(df.describe())
st.subheader("Correlation Analysis")
correlation = df[["studytime", "absences", "failures",
                  "G1", "G2", "G3"]].corr()
st.write(correlation)
st.dataframe(correlation.style.background_gradient(cmap="coolwarm"))
st.subheader("Factors Affecting Final Marks")
g3_correlation = correlation["G3"].drop("G3")
g3_correlation = g3_correlation.sort_values(
    ascending=False
)
st.write("Relationship with Final Marks:")
st.write(g3_correlation)
st.bar_chart(g3_correlation)