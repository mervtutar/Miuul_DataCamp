
students = ["Ayse", "Ali", "Merve", "Zeliha"]

for student in students:
    print (student)

# index default olarak 0 dan başlar, istersek değiştirebiliriz

for index, student in enumerate(students): # enumarate(students, 1) index 1'den başlar
    print(index, student)


# çift index ve tek indextekileri ayırmak istersek

A = []
B = []

for index, student in enumerate(students):
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)

print(A)
print(B)

#################
# UYGULAMA
#################
# divide_students fonksiyonu yazınız.
# Çift indexte yer alan öğrencileri bir listeye alınız.
# Tek indexte yer alan öğrencileri başka bir listeye alınız.
# Fakat bu iki liste tek bir liste olarak return olsun.

students = ["Ayse", "Ali", "Merve", "Zeliha"]

def divide_students(students):
    groups = [[],[]]
    for index,student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else :
            groups[1].append(student)
    print(groups)
    return groups

st = divide_students(students)
st[0] # çift index
st[1] # tek index

#####################
# alternating fonksiyonunun enumerate ile yazılması (enumerate dışında len ve range fonksiyonları kullanılarak yapılabilir
# çift indexleri büyük, tek indexleri küçük harfle yaz
#####################

def alternating_enumerate(string):
    new_string = ""
    for i, letter in enumerate(string):
        if i % 2 == 0:
            new_string += letter.upper()
        else :
            new_string += letter.lower()
    print(new_string)

alternating_enumerate("hi i am merve") # output Hi i aM MeRvE
