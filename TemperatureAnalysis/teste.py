import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('GlobalLandTemperaturesByState.csv')
print(df.head(3))

Brazil = df['Country'] == 'Brazil'
Brazil = df[Brazil]
print(Brazil.head(3))

SC = Brazil['State'] == 'Santa Catarina'
SC = Brazil[SC]
print(SC.head(3))
