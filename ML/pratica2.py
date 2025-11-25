import pandas as pd
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, LabelEncoder 
import matplotlib.pyplot as plt

data = sns.load_dataset('titanic')

data.drop(['deck', 'embark_town'], axis=1, inplace=True)
data['age'].fillna(data['age'].mean(), inplace=True)

scaler = MinMaxScaler()
data[['age', 'fare']] = scaler.fit_transform(data[['age', 'fare']])

le = LabelEncoder()
data['sex'] = le.fit_transform(data['sex'])
data['embarked'] = le.fit_transform(data['embarked'].astype(str))

sns.histplot(data['age'], bins=10, kde=True)
plt.title('Distribuição de Idade dos Passageiros')
plt.show()