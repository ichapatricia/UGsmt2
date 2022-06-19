#1. Desimal To Binary
''''
CHRISTO
def desimaltobinary(angka):
    string= '01' 
    if angka < 2:
        return string[angka]
    else:
        return desimaltobinary(angka//2) + string[((angka)%2)]

def bagidesimal(angka):
    listIP = angka.split(".")
    hasil = ''
    for i in range(len(listIP)):
        if(i==(len(listIP)-1)):
            if(len(desimaltobinary(int(listIP[i])))<8):
                hasil += '0'*(8-len(desimaltobinary(int(listIP[i])))) + desimaltobinary(int(listIP[i]))
            else:
                hasil += desimaltobinary(int(listIP[i]))
        else:
            if(len(desimaltobinary(int(listIP[i])))<8):
                hasil += '0'*(8-len(desimaltobinary(int(listI
else:
            if(len(desimaltobinary(int(listIP[i])))<8):
                hasil += '0'*(8-len(desimaltobinary(int(listIP[i])))) + desimaltobinary(int(listIP[i]))+'.'
            else:
                hasil += desimaltobinary(int(listIP[i])) + "."
    return hasil
'''

#3 Faktorial Genap
'''
def faktorialgenap(jumlah, awal):
    if jumlah == 1 and awal == 0:
        return 2
    else:
        return faktorialgenap(jumlah-1, awal) * jumlah * 2

print(faktorialgenap(5,0))
print(faktorialgenap(2,0))
print(faktorialgenap(10,0))
'''
#4 Pasangan Huruf
'''
def pasanganHuruf(s, hitung=None):
    if hitung == None:
        hitung = 0

    # for i in range(len(s)-2):
    #     if s[i] != s[i+1] and s[i] == s[i+2]:
    #         hitung += 1

    if len(s) >= 3:
        if s[0] != s[1] and s[0] == s[2]:
            hitung += 1
        return pasanganHuruf(s[1:], hitung)
    return hitung
'''

#2 Huruf Jaga Jarak
'''
def hurufJagaJarak(string, hasil=None):
    if hasil == None:
        hasil = ""

    if len(string) > 1:
        if string[0] != string[1]:
            hasil += string[0]
        return hurufJagaJarak(string[1:], hasil)
        
    hasil += string[0]
    return hasil
'''
#4. Cari Angka
'''
def cariangka(n):
    angka=1000
    primes = []
    for i in range (2, angka+1):
        for j in range(2, i):
            if i%j == 0:
                    break
        else :
            primes.append(i)
            if len(primes) >= n:
                break
    jumlah = sum(primes)
            
    return(jumlah)
'''