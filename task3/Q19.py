import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea
   

df1= pd.read_csv("train.csv")
df2= pd.read_csv("test.csv")
combine = [df1,df2]
titanic = pd.concat(combine)
mode = titanic['Fare'].mode()
titanic['Fare']=titanic['Fare'].fillna('mode[0]')
titanic['Fare'].isnull().sum()

