# Load libraries
import pandas as pd
import numpy as np
import codecademylib3
import matplotlib.pyplot as plt
import seaborn as sns
# Import data
students = pd.read_csv('students.csv')
#Step1
print(students.head())
#Step2
print(students.describe(include = 'all'))
#Step3 
print(f"Mean of Math Grade is :{students.math_grade.mean()}" )
#Step4 
print(f"Median of Math Grade is :{students.math_grade.median()} ")
#Step5 
print(f"Mode of Math Grade is :{students.math_grade.mode()} ")
print(f"Mode of Math Grade is :{students.math_grade.mode()[0]} ")
#Step6
print(f"Minimum of Math Grade is :{students.math_grade.min()} ")
print(f"Maximum of Math Grade is :{students.math_grade.max()} ")
#step7
print(f"standard deviation of Math Grade is :{students.math_grade.std()} ")
#Step8
print(f"Mean Absolute Deviation of Math Grade is: {students.math_grade.mad()}")
#Step9
sns.histplot(x = 'math_grade', data = students)
plt.show()
plt.clf()
#Step10
sns.boxplot(x = 'math_grade', data = students)
plt.show()
plt.clf()
#Step11
print(f"Most common data in Mjob is: \n {students.Mjob.value_counts()}")
#Step12 
print(f"Most common data in Mjob is: \n {students.Mjob.value_counts(normalize = True)}")
#Step13
sns.countplot(x = 'Mjob', data = students)
plt.show()
plt.clf()
#Step14
students.Mjob.value_counts().plot.pie()
plt.show()
plt.clf()
