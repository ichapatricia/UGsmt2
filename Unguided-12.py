#Gaided

# def hitungHonorAsisten(data,honor):
#     asisten = []
#     honorasisten = dict()

#     for i in data.items():
#         asisten += i[1]
#     asistenuniq = list(set(asisten))
#     asistenuniq.sort()
#     for i in asistenuniq:
#         if i not in honorasisten.keys():
#             honorasisten[i] = honor*asisten.count(i)
        
#     return honorasisten



#1. Kata Unik Spesial
'''
# BIMA
def kata_unik_spesial(kalimat1, kalimat2):
    hasil = set()
    k1 = kalimat1.lower().split()
    k2 = kalimat2.lower().split()

    for i in k1:
        k2.append(i)

    for j in k2:
        if j not in hasil:
            if k2.count(j) == 2:
                hasil.add(j + j)
            else:
                hasil.add(j)
        

    return hasil
'''
#2. Euclidien Calculation
'''
# BIMA
def euclidienCalculation(dict1, dict2):
    m = set(dict1) | set(dict2)
    n = set(dict1) & set(dict2)
    total = 0
    for i in n:
        a = (dict1[i] - dict2[i])**2
        total += a
    total = total**0.5
    total = total /4
    return total
'''
#3. cek Karakter
'''
#BIMA
def cekKarakter(kalimat):
    import string
 
    huruf=string.ascii_lowercase
    huruf_=list(str(huruf))
    kalimat=kalimat.replace(" ","")
    kalimat.lower()
    kalimat_=list(str(kalimat))
    
    if len(set((huruf_)))==len(set(kalimat_)):
        print("Kalimat tersebut memiliki semua huruf")
    else:
        print("Kalimat tersebut tidak memiliki semua huruf")
cekKarakter(kalimat="the quick brown fox jumps over the lazy dog")
'''
#4. Daftar Tidak Sama
'''
#BIMA
def daftar_tidak_sama(angka1,angka2,batas):
    himpunan1=[]
    himpunan2=[]
    x=angka1
    y=angka2
    for i in range(angka1,batas,angka1):
        himpunan1+=[angka1]
        angka1+=x
    for i in range(angka2,batas,angka2):
        himpunan2+=[angka2]
        angka2+=y

    himpunan_gabungan=set(himpunan1)|set(himpunan2)
    hasil=himpunan_gabungan-(set(himpunan1)&set(himpunan2))
    print(len(set(hasil)))
'''
#5. Daftar Tidak Sama
'''
BIMA
def daftar_tidak_sama(angka1,angka2,batas):
    himpunan1=[]
    himpunan2=[]
    angka1_jumlah=angka1
    for i in range(angka1,batas+1,angka1):
        himpunan1+=[angka1]
    print(himpunan1)
'''
#6. Cek Kekurangan
'''
BIMA
def cek_kekurangan(krs1,krs2):
    krs=set(krs1)-set(set(krs1)&set(krs2))
    print(len(krs))

VINCENT
def cek_kekurangan(krs1, krs2):
    x = set(krs1)
    b = set(krs2)
    a = x - b
    print(len(a))
        

krs1 = ['alpro', 'strukdat', 'pbo', 'ppkn', 'toefl', 'prakalpro', 'skripsi', 'kkn', 'statistik', 'ai', 'jarkom', 'tekwan']
krs2 = ['alpro', 'jarkom', 'pbo', 'strukdat', 'statistik', 'hamdem', 'kcp']
cek_kekurangan(krs1, krs2)
'''
