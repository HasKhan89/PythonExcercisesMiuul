# Görev 1 #
#type() metodu ile tip belirleme
#int
x = 8
type(x)

#float
y = 3.2
type(y)

#complex
z = 8j + 18
type(z)

#str
a = "Hello World"
type(a)

#Bool
b = True
type(b)

#Bool
c = 23 < 22
type(c)

#list
l = [1,2,3,4]
type(l)

#dict
d = {"Name": "Jake",
    "Age":27,
    "Address":"Downtown"}
type(d)

#tuple
t = ("Machine Learning","Data Science")
type(t)

#set
s = {"Python", "Machine Learning", "Data Science"}
type(s)

# Görev 2 #
# Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz,kelime kelime ayırınız.#


text = "The goal is to turn data into information, and information into insight."

print(text.upper().split(), sep= ","  , end=" ")

# Görev 3

lst = ["D","A","T","A","S","C","I","E","N","C","E"]

# listenin eleman sayısı
len(lst) #11
lst[0]
lst[10]

data_list  = lst[0:4]
data_list
#DATA
lst.pop(8)


lst.append("1907")

lst.insert(8,"N")

lst

# Görev 4

my_dictionary = {'Christian' : ["America" , 18],
        'Daisy' : ["England" , 12],
        'Antonio' : ["Spain" , 22],
        'Dante' : ["Italy" , 25]}

my_dictionary.keys() # KEY Değerleri
my_dictionary.values() # value değerleri

my_dictionary['Daisy'][1] = 13 # 12 Değeri 13 olarak değiştirildi.

""" 
dict 

{'Christian': ['America', 18],
 'Daisy': ['England', 13],
 'Antonio': ['Spain', 22],
 'Dante': ['Italy', 25]}"""

my_dictionary.update({'Ahmet' : ['Türkiye', 24]}) # Key Value Değeri Girmek



my_dictionary.pop('Antonio')



#Görev 5

l=[2,13,18,93,22]

def func(list):
    cift_list = []
    tek_list = []
    for i in list:
        if i% 2 == 0:
            cift_list.append(i)
        else:
            tek_list.append(i)
    return cift_list, tek_list

cift, tek = func(l)
cift, tek


# Görev 6
ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

for i,x in enumerate(ogrenciler):
    if i<3:
        i += 1
        print("Mühendislik Fakültesi" ,i, ". öğrenci: ", x)
    else:
        i -= 2
        print("Tıp Fakültesi",i," . öğrenci: ", x)



# Görev 7
ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi=[3,4,2,4]
kontenjan = [30,75,150,25]


for ders_kodu,kredi,kontenjan in zip(ders_kodu,kredi,kontenjan):
    print(f"Kredisi {kredi} olan {ders_kodu} kodlu dersin kontenjanı {kontenjan} kişidir.")

# Görev 8

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lamda", "python", "miuul"])

def kume(set1, set2):
    if set1.issuperset(set2):
        print(set1.intersection(set2))
    else:
        print(set2.difference(set1))

kume(kume1,kume2)
kume(kume2,kume1)

















