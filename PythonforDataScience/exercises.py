#########################################################
# Görev 1: Verilen değerlerin veri yapılarını inceleyiniz.
# Type() metodunu kullanınız
# x = 8
# y = 3.2
# z = 8j + 18
# a = "Hello World"
# b = True
# c = 23 22
# l = [1, 2, 3, 4]
# d = {"Name": "Jake", "Age": 27, "Adress": "Downtown"}
# t = ("Machine Learning", "Data Science")
# S = {"Python", "Machine Learning", "Data Science"}
#########################################################
x = 8
type(x) # int

y = 3.2
type(y) # float

z = 8j + 18
type(z) # complex

a = "Hello World"
type(a) # str

b = True
type(b) # bool

c = 23<22
type(c) # bool

l = [1, 2, 3, 4]
type(l) # list
# Sıralıdır
# Kapsayıcıdır
# Değiştirilebilir

d = {"Name": "Jake", "Age": 27, "Adress": "Downtown"}
type(d) # dict
# Değiştirilebilir
# Kapsayıcı
# Sırasız
# Key değerleri farklı olacak

t = ("Machine Learning", "Data Science")
type(t) # tuple
# Değiştirilemez
# Kapsayıcı
# Sıralı

S = {"Python", "Machine Learning", "Data Science"}
type(S) # set
# Değiştirilebilir
# Sırasız + Eşsiz
# Kapsayıcı

##################################################################################################################
# Görev 2:  Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız

# text = "The goal is to turn data into information, and information into insight."

# Beklenen çıktı:
# ['THE', 'GOAL', 'IS', 'TO', 'TURN', 'DATA', 'INTO', 'INFORMATION', 'AND', 'INFORMATION', 'INTO', 'INSIGHT']

# String metodlarını kullanınız.
##################################################################################################################
text = "The goal is to turn data into information, and information into insight."

new_text = text.upper().replace(","," ").replace("."," ").split()
print((new_text)) # ['THE', 'GOAL', 'IS', 'TO', 'TURN', 'DATA', 'INTO', 'INFORMATION', 'AND', 'INFORMATION', 'INTO', 'INSIGHT']


##################################################################################################################
# Görev 3: Verilen listeye aşağıdaki adımları uygulayınız.
# lst = ["D","A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]
# Adım 1: Verilen listenin eleman sayısına bakınız.
# Adım 2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
# Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
# Adım 4: Sekizinci indeksteki elemanı siliniz.
# Adım 5: Yeni bir eleman ekleyiniz.
# Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.
##################################################################################################################

lst = ["D","A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]
len(lst) # 11
lst[0] # 'D'
lst[10] # 'E'
new_lst = lst[0:4]
new_lst # ['D', 'A', 'T', 'A']

lst.pop(8)
lst # ['D', 'A', 'T', 'A', 'S', 'C', 'I', 'E', 'C', 'E']

lst.insert(10,"M")
lst # ['D', 'A', 'T', 'A', 'S', 'C', 'I', 'E', 'C', 'E', 'M']

lst.append(100) # append en sona ekler
lst # ['D', 'A', 'T', 'A', 'S', 'C', 'I', 'E', 'C', 'E', 'M', 100]

lst.insert(8,"N")
lst # ['D', 'A', 'T', 'A', 'S', 'C', 'I', 'E', 'N', 'C', 'E', 'M', 100]