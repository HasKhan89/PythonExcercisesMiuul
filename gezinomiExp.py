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
pd.set_option('display.float_format', lambda x: '%.2f' % x)


df = pd.read_excel("./DATA/miuul_gezinomi.xlsx")
df.head()
df.tail()
df.shape
df.info()

#Gorev 2
#Kaç Unique Şehir frekansi nedir
df["SaleCityName"].nunique()
df["SaleCityName"].value_counts()

#Gorev 3
#Kaç unique Konsept var
df["ConceptName"].nunique()

#Gorev 4
# Hangi Concept'den kaçar tane satış gerçekleşmiştir
df["ConceptName"].value_counts()

#Gorev 5
#Şehirlere göre satışlardan ne kadar kazanılmış.
df.groupby("SaleCityName").agg({"Price": "sum"})

#Gorev 6
#ConceptTürüne Göre ne kadar kazanılmış
df.groupby("ConceptName").agg({"Price": "sum"})

#Gorev 7
#Şehirlere göre PRICE ortalamaları
df.groupby("SaleCityName").agg({"Price": "mean"})

#Gorev 8
#Conceptlere göre Price ortalamaları
df.groupby("ConceptName").agg({"Price": "mean"})

#Gorev 9
#Şehir - Concept kırılımında Price Ortalamaları

df.groupby(["SaleCityName","ConceptName"]).agg({"Price": "mean"})

#Gorev 2.1
bins = [-1, 7, 30, 90, df["SaleCheckInDayDiff"].max()]
labels = ["Last Minuters", "Potantial Planners", "Planners", "Early Bookers" ]

df["EB_Score"] = pd.cut(df["SaleCheckInDayDiff"], bins, labels=labels)
df.head(50).to_excel("./DATA/eb_scores.xlsx",index=False)
