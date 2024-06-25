#Liste
x=["btc","eth","xrp"]
type(x)

#Sözlük (dictionary)- değişitirilebilir, farklı veri türlerini tutabilir, kapsayıcıdır
x= {"name": "Merve", "Age":23, "No": [1,2,3]} # key: value
type(x)
x["Age"] # 23
x["No"][0] # 1
x["No"][1] # 2
x["No"][2] # 3

"Age" in x # True

x["Age"]= ["a", 5] # value değiştir
x # {'name': 'Merve', 'Age': ['a', 5], 'No': [1, 2, 3]}

x.keys() # dict_keys(['name', 'Age', 'No'])

x.values() #  dict_values(['Merve', ['a', 5], [1, 2, 3]])

x.items() # key value çiftleri dict_items([('name', 'Merve'), ('Age', ['a', 5]), ('No', [1, 2, 3])])  tuple formatında

x.update({"name": "mrv"}) # {'name': 'mrv', 'Age': ['a', 5], 'No': [1, 2, 3]}


#Tuple-demet listelerin değiştirilemeyen halidir parantezle ifade edilir, sıralıdır, kapsayıcıdır
x=("python","ml","ds")
type(x)

#Set-kümeler gibi, değiştirilebilir, sırasız eşsiz ve kapsayıcıdır
x=("python","ml","ds")
type(x)

set1=set([1,3,5])# bir liste üzerinden set oluşturuyoruz
set2=set([1,2,3])

set1.difference(set2)# set1 de olup set2 de olmayanlar 5
set1-set2 # 5
set2.difference(set1)# set2 de olup set1 de olmayanlar 2
set2- set1 # 2

set1.symmetric_difference(set2) # iki kümede de birbirlerinde olmayanlar {2, 5}
set2.symmetric_difference(set1) # iki kümede de birbirlerinde olmayanlar {2, 5}

set1.intersection(set2) # iki kümenin kesişimi {1, 3}
set2.intersection(set1) # iki kümenin kesişimi {1, 3}

set1 & set2 # {1, 3} kesişim
# NOT-Liste,tuple,set ve dictionary veri yapıları aynı zamanda Python Collections (Arrays) olarak geçmektedir.

set1.union(set2) # iki küme birleşimi {1, 2, 3, 5}
set2.union(set1) # iki küme birleşimi {1, 2, 3, 5}

set1.isdisjoint(set2) # iki kümenin kesişimi boş mu ? False
set2.isdisjoint(set1) # iki kümenin kesişimi boş mu ? False

set1=set([1,2,3,5])# bir liste üzerinden set oluşturuyoruz
set2=set([1,2,3])
set1.issubset(set2) # bir küme diğer kümenin alt kümesi mi? False
set2.issubset(set1) # bir küme diğer kümenin alt kümesi mi? True set1 alt küme

a=10.7
int(a) # 10

#String Methods

dir(str)

name = 'john AE'
len(name) #fonksiyon

"MERVE".lower() #method
"merve".upper()

hi="Hello ai"
hi.replace("l","p")

hi.split() #argüman girmezsen direkt boşluklara göre böler

hi.strip("i") #kırpar
hi.strip("H")

"abcde".capitalize() #ilk harfi büyütür

"abcde".startswith("a") #neyle başlayıp başlamadığını kontrol eder



# Liste (List) - değiştirilebilir, sıralıdır index işlemleri yapılabilir, kapsayıcıdır

notes=[1,2,3,4]
type(notes)

names = ["a", "b", 10, True, [1, 2, 3]]
type(names)

names[4] # [1, 2, 3]
names[4][1] # 2

names[0]=5
names # [5, 'b', 10, True, [1, 2, 3]]

names[0:3] # [5, 'b', 10]

# Liste metodları

dir(names)

len(names) #5

names.append(100) #listeye eleman ekler
names #[5, 'b', 10, True, [1, 2, 3], 100]

names.pop(0) #indexe göre eleman siler ['b', 10, True, [1, 2, 3], 100]
names.insert(0,"m") # indexe göre eleman ekler ['m', 'b', 10, True, [1, 2, 3], 100]

