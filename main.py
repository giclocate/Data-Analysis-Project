import pandas as pd
import numpy as np

data = pd.read_csv('Salaries.csv')

# 1.  Display Top 10 Rows of The Dataset
print("The first 10 rows of the DataSet are: ")
print(data.head(10))
print("\n")

# 2. Check Last 10 Rows of The Dataset
print("The last 10 rows of the DataSet are: ")
print(data.tail(10))
print("\n")
# 3. Find Shape of Our Dataset (Number of Rows And Number of Columns)
print("The number of rows of the DataSet is: ", data.shape[0])
print("\n")
print("The number of columns of the DataSet is: ", data.shape[1])
print("\n")
print("The number of rows and columns of the DataSet is: ", data.shape)
print("\n")

# 4.  Getting Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement
# Converter colunas numéricas específicas para float, ignorando erros
cols = ['BasePay', 'OvertimePay', 'OtherPay', 'Benefits', 'TotalPay', 'TotalPayBenefits', 'Status']
for col in cols:
    data[col] = pd.to_numeric(data[col], errors='coerce')  # Converte e ignora erros
print(data.info())
print("\n")

# 5. Check Null Values In The Dataset
print(data.isnull().sum())
print("\n")

# 6. Drop ID, Notes, Agency, and Status Columns
print("The columns ID, Notes, Agency, and Status are dropped from the DataSet: ")
data = data.drop(['Id', 'Notes', 'Agency', 'Status'], axis=1)
print(data.head())
print("\n")

# 7. Get Overall Statistics About The Dataframe
print("The overall statistics about the DataSet are: ")
print(data.describe())
print("\n")

# 8. Find Occurrence of The Employee Names  (Top 5)
print("The occurrence of the Employee Names are: ")
print(data['EmployeeName'].value_counts().head())
print("\n")

# 9. Find The Number of Unique Job Titles
print("The number of unique Job Titles are: ")
print(data['JobTitle'].nunique())

# 10.Total Number of Job Titles Contain Captain
print("The total number of Job Titles contain Captain are: ")
print(data[data['JobTitle'].str.contains('Captain', case=False)].shape[0])
print("\n")

# 11. Display All the Employee Names From Fire Department
print("The Employee Names from Fire Department are: ")
print(data[data['JobTitle'].str.contains('Fire', case=False)]['EmployeeName'])
print("\n")

# 12. Find Minimum, Maximum, and Average BasePay
print("The minimum, maximum, and average BasePay are: ")
print(data['BasePay'].describe())
print("\n")
# 13. Replace 'Not Provided' in EmployeeName' Column to NaN 
print("The 'Not Provided' in EmployeeName Column is replaced by NaN: ")
data['EmployeeName'] = data['EmployeeName'].replace('Not provided', np.nan)
print(data['EmployeeName'])
print("\n") 

# 14. Drop The Rows Having 5 Missing Values
print("The rows having 5 missing values are dropped: ")
data.drop(data[data.isnull().sum(axis=1) == 5].index, axis=0, inplace=True)
print(data.isnull().sum(axis=1))
print("\n")

# 15. Find Job Title of ALBERT PARDINI
print("The Job Title of ALBERT PARDINI is: ")
print(data[data['EmployeeName'] == 'ALBERT PARDINI']['JobTitle'])
print("\n")

# 16. How Much ALBERT PARDINI Make (Include Benefits)?
print("The amount ALBERT PARDINI make is: ")
print(data[data['EmployeeName'] == 'ALBERT PARDINI']['TotalPayBenefits'])
print("\n")

# 17.Display Name of The Person Having The Highest BasePay
data['BasePay'] = pd.to_numeric(data['BasePay'], errors='coerce')
# Encontre a pessoa com o maior 'BasePay'
print("The name of the person having the highest BasePay is: ")
print(data[data['BasePay'] == data['BasePay'].max()]['EmployeeName'])

# 18.Find Average BasePay of All Employee Per Year 
print("The average BasePay of all employees per year is: ")
print(data.groupby('Year')['BasePay'].mean())
print("\n")

# 19. Find Average BasePay of All Employee Per JobTitle 
print("The average BasePay of all employees per JobTitle is: ")
print(data.groupby('JobTitle')['BasePay'].mean())
print("\n")

# 20. Find Average BasePay of Employee Having Job Title ACCOUNTANT  
print("The average BasePay of employees having Job Title ACCOUNTANT is: ")
print(data[data['JobTitle'] == 'ACCOUNTANT']['BasePay'].mean())
print("\n")

# 21. Find Top 5 Most Common Jobs
print("The top 5 most common jobs are: ")
print(data['JobTitle'].value_counts().head())
print("\n")