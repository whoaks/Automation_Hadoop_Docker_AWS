import pandas
dataset=pandas.read_csv('/root/Salary_Data.csv')
y=dataset['Salary']
x=dataset['YearsExperience']
from sklearn.linear_model import LinearRegression
x=x.values
x=x.reshape(-1,1)
model=LinearRegression()
model.fit(x,y)
exp=input('\t\t\t\tEnter Value to Predict from DataSet :-   ')
print('\t\t\t\tPredicted Value is :-  ', end='')
print(model.predict([[float(exp)]]))
print()
