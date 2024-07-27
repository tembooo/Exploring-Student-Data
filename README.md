# Exploring-Student-Data
Imagine that you work for a school district and have collected some data on local students and their parents. You’ve been tasked with answering some important questions.
* How are students performing in their math classes?
* What do students’ parents do for work?
* How often are students absent from school?
<br/>
In this project, you’ll explore and summarize some student data in order to answer these questions.
Data citation:
Dua, D. and Graff, C. (2019). UCI Machine Learning Repository Irvine, CA: University of California, School of Information and Computer Science.<br/>
http://archive.ics.uci.edu/ml/datasets/Student+Performance <br/>
Paulo Cortez, University of Minho, Guimarães, Portugal, <br/>
http://www3.dsi.uminho.pt/pcortez 
<br/>
<br/> `I use Code Academy lesson.` <br/>
`Improve appereance with this link:` <a href="[https://bit.ly/2BNk3P1](https://github.com/noob-hackers/grabcam/edit/master/README.md)"> https://github.com/noob-hackers/grabcam/edit/master/README.md <a> <br/>

# Initial exploration

Detect variables/feature

## Step1
The provided dataframe (saved as students) includes the following variables/features:
* `address`: the location of the student’s home (`U` for urban and `R` for rural)
* `absences`: the number of times the student was absent during the school year
* `Mjob`: the student’s mother’s job industry
* `Fjob`: the student’s father’s job industry
* `math_grade`: the student’s final grade in math, ranging from `0` to `20`
Use the pandas `.head()` method to inspect the first few rows of data.
```python
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
```
## Step2
Use the pandas `.describe()` method to print out summary statistics for all five features in the dataset. Inspect the output. Do more students live in urban or rural locations?
Make sure to use `include = 'all’` to include all of the columns in the dataset.
```python
#Step2
print(students.describe(include = 'all'))

```
# Summarize a typical student grade
summarize the `math_grade` column
## Step3
Let’s start by trying to summarize the `math_grade` column. 
Calculate and print the mean value of `math_grade`.
```python
#Step3 
print(f"Mean of Math Grade is :{students.math_grade.mean()}" )

```
## Step4 median 
Next, calculate and print the median value of `math_grade`. Compare this value to the mean. Is it smaller? larger?
```python
#Step4 
print(f"Median of Math Grade is :{students.math_grade.median()} ")

```
## Step5 
Finally, calculate and print the mode of the `math_grade` column. What is the most common grade earned by students in this dataset? How different is this number from the mean and median?
Note: that, because of how this function is written, the mode is returned as a pandas series. In order to convert it to a single value, we can extract the first value in the series (eg., `students.math_grade.mode()[0]`)
```python
#Step5 
print(f"Mode of Math Grade is :{students.math_grade.mode()} ")
print(f"Mode of Math Grade is :{students.math_grade.mode()[0]} ")
```
![image](https://github.com/user-attachments/assets/8d44a32e-3ee9-4298-a39c-fac06cddf4a1)




