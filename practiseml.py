import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

df=pd.read_csv(r'C:\Users\Joel Zerubabel\ML1\canada_per_capita_income.csv')
print(df.head(10))
X=df[['year']]
y=df[['per capita income (US$)']]
scalar=StandardScaler()
x=scalar.fit_transform(X)
model=LinearRegression(copy_X=True,fit_intercept=True, n_jobs=None)
model.fit(x,y)



print(model.coef_[0])
print(model.intercept_)
