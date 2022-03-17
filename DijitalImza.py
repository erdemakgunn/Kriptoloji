from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
privateKey = RSA.generate(1024)
publicKey=privateKey.public_key()
print("Private Key : ","(",privateKey.d,",",privateKey.n,")")
print("Public Key : ","(",publicKey.e,",",publicKey.n,")")
mesaj = b'Bu Mesaj Imzalanmistir .'
hash = int.from_bytes(SHA256.new(mesaj).digest(), byteorder='big')
print("Hash : ",hash)
########################################
#Imzalama işlemi hash^d%n
imza = pow(hash, privateKey.d, privateKey.n)
print("Imza:", hex(imza))
deimza = pow(imza, publicKey.e, publicKey.n)
########################################
#Doğrulama işlemi
if deimza==hash:
    print("Imza Geçerlidir .")
else:
    print("Imza Geçerli Değildir .!")
###############################################################
print("--------------------------------------------------------")
print("Geçersiz İmza  ")
mesaj = b'Degistirilmis Mesaj'
hash = int.from_bytes(SHA256.new(mesaj).digest(), byteorder='big')
deimza = pow(imza, publicKey.e, publicKey.n)
print("Hash : ",hash)
if deimza==hash:
    print("Imza Geçerlidir .")
else:
    print("Imza Geçerli Değildir .!")