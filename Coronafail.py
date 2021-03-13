import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

df = pd.read_csv('owid-covid-data.csv')




df['date'] = df['date'].replace({'-':''}, regex = True)
#rint(df['date'].head)

z = []
#print(df['date'][74208])
for x in df['date']:
	for i in x:
		if("2020" not in x):
			z.append(x)
			
#df['date'] = z



df = df[['date', 'new_cases', 'people_vaccinated_per_hundred', 'people_fully_vaccinated_per_hundred']]
#for i in df['date']:
#	for j in z: 
#		if i == j:
			
df['date'] = pd.to_datetime(df.date, format="%Y%m%d")
print(df['date'])
df.index = df['date']

print(df.dtypes)

plt.plot(df['new_cases'], label="new cases")
plt.show() 
print(df.corr())




