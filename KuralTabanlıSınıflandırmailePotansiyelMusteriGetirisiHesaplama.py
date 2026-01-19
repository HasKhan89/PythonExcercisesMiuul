import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 500)
pd.set_option('display.float_format', '{:,.2f}'.format)

df = pd.read_csv("./DATA/persona.csv")
df.head(20)
df.shape
df.info()


#Gorev 2
df["SOURCE"].nunique()
df["SOURCE"].value_counts()

#Gorev 3
df["PRICE"].nunique()

#Gorev 4
df["PRICE"].value_counts()

#Gorev 5
df["COUNTRY"].value_counts()
df.groupby("COUNTRY")["PRICE"].count()

#Gorev 6
df.groupby("SOURCE")["PRICE"].sum()
df.groupby("COUNTRY").agg({"PRICE": "sum"})

#Gorev 7
df.groupby("SOURCE").value_counts()

#Gorev 8
df.groupby("COUNTRY").agg({"PRICE": "mean"})

#Gorev 9
df.groupby("SOURCE").agg({"PRICE": "mean"})

#Gorev 10
df.groupby(["COUNTRY", "SOURCE"]).agg({"PRICE": "mean"})

#Gorev 2.1
agg_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE" ]).agg({"PRICE": "mean"}, sort_values="PRICE" , ascending=False)

#Gorev 4.1
agg_df = agg_df.reset_index()
agg_df.head()
#Gorev 5

agg_df["AGE"].describe()
bins = [0, 18, 23, 30, 40, agg_df["AGE"].max()]
labels = ["0_18","19_23","24_30","31_40","41_" + str(agg_df["AGE"].max())]

agg_df["age_cat"] = pd.cut(df["AGE"], bins, labels=labels)
df.head(50).to_excel("./DATA/age_cat.xlsx",index=False)
agg_df.head()

agg_df["customers_level_based"] = agg_df[["COUNTRY","SOURCE","SEX","age_cat"]].agg(lambda x: "_" .join(x).upper(), axis=1)
#Gorev 7

agg_df["SEGMENT"]=pd.qcut(agg_df["PRICE"], 4, labels=["D", "C" , "B", "A"])
agg_df.head(30)
agg_df.groupby("SEGMENT").agg({"PRICE": ["mean" , "max" , "sum"]})

#Gorev 8
#agg_df.sort_values("ANDROID")
new_user = "TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]

new_user = "FRA_IOS_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]