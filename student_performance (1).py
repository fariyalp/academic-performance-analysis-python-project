# import pandas as pd
# # df = pd.read_csv("student_grades.csv")import pandas as pd

# df = pd.read_csv("student_grades.csv")

# print(df)


# import pandas as pd

# # Import dataset
# df = pd.read_csv("student_grades.csv")

# # Display first 5 rows
# print("FIRST 5 RECORDS")
# print(df.head())

# # Display number of rows and columns
# print("\nDATASET SHAPE")
# print(df.shape)

# # Display column names
# print("\nCOLUMN NAMES")
# print(df.columns)

# # Display basic information
# print("\nDATASET INFORMATION")
# print(df.info())




# import matplotlib.pyplot as plt

# print("Matplotlib installed successfully!")
# import pandas as pd
# import matplotlib.pyplot as plt



#graph 1
# import pandas as pd
# import matplotlib.pyplot as plt

# # ---------------------------------------
# # 1. LOAD DATASET
# # ---------------------------------------

# df = pd.read_csv("student_grades.csv")

# print("STUDENT ACADEMIC PERFORMANCE ANALYSIS")
# print("--------------------------------------")

# print("\nFirst 5 Records:")
# print(df.head())

# print("\nDataset Information:")
# print(df.info())

# print("\nTotal Number of Records:", len(df))

# print("\nNumber of Students:", df["Student_ID_Source"].nunique())

# print("Number of Courses:", df["Course_ID_Source"].nunique())

# print("Number of Professors:", df["Professor_ID_Source"].nunique())

# print("Number of Semesters:", df["Semester_ID_Source"].nunique())


# # ---------------------------------------
# # 2. GRADE TO GRADE POINT CONVERSION
# # ---------------------------------------

# grade_points = {
#     "A+": 4.0,
#     "A": 4.0,
#     "A-": 3.7,
#     "B+": 3.3,
#     "B": 3.0,
#     "B-": 2.7,
#     "C+": 2.3,
#     "C": 2.0,
#     "C-": 1.7,
#     "D": 1.0,
#     "F": 0.0
# }

# df["Grade_Point"] = df["Letter_Grade"].map(grade_points)

# print("\nDataset with Grade Points:")
# print(df.head())


# # ---------------------------------------
# # 3. OVERALL AVERAGE GRADE POINT
# # ---------------------------------------

# overall_average = df["Grade_Point"].mean()

# print("\nOverall Average Grade Point:",
#       round(overall_average, 2))


# # ---------------------------------------
# # 4. STUDENT-WISE PERFORMANCE
# # ---------------------------------------

# student_performance = df.groupby(
#     "Student_ID_Source"
# )["Grade_Point"].mean().sort_values(ascending=False)

# print("\nStudent-wise Average Grade:")
# print(student_performance)


# # ---------------------------------------
# # 5. TOP PERFORMING STUDENTS
# # ---------------------------------------

# print("\nTop 5 Performing Students:")

# print(student_performance.head(5))


# # ---------------------------------------
# # 6. COURSE-WISE PERFORMANCE
# # ---------------------------------------

# course_performance = df.groupby(
#     "Course_ID_Source"
# )["Grade_Point"].mean().sort_values(ascending=False)

# print("\nCourse-wise Average Grade:")
# print(course_performance)


# # ---------------------------------------
# # 7. PROFESSOR-WISE PERFORMANCE
# # ---------------------------------------

# professor_performance = df.groupby(
#     "Professor_ID_Source"
# )["Grade_Point"].mean().sort_values(ascending=False)

# print("\nProfessor-wise Average Grade:")
# print(professor_performance)


# # ---------------------------------------
# # 8. SEMESTER-WISE PERFORMANCE
# # ---------------------------------------

# semester_performance = df.groupby(
#     "Semester_ID_Source"
# )["Grade_Point"].mean()

# print("\nSemester-wise Average Grade:")
# print(semester_performance)


# # ---------------------------------------
# # 9. GRADE DISTRIBUTION
# # ---------------------------------------

# grade_distribution = df["Letter_Grade"].value_counts()

# print("\nGrade Distribution:")
# print(grade_distribution)


# # ---------------------------------------
# # 10. PASS AND FAIL ANALYSIS
# # ---------------------------------------

# df["Result"] = df["Letter_Grade"].apply(
#     lambda x: "Fail" if x == "F" else "Pass"
# )

# result_count = df["Result"].value_counts()

# print("\nPass/Fail Analysis:")
# print(result_count)


# # ---------------------------------------
# # 11. PASS PERCENTAGE
# # ---------------------------------------

# pass_percentage = (
#     (df["Result"] == "Pass").sum() / len(df)
# ) * 100

# fail_percentage = (
#     (df["Result"] == "Fail").sum() / len(df)
# ) * 100

# print("\nPass Percentage:",
#       round(pass_percentage, 2), "%")

# print("Fail Percentage:",
#       round(fail_percentage, 2), "%")


# # ---------------------------------------
# # 12. BEST COURSE
# # ---------------------------------------

# best_course = course_performance.idxmax()

# print("\nCourse with Highest Average Grade:",
#       best_course)

# print("Average Grade Point:",
#       round(course_performance.max(), 2))


# # ---------------------------------------
# # 13. LOWEST PERFORMING COURSE
# # ---------------------------------------

# lowest_course = course_performance.idxmin()

# print("\nCourse with Lowest Average Grade:",
#       lowest_course)

# print("Average Grade Point:",
#       round(course_performance.min(), 2))


# # ---------------------------------------
# # 14. VISUALIZATION - GRADE DISTRIBUTION
# # ---------------------------------------

# plt.figure(figsize=(8, 5))

# grade_distribution.plot(kind="bar")

# plt.title("Grade Distribution")
# plt.xlabel("Letter Grade")
# plt.ylabel("Number of Students")

# plt.tight_layout()
# plt.show()


# # ---------------------------------------
# # 15. VISUALIZATION - COURSE PERFORMANCE
# # ---------------------------------------

# plt.figure(figsize=(10, 5))

# course_performance.plot(kind="bar")

# plt.title("Course-wise Average Grade Point")
# plt.xlabel("Course")
# plt.ylabel("Average Grade Point")

# plt.xticks(rotation=45)

# plt.tight_layout()
# plt.show()


# # ---------------------------------------
# # 16. VISUALIZATION - SEMESTER PERFORMANCE
# # ---------------------------------------

# plt.figure(figsize=(7, 5))

# semester_performance.plot(
#     kind="bar"
# )

# plt.title("Semester-wise Average Performance")
# plt.xlabel("Semester")
# plt.ylabel("Average Grade Point")

# plt.tight_layout()
# plt.show()


# # ---------------------------------------
# # 17. SAVE ANALYSIS RESULTS
# # ---------------------------------------

# student_performance.to_csv(
#     "student_performance_results.csv"
# )

# course_performance.to_csv(
#     "course_performance_results.csv"
# )

# print("\nAnalysis completed successfully!")

# print("Result files have been created.")



#graph2
# import matplotlib.pyplot as plt

# df = pd.read_csv("student_grades.csv")

# grade_count = df["Letter_Grade"].value_counts()

# plt.figure(figsize=(8, 5))
# plt.bar(grade_count.index, grade_count.values)

# plt.title("Grade Distribution")
# plt.xlabel("Letter Grade")
# plt.ylabel("Number of Students")

# plt.show() 



#graph 3

# result = df["Letter_Grade"].apply(
#     lambda x: "Fail" if x == "F" else "Pass"
# )

# result_count = result.value_counts()

# plt.figure(figsize=(6, 6))
# plt.pie(
#     result_count.values,
#     labels=result_count.index,
#     autopct="%1.1f%%"
# )

# plt.title("Pass vs Fail Percentage")

# plt.show()
# import pandas as pd

#graph4

# grade_points = {
#     "A+": 4.0,
#     "A": 4.0,
#     "A-": 3.7,
#     "B+": 3.3,
#     "B": 3.0,
#     "B-": 2.7,
#     "C+": 2.3,
#     "C": 2.0,
#     "C-": 1.7,
#     "D": 1.0,
#     "F": 0.0
# }

# df["Grade_Point"] = df["Letter_Grade"].map(grade_points)

# course_average = df.groupby(
#     "Course_ID_Source"
# )["Grade_Point"].mean()

# plt.figure(figsize=(10, 5))
# plt.bar(course_average.index, course_average.values)

# plt.title("Course-wise Average Grade Point")
# plt.xlabel("Course")
# plt.ylabel("Average Grade Point")

# plt.xticks(rotation=45)
# plt.tight_layout()

# plt.show()