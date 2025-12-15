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
"""
l=[2,13,18,93,22]
def fun(..):
    for i in l:
        if i%2 != 0:
            print(i)
        else:
            print(i)
    return .. 

even_list, odd_list = func(l)


"""
























