import pandas as pd
data = pd.read_csv('jaggi.csv')
data.dropna().to_csv('test.csv')