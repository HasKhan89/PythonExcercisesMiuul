#Gorev 1
import collections

import seaborn as sns
import pandas as pd
df = sns.load_dataset("car_crashes")
df.columns
df.info()

["NEW_" + col.upper()  if df[col].dtype != 0 else col.upper for col in df.columns ]