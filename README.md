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
# Summarize the spread of student grades
Spread Factor is important because evaluate exact position of center location. 

## Step6
Next, let’s summarize the spread of student grades. Calculate and print the range of the `math_grade` column. `.max()` and `.min()`.
```python
#Step6
print(f"Minimum of Math Grade is :{students.math_grade.min()} ")
print(f"Maximum of Math Grade is :{students.math_grade.max()} ")
```
## Step7 
Calculate and print the standard deviation of the `math_grade` column. About two thirds of values fall within one standard deviation of the mean. What does this number tell you about how much math grades vary?
The standard deviation is about 4.6, while the average grade is about 10.4. This means that about two thirds of students are earning a grade between 5.8 (calculated as 10.4 - 4.6) and 15 (calculated as 10.4 + 4.6).
```python
#step7
print(f"standard deviation of Math Grade is :{students.math_grade.std()} ")
```
## Step8 
Finally, calculate the mean absolute deviation of the `math_grade` column. This is the mean difference between each students’s score and the average score. `.mad()`.
```python
#Step8
print(f"Mean Absolute Deviation of Math Grade is: {students.math_grade.mad()}")
```
# Visualize the distribution of student grades
visualize the distribution
## Step9
Now that we’ve summarized student grades using statistics for central tendency and spread, let’s visualize the distribution using a histogram. Use the seaborn `histplot()` function to create a histogram of `math_grade`.
This ensures that the plots don’t get layered on top of each other. Make sure that you add your code to call `sns.histplot()` above `plt.show()`.
```python
#Step9
sns.histplot(x = 'math_grade', data = students)
plt.show()
plt.clf()
```
![image](https://github.com/user-attachments/assets/143daee0-c43e-48bb-8a5a-f80bee0e06af)

## Step10
Another way to visualize the distribution of a quantitative variable is using a box plot. Use the seaborn `boxplot()` function to create a boxplot of `math_grade`.
Make sure to add this code after the first call to `plt.clf()` from the above plot and before the second call to `plt.show()`.
```python
#Step10
sns.boxplot(x = 'math_grade', data = students)
plt.show()
plt.clf()
```
![image](https://github.com/user-attachments/assets/3f7b6bfc-8f02-413c-8aec-1f16c4cd2bd5)
# Summarize mothers' jobs
Jobs statics
## Step11
The `Mjob` column in the dataset contains information about what the students mothers do as a profession. Summarize the Mjob column by printing the number of students who have mothers with each job type.
Which value of `Mjob` is most common?
Use the pandas `.value_counts()` method.
```python
#Step11
print(f"Most common data in Mjob is: \n {students.Mjob.value_counts()}")

```
##Step12
Now, calculate and print the proportion of students who have mothers with each job type. What proportion of students have mothers who work in health?
Use `.value_counts(normalize = True)` to calculate the proportion of values in each category.
```python
#Step12 
print(f"Most common data in Mjob is: \n {students.Mjob.value_counts(normalize = True)}")

```
# Visualize the distribution of mothers' jobs
relative frequencies
## Step13 
Now that we’ve used summary statistics to understand the relative frequencies of different mothers’ jobs, let’s visualize the same information with a bar chart. Use the seaborn `countplot()` function to create a bar chart of the `Mjob` variable.
```python
#Step13
sns.countplot(x = 'Mjob', data = students)
plt.show()
plt.clf()

```
![image](https://github.com/user-attachments/assets/5df580fd-c3bd-4978-bcd9-fd956a131208)

## Step14
We can also visualize the same information using a pie chart. Create a pie chart of the `Mjob` column.
```python
#Step14
students.Mjob.value_counts().plot.pie()
plt.show()
plt.clf()
```
![image](https://github.com/user-attachments/assets/fd7015db-613e-42d9-8df4-992361c2bfc6)

# Full Code
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

```






