###GUIDED###
'''
VINCENT

def inisial (daftar):
    k = []

    for i in daftar:
        if i[0] not in k:
            print(i)
            k.append(i[0])
        else:
            ke = k.count(i[0])
            print("{}{}".format(i,ke+1))
            k.append(i[0])

KAK YUSAK
def inisial(daftar):
    inisial_kosong = []
    for i in daftar :
        if i[0] not in inisial_kosong:
            print(i)
            inisial_kosong.append(i[0])
        else:
            inisial_kosong.append(i[0])
            print(i+str(inisial_kosong.count(i[0])))

daftar = (

             "Michael","Viny","Aurelio","Michael",

             "Felix","Kevin","Vincen","Vincen","Michael")

inisial(daftar)

KA NATHALIE
def inisial(daftar):
    inisial_kosong = []
    for i in daftar:
        if i[0] not in inisial_kosong:
            print(i)
            inisial_kosong.append(i[0])
        else:
            inisial_kosong.append(i[0])
            print(i + str(inisial_kosong.count(i[0])))
'''

#UNGAIDED
'''
1. hitung(dompet)
VINCENT
def hitung(dompet):
    k = dict()
    total = 0

    for i in dompet:
        if i not in k:
            k[i] = 1
        else:
            k[i] += 1

    for i in dompet:
        total += int(i[4:])
    for i,j in k.items():
        print("{} lembar senilai {}" .format(j,i))
    print(total)
 #buat test case--dompet = (

            "Rp. 100000", "Rp. 20000","Rp. 50000",

            "Rp. 50000","Rp. 10000","Rp. 5000",)

hitung(dompet)#
'''

'''
2. databuku(data)
DHEA
def databuku(data):
    for i in data:
        for j in i:
            if str(j).isdigit():
                tahun = j
            elif str(j).isupper():
                penulis = j
            else:
                judul = j
        print(judul)
        print(tahun)
        print(penulis)
'''

'''
3. bosan(daftar)
VINCENT
def bosan(daftar):
    hitung = -1

    for i in daftar:
        try:
            print(i[hitung],end="")
            hitung -= 1
        except IndexError:
            print("x",end="")
            hitung -= 1
daftar = ("Yusta", "Anbu", "Acen", "Dori")

EPAN
bosan(daftar):
indeks = -1
    hasil = ""
    for nama in daftar:
        try:
            hasil += nama[indeks]
        except:
            hasil += "x"
        indeks -= 1

    print(hasil)

bosan(daftar)
'''
'''
4. hapus(data,angka)
NEIKO
def hapus(data,angka):
    hasil = list()
    for i in data:
        if type(i) == tuple:
            h = []

            for j in i:
                if j != angka:
                    h.append(j)
            h1 = tuple(h)
            hasil.append(h1)

        elif i != angka:
            hasil.append(i)
    x = tuple(hasil)
    print(x)

def hapus(data, angka):
    isi = list()
    for dt in data: 
        isi.append(dt)
    for i in isi: 
        if type(i) == tuple:
            e = list(i)
            if angka in e:
                b = e.count(angka)
                for j in range(b):
                    e.remove(angka)
            e = tuple(e)
            isi[isi.index(i)] = e
    if angka in isi:
        c = isi.count(angka)
        for k in range(c):
            isi.remove(angka)
    hasil = tuple(isi)
    print(hasil)
'''