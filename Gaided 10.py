#GAIDED#################################
'''
KALEB
def nilai_terendah(khs):
    list = []
    matkul = []
    for key in khs:
        list.append(khs[key])
    
    for key in khs:
        if khs[key] == min(list):
            matkul.append(key)
            
    return matkul
ARIKA
def nilai_terendah(nilai):
    matkul_terendah = []
    nilai_terendah = sorted(list(nilai.values()))
    
    for matkul,nilai in nilai.items():
        if nilai == nilai_terendah[0]:
            matkul_terendah.append(matkul)
            
    return sorted(matkul_terendah)
'''
#UNGAIDED###############################3
'''
1. cari_berdasar_operator(contacts, operator) 
VINCENT
import re
def cari_berdasar_operator(contacts, operator):
    op = {
    "telkomsel" : ["0812",  "0822"],
    "im3" : ["0856", "0857", "0858"],
    "three" : "0898",
    "xl" : ["0817", "0818"]
    }
    hasil = []

    for i, n in contacts.items():
        ang = n[:4]
        if str(ang) in op[operator]:
            hasil.append(i)

    return sorted(hasil)
EPAN
nama = []

    for pengguna,nomer in contacts.items():
        if operator == 'im3':
            if re.search('0856\w',nomer) or re.search('0858\w',nomer):
                nama.append(pengguna)
        elif operator == 'telkomsel':
            if re.search('0812\w',nomer) or re.search('0822\w',nomer):
                nama.append(pengguna)
        elif operator == 'three':
            if re.search('0898\w',nomer):
                nama.append(pengguna)
        elif operator == 'xl':
            if re.search('0817\w',nomer) or re.search('0818\w',nomer):
                nama.append(pengguna)
    
    return sorted(nama)
########################################################################################
2. kelilingSegitiga(koordinat)
KAREND
from math import sqrt
def kelilingSegitiga(koordinat):
    keys = []
    for j in test:
        keys.append(j)
    getA = koordinat.get(keys[0])
    getB = koordinat.get(keys[1])
    getC = koordinat.get(keys[2])
    
    AB = sqrt( (getB[0] - getA[0])**2 + (getB[1] - getA[1])**2 )
    AC = sqrt( (getC[0] - getA[0])**2 + (getC[1] - getA[1])**2 )
    BC = sqrt( (getC[0] - getB[0])**2 + (getC[1] - getB[1])**2 )

    result = AB + AC + BC
    segi = ""
    for i in koordinat:
        segi+=i
    print("Segitiga",segi,"memiliki keliling {:.4f}".format(result))
3. fungsi hitung_nilai_akhir(daftar_nilai,n)
CHRISTO
def hitung_nilai_akhir(daftar_nilai, n):
    a = list(sorted(daftar_nilai.keys()))
    b = []
    c = []
    for i in range(0, len(daftar_nilai)):
        b.append(a[i])
        d = sorted(daftar_nilai[a[i]])
        e = len(d)
        k = 0
        for j in range(1,n+1):
            k = k + d[e-j]
        f = k / n
        c.append(f)

    for j in range (0, len(daftar_nilai)):
        print( b[j],"{0:.6f}".format(c[j]))
4. sort by ASCII
VINCENT
hasil = 0
    hasil_a = dict()
    hasil_b = dict()

    for i in range(len(list_name)):
        for j in range(len(list_name[i])):
            huruf = list_name[i][j]
            hasil += ord(huruf)

        if hasil not in hasil_a:
            hasil_a[hasil] = [list_name[i]]
        else:
            hasil_a[hasil] += [list_name[i]]

        hasil = 0
    
    for n in sorted(hasil_a):
        if len(hasil_a[n]) > 1:
            hasil_b[n] = sorted(hasil_a[n])
        else:
            hasil_b[n] = hasil_a[n]
    
    

    return hasil_b
'''
