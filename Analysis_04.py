import os
import subprocess
import stat
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

sns.set(style="blue")


# absolute path till parent folder
abs_path = os.getcwd()
path_array = abs_path.split("/")
path_array = path_array[: len(path_array) - 1]
homefolder_path = ""
for i in path_array[1:]:
    homefolder_path = homefolder_path + "/" + i


# path to clean data
clean_data_path = homefolder_path + "cleaned_autos.csv"

# reading csv into raw dataframe
df = pd.read_csv(clean_data_path, encoding="latin-1")


trial = pd.DataFrame()
for b in list(df["brand"].unique()):
    for v in list(df["vehicleType"].unique()):
        z = df[(df["brand"] == b) & (df["vehicleType"] == v)]["price"].mean()
        trial = trial.append(
            pd.DataFrame({"brand": b, "vehicleType": v, "avgPrice": z}, index=[0])
        )
trial = trial.reset_index()
del trial["index"]
trial["avgPrice"].fillna(0, inplace=True)
trial["avgPrice"].isnull().value_counts()
trial["avgPrice"] = trial["avgPrice"].astype(int)
print(trial.head(5))


# ## Average price of a vehicle by brand as well as vehicle type


# HeatMap tp show average prices of vehicles by brand and type together
tri = trial.pivot("brand", "vehicleType", "avgPrice")
fig, ax = plt.subplots(figsize=(15, 20))
sns.heatmap(tri, linewidths=1, cmap="YlGnBu", annot=True, ax=ax, fmt="d")
ax.set_title(
    "Average price of vehicles by vehicle type and brand", fontdict={"size": 18}
)
plt.show()


fig.savefig((abs_path + "/heatmap-price-brand-vehicleType.png"))

