import RSA
# hexadecimalden binarye çevirme
def hex2bin(s):
    mp = {'0': "0000",
          '1': "0001",
          '2': "0010",
          '3': "0011",
          '4': "0100",
          '5': "0101",
          '6': "0110",
          '7': "0111",
          '8': "1000",
          '9': "1001",
          'A': "1010",
          'a': "1010",
          'B': "1011",
          'C': "1100",
          'D': "1101",
          'E': "1110",
          'F': "1111"}
    bin = ""
    for i in range(len(s)):
        bin = bin + mp[s[i]]
    return bin
# binaryden hexadecimale çevirme
def bin2hex(s):
    mp = {"0000": '0',
          "0001": '1',
          "0010": '2',
          "0011": '3',
          "0100": '4',
          "0101": '5',
          "0110": '6',
          "0111": '7',
          "1000": '8',
          "1001": '9',
          "1010": 'A',
          "1011": 'B',
          "1100": 'C',
          "1101": 'D',
          "1110": 'E',
          "1111": 'F'}
    hex = ""
    for i in range(0, len(s), 4):
        ch = ""
        ch = ch + s[i]
        ch = ch + s[i + 1]
        ch = ch + s[i + 2]
        ch = ch + s[i + 3]
        hex = hex + mp[ch]

    return hex
# binaryden decimale çevirme
def bin2dec(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal
# decimalden binarye çevirme
def dec2bin(num):
    res = bin(num).replace("0b", "")
    if (len(res) % 4 != 0):
        div = len(res) / 4
        div = int(div)
        counter = (4 * (div + 1)) - len(res)
        for i in range(0, counter):
            res = '0' + res
    return res
# permüte yapma işlemi
def permute(k, dizi, n):
    permutasyon = ""
    for i in range(0, n):
        permutasyon = permutasyon + k[dizi[i] - 1]
    return permutasyon
# sola kaydırma işlemi
def sola_kaydir(k, nth_shifts):
    s = ""
    for i in range(nth_shifts):
        for j in range(1, len(k)):  # shift_table tablosuna göre nekadar kaydırıcağını gösterir örneğin
            # 1 ise en baştaki elemanı en sona atar 2 ise en baştaki 2 elemanı sona atar
            s = s + k[j]
        s = s + k[0]
        k = s
        s = ""
    return k
# xorlama işlemi
def xor(a, b):
    ans = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            ans = ans + "0"
        else:
            ans = ans + "1"
    return ans
# ilk permütasyon tablosu
ilk_perm = [58, 50, 42, 34, 26, 18, 10, 2,
            60, 52, 44, 36, 28, 20, 12, 4,
            62, 54, 46, 38, 30, 22, 14, 6,
            64, 56, 48, 40, 32, 24, 16, 8,
            57, 49, 41, 33, 25, 17, 9, 1,
            59, 51, 43, 35, 27, 19, 11, 3,
            61, 53, 45, 37, 29, 21, 13, 5,
            63, 55, 47, 39, 31, 23, 15, 7]
# Genişletme Tablosu
genisletme_tablosu = [32, 1, 2, 3, 4, 5, 4, 5,
                      6, 7, 8, 9, 8, 9, 10, 11,
                      12, 13, 12, 13, 14, 15, 16, 17,
                      16, 17, 18, 19, 20, 21, 20, 21,
                      22, 23, 24, 25, 24, 25, 26, 27,
                      28, 29, 28, 29, 30, 31, 32, 1]
# Permütasyon tablosu
per = [16, 7, 20, 21,
       29, 12, 28, 17,
       1, 15, 23, 26,
       5, 18, 31, 10,
       2, 8, 24, 14,
       32, 27, 3, 9,
       19, 13, 30, 6,
       22, 11, 4, 25]
# Sbox tablosu
sbox = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
         [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
         [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
         [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

        [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
         [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
         [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
         [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

        [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
         [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
         [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
         [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

        [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
         [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
         [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
         [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

        [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
         [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
         [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
         [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

        [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
         [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
         [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
         [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

        [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
         [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
         [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
         [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

        [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
         [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
         [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
         [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]
# final permütasyon tablosu
final_perm = [40, 8, 48, 16, 56, 24, 64, 32,
              39, 7, 47, 15, 55, 23, 63, 31,
              38, 6, 46, 14, 54, 22, 62, 30,
              37, 5, 45, 13, 53, 21, 61, 29,
              36, 4, 44, 12, 52, 20, 60, 28,
              35, 3, 43, 11, 51, 19, 59, 27,
              34, 2, 42, 10, 50, 18, 58, 26,
              33, 1, 41, 9, 49, 17, 57, 25]


# Şifrele
def sifrele(metin, anahtar_binary, anahtar_hex):
    metin = hex2bin(metin)
    # Ilk Permutasyon işlemi
    metin = permute(metin, ilk_perm, 64)  # 64 bitlik mesaj başlangıç permütasyonuna göre permute edilir
    print("İlk Permütasyon işleminden sonra :", bin2hex(metin))
    # İkiye Bölme
    sol = metin[0:32]
    sag = metin[32:64]
    for i in range(0, 16):
        #  Genişletme Tablosundan 32 bitlik veriyi 48 bite genişletme
        sag_genisletme = permute(sag, genisletme_tablosu, 48)
        # 48 bitlik sag parça ile 48 bitlik anahtarımız ile xor işlemi
        xor_x = xor(sag_genisletme, anahtar_binary[i])
        # 8 parçaya ayırdığımız 48 bitlik veriyi satır sütün değerini hesaplayarak sbox tablosuna göre değiştirme
        sbox_deger = ""
        for j in range(0, 8):
            sutun = bin2dec(int(xor_x[j * 6] + xor_x[j * 6 + 5]))
            satir = bin2dec(int(xor_x[j * 6 + 1] + xor_x[j * 6 + 2] + xor_x[j * 6 + 3] + xor_x[j * 6 + 4]))
            deger = sbox[j][sutun][satir]
            sbox_deger = sbox_deger + dec2bin(deger)
        # 32 bitlik veri permütasyon tablosundan geçirilir
        sbox_deger = permute(sbox_deger, per, 32)
        # sol parça ile xor işlemine tabi tutulur
        sonuc = xor(sol, sbox_deger)
        sol = sonuc
        # sol ve sağ parçalarımız yer değiştirir
        if (i != 15):
            sol, sag = sag, sol
        print("Adım ", i + 1, " ", bin2hex(sol), " ", bin2hex(sag), " ", anahtar_hex[i])
    # Sol ve Sağ Parça Birleştirilir
    kombinasyon = sol + sag
    # Son olarak final permütasyonundan geçirilip şifreli metin elde edilir
    sifreli_metin = permute(kombinasyon, final_perm, 64)
    return sifreli_metin
metin="0123456789ABCDEF"
#RSA'dan anahtarı alma
anahtar=((RSA.desifreliMetin).encode('utf-8')).hex().upper()
# Anahtar Oluşturma
anahtar = hex2bin(anahtar)
# Parity bit tablosu
key_parity = [57, 49, 41, 33, 25, 17, 9,
              1, 58, 50, 42, 34, 26, 18,
              10, 2, 59, 51, 43, 35, 27,
              19, 11, 3, 60, 52, 44, 36,
              63, 55, 47, 39, 31, 23, 15,
              7, 62, 54, 46, 38, 30, 22,
              14, 6, 61, 53, 45, 37, 29,
              21, 13, 5, 28, 20, 12, 4]
# parity bit tablosunu kullanarak 64 bitlik anahtar parity bit tablosuna göre permute edilip 56  bite sıkıştırılır
anahtar = permute(anahtar, key_parity,56)
# kaç bit kaydırıcağımızı gösterir
kaydirma_tablosu = [1, 1, 2, 2,
                    2, 2, 2, 2,
                    1, 2, 2, 2,
                    2, 2, 2, 1]

# 56 bitlik anahtar anahtar sıkıştırma tablosuna göre permute edilip 48 bite sıkıştırılır
anahtar_s = [14, 17, 11, 24, 1, 5,
             3, 28, 15, 6, 21, 10,
             23, 19, 12, 4, 26, 8,
             16, 7, 27, 20, 13, 2,
             41, 52, 31, 37, 47, 55,
             30, 40, 51, 45, 33, 48,
             44, 49, 39, 56, 34, 53,
             46, 42, 50, 36, 29, 32]

# İkiye Bölme
sol = anahtar[0:28]  # Sol degeri key'in
sag = anahtar[28:56] # Sağ degeri key'in
anahtar_binary = []
anahtar_hex = []
for i in range(0, 16):
    # kaydırma tablosuna göre sola kaydırma işlemleri
    sol = sola_kaydir(sol, kaydirma_tablosu[i])
    sag = sola_kaydir(sag, kaydirma_tablosu[i])
    # sol ve sağ parçayı birleştirme işlemi
    kombinasyon = sol + sag
    # anahtar sıkıştırma tablosu kullanılarak 56 bitlik anahtar 48 bite sıkıştırılır
    adim_anahtar = permute(kombinasyon, anahtar_s, 48)
    anahtar_binary.append(adim_anahtar)
    anahtar_hex.append(bin2hex(adim_anahtar))  # enson binary bulduğumuz keyi hexadesimale çevirdik
print("Şifrele")
sifreli_metin = bin2hex(sifrele(metin, anahtar_binary, anahtar_hex))
print("Şifreli Metin : ", sifreli_metin)
print("Şifre Çözme")
anahtar_binary_t = anahtar_binary[::-1]
anahtar_hex_t = anahtar_hex[::-1]
metin = bin2hex(sifrele(sifreli_metin, anahtar_binary_t, anahtar_hex_t))
print("Metin : ", metin)