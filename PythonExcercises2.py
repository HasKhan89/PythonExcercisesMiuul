#List Comperehension Exercises


#Gorev 1
import collections

import seaborn as sns
import pandas as pd
df = sns.load_dataset("car_crashes")
df.columns
df.info()

["NEW_" + col.upper()  if df[col].dtype != 0 else col.upper for col in df.columns ]

#Gorev 2

[col.upper() + " FLAG " if  "no" not in col else col.upper() for col in df.columns ]

#Gorev 3

#og_list = ["abbrev", "no_previous"]

og_list = ["abbrev", "no_previous"]
new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
new_df.head()


#Pandas Exercises
#Gorev 1

import seaborn as sns
df = sns.load_dataset("titanic")
df.head()
df.shape
#titanic veri setini eklemek

#Gorev 2

df["sex"].value_counts()
#titanic veri setindeki kadın ve erkek yolcu sayısı

#Gorev 3

df.nunique()
#her bir sutuna ait unique değerlerin sayısı

#Gorev 4
#pclass değişkeninin unique değerleri

df["pclass"].unique()

#Gorev 5
#pclass ve parch değişkenlerinin unique değerlerinin sayısı
df[["pclass", "parch" ]].nunique()

#Gorev 6
#embarked değişkenin  tipi nedir. Category olarak değiştirin tekrar kontrol edin
df["embarked"].dtype
df["embarked"] = df["embarked"].astype("category")
df["embarked"]
df.info()

#Gorev 7
#embarked değeri C olanların tüm bilgileri
df[df["embarked"] == "C"].head(10)

#Gorev 8
#emvarked değeri S olmayanların tüm bilgileri
df[df["embarked"] != "S"].head(10)


# SETTİNGS ARE SETTED
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
#SETTİNGS ARE SETTED

df[df["embarked"] != "S"]["embarked"].unique()
df[~(df["embarked"] == "S")]["embarked"].unique()


#Gorev 9
#Yası 30 dan küçük ve kadın olan yolcuların tüm bilgileri

df[(df["age"] < 30 ) & (df["sex"]=="female")].head()

#Gorev 10
# Fare i 500 den büyük veya yaşı 70 ten büuük uolcular.

df[(df["fare"] > 500 ) | (df["age"] > 70)].head()

#Gorev 11
#Ger bir değişkenin boş değerlerinin toplamı
df.isnull().sum()

#Gorev 12
# who değişkenini dataframe den çıkarınız
df.head()
df.drop("who", axis=1, inplace=True)
df.head()

#Gorev 13
#deck değişkenindeki boş değişkenleri en çok tekrar eden değeri mode ile doldur

type(df["deck"].mode())
df["deck"].mode()[0]
df["deck"].fillna(df["deck"].mode()[0])
df["deck"].isnull().sum()

#Gorev 14
# age değişkenin boş değerlerini age değişkenin medyanı ile doldur


df["age"].fillna(df["age"].median(),inplace=True)
df.isnull().sum()

#Gorev 15
# Survived değişkenin pclass ve cinsiyet değişkenleri kırılımında sum , count , mean değerlerini bulunuz.

df.groupby(["pclass", "sex"]).agg({"survived":["sum", "count" , "mean"]})


#Gorev 16
# 30 yaşın altında olanlar 1, 30' a eşit ve üstünde olanlar a 0 verecek bir fonksiyon yazın.Bu Fonksiyonla titanic veri setinde age_flag adında bir değişken oluşturunuz. (apply ve lamda yapılarını kullnınız)

def age_30(age):
    if age < 30:
        return 1
    else:
        return 0

df["age_flag"] = df["age"].apply(lambda x : age_30(x))

df["age_flag"] = df["age"].apply(lambda x : 1 if x >= 30 else 0)

#Gorev 17
#Tips veri setini tanımla

import seaborn as sns
df = sns.load_dataset("tips")
df.head()
df.shape

#Gorev 18
#time değişkenin (dinner,Launch) a göre total_bill değerlerinin toplamını min max ve ortalamasını bulun

df.groupby("time").agg({"total_bill":["sum", "min" ,"max", "mean"]})

#Gorev 19
#Günlere ve time göre total_bill değerinin toplamı min max ve ortalamasını bulun

df.head()
df.groupby( ["day" , "time"]).agg({"total_bill":["sum", "min" ,"max", "mean"]})


#Gorev 20
#Launch zamanında kadın müşterilerie ait total_bill tip değerlerinin day e göre toplamının min max ve ortalaması

df[(df["time"] == "Lunch") & (df["sex"] == "Female")].groupby("day").agg({"total_bill":["sum", "min" ,"max", "mean"],"tip":["sum", "min" ,"max", "mean"]})


#Gorev 21
#Size 3 ten küçük , total_bill 10 dan büyük olan siparişlerin ortalaması (loc kullanın)

df.loc[(df["size"] < 3) & (df["total_bill"] > 10 )  , "total_bill"].mean()

#Gorev 22
#total_bill_tip_sum adında yeni bir değişken oluşturunuz. Her müşterinin ödediği totalbill ve tip in toplamını versin

df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]
df.head()

#Gorev 23
#total_bill_tip_sum değişlenine göre büyükten küçüğe sıralayınız ilk 30 kişiyi yeni dataframe e atayınız.
new_df = df.sort_values(by=["total_bill_tip_sum"], ascending=False)[:30]
new_df.shape
new_df.head()