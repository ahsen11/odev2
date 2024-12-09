# 1) Bir aracın yakıt tipine göre (benzin,dizel,lpg) belirtilen bir mesafede ne kadar yakıt masrafı olduğunu hesaplayan uygulamayı yapınız.
# benzin    : 39.35
# dizel     : 41.71
# lpg       : 20.28

yakıtTipi=input("hangi yakıt tipini kullandınız? : ")
mesafe=float(input("ne kadar yol aldınız? :"))

benzinFiyat=39.35
dizelFiyat=41.71
lpgFiyat=20.28

print("yakıt masrafınız:")

if(yakıtTipi=="benzin"):
    print(mesafe*benzinFiyat)
    
elif(yakıtTipi=="dizel"):
    print(mesafe*dizelFiyat)
    
elif(yakıtTipi=="lpg"):
    print(mesafe*lpgFiyat)
    
else:
    print("Geçerli bir yakıt tipi giriniz.")

    # 2) Bir öğrencinin 2 vize 1 final notunu alarak ortalama hesaplayınız ve hesaplanan ortalamaya göre not aralığına karşılık gelen harf notunu yazdırınız.
#    90-100 => AA
#    80-89  => BA
#    70-79  => BB
#    60-69  => CB
#    50-59  => CC
#    40-49  => DC

vize1=float(input("1. vize notunuzu giriniz:"))
vize2=float(input("2. vize notunuzu giriniz:"))
final=float(input("final notunuzu giriniz:"))

notOrtalaması=(vize1*0.3+vize2*0.3+final*0.4)

print("harf notunuz= ")

if(100>=notOrtalaması>90):
    print("AA")

elif(90>=notOrtalaması>80):
    print("BA")

elif(80>=notOrtalaması>70):
    print("BB")

elif(70>=notOrtalaması>60):
    print("CB")

elif(60>=notOrtalaması>50):
    print("CC")

elif(50>=notOrtalaması>40):
    print("DC")

else:
    print("başarısız")