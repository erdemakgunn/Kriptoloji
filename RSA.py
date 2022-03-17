import random
def Obeb(x, y):
    minimum = min(x, y)
    obeb = 1
    for i in range(2, minimum):
        if x % i == 0 and y % i == 0:
            obeb = i
    return obeb
##############################
def eUret(t):
    while True:
        rand = random.randrange(2, t)
        if Obeb(rand, t) == 1:
            e = rand
            break
    return e
##################################3
def dUret(t, e):
    for i in range(1, t):
        t1 = t * i + 1
        t1 = t1 / e
        if t1 % 2 == 0 or t1 % 2 == 1:
            break
    return int(t1)
###################################################
def ASCII(metin):
    ascii_degeri = []
    for karakter in metin:
        ascii_degeri.append(ord(karakter))
    return ascii_degeri
##########################################
def ustAlma(metin, t, e):
    ust = []
    for i in range(0, len(metin)):
        ust.append(ASCII(metin)[i] ** e)
    return ust
###########################################
def sifrele(metin, t, n):
    sMetin = []
    for i in range(0, len(metin)):
        sMetin.append(ustAlma(metin, t, e)[i] % n)
    return sMetin
#############################################
def deSifrele(sMetin, d, n):
    dMetin = []
    for i in range(0, len(sMetin)):
        dMetin.append(sMetin[i] ** d % n)

    return dMetin
#######################################
while True:
    p = int(input("p Sayısını Girin : "))
    if p > 1:
        for i in range(2, p):
            if (p % i) == 0:
                print("p Sayısı Asal Olmalıdır .")
                break
        else:
            break
while True:
    q = int(input("q Sayısını Girin : "))
    if q > 1:
        for i in range(2, q):
            if (q % i) == 0:
                print("q Sayısı Asal Olmalıdır .")
                break
        else:
            break
n = p * q
t = (p - 1) * (q - 1)
e = eUret(t)
d = dUret(t, e)
print("N Sayısı : ", n)
print("T Sayısı : ", t)
print("E Sayısı : ", e)
print("D Sayısı : ", d)
print("Public Anahtar = (", n, e, ")")
print("Private Anahtar = (", n, dUret(t, e), ")")
metin = input("Şifrelicek Metini Giriniz .")
print("Şifrelenicek Metnin ASCII Hali =", ASCII(metin))
sMetin = sifrele(metin, t, n)
print("Şifrelenen Metnin ASCII Hali = ", sMetin)
ascii = []
for i in range(0, len(metin)):
    ascii.append(chr(sifrele(metin, t, n)[i]))
print("Şifrelenmiş Metin = ", ascii)
asciiD = []
desifreliMetin=""
for i in range(0, len(sMetin)):
    asciiD.append(chr(deSifrele(sMetin, d, n)[i]))
print("Deşifrelenmiş Metnin ASCII Hali = ", deSifrele(sMetin, d, n))
for i in asciiD:
    desifreliMetin+=i
print("Deşifrelenmiş Metin = ", desifreliMetin)
