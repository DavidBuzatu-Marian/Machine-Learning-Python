import pandas as pd
import quandl
import math

df = quandl.get('WIKI/GOOGL')
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
# High to low percentage
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
# Daily percentage
df['Change_PCT'] = (df['Adj. Close'] - df['Adj. Open']) / \
    df['Adj. Open'] * 100.0
# Redefine data we need (features)
df = df[['Adj. Close', 'HL_PCT', 'Change_PCT', 'Adj. Volume']]

# Define the column we want to forecast
forecast_col = 'Adj. Close'

# Fill empty columns
df.fillna(-99999, inplace=True)

# Predict the following 10 days
forecast_out = math.ceil(0.01 * len(df))

# Add label.
df['label'] = df[forecast_col].shift(-forecast_out)
print(df.head())
