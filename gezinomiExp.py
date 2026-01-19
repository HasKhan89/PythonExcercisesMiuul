#Gorev 1


#Libraries are imported
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Settings are done.
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 500)


df = pd.read_csv("./DATA/miuul_gezinomi.xlsx")
df.head()
df.shape
df.info()
