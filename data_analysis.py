import pandas as pd
import seaborn

df = pd.read_csv("dht22-data-logger/arduino_data.csv")
print(df.head())