import pandas as pd
import matplotlib.pyplot as plt

# Data frame (object that is the cols and rows)
# Series (only rows)
df = pd.read_csv('datasets/avocado.csv')

# Filter
# dataframe where column equals value
albany_df = df[df['region'] == "Albany"]

# Returns a new dataframe
albany_df = albany_df.set_index("Date")
# inplace=True -> does not require reassignment

albany_df.plot()
plt.show()
