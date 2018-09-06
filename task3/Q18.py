import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea
   

df1= pd.read_csv("train.csv")
df2= pd.read_csv("test.csv")
combine = [df1,df2]
titanic = pd.concat(combine)
titanic['Embarked'].describe()
titanic['Embarked'].isnull().sum()
titanic['Embarked']=titanic['Embarked'].fillna('S')
titanic['Embarked'].isnull().sum()


