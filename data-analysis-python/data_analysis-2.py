import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datasets/avocado.csv")
df["Date"] = pd.to_datetime(df["Date"])
albany_df = df[df["region"] == "Albany"]
albany_df.set_index("Date", inplace=True)


# Average map
albany_df.sort_index(inplace=True)
# albany_df['AveragePrice'].rolling(25).mean().plot()
# plt.show()

albany_df['price25ma'] = albany_df['AveragePrice'].rolling(25).mean()
print(albany_df.head(3))

# Drop any row that that NaN
# albany_df.dropna()
