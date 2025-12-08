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
lst[0]  #D
lst[10] #E

lst[0:4] #DATA
lst.pop(8)
lst

lst.append("1907")
lst
lst.insert(8,"N")
lst