###############################
# lambda, map, filter, reduce
###############################

# LAMBDA tek satırlık fonksiyondur

def summer(a,b):
    return a+b

summer(1,3)*9

new_sum = lambda a,b: a + b
new_sum(4,5)

# MAP bir listedeki elemanlara istediğin fonksiyonu uygulamayı sağlar

salaries = [1000,2000,3000,4000,5000]

def new_zam(x):
    return x * 20 / 100 + x

new_zam(50000)

# her bir elemana zam uygulama işlemi gerçekleştirmek istediğimizde
for salary in salaries:
    print(new_zam((salary))) # 1200.0 2400.0 3600.0 4800.0 6000.0

# map fonksiyonu ile bunu yapmak istediğimizde for döngüsünden kurtulmuş oluruz
list(map(new_zam,salaries)) # Out[13]: [1200.0, 2400.0, 3600.0, 4800.0, 6000.0]

# bu işlemi lambda ile beraber yapmak istediğimizde;
list(map(lambda x: x * 20 / 100 + x, salaries))

# FILTER bir fonksiyondan True dönen elementler için liste oluşturur

list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(filter(lambda x: x % 2 == 0, list_store)) # Out[16]: [2, 4, 6, 8, 10]

# REDUCE Dizinin her değeri için bir işlev yürütür ve sonunda diziyi tek bir değere düşürür

from functools import reduce

list_store = [1, 2, 3, 4]
reduce(lambda x, y: x + y, list_store)

