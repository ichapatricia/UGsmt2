#GAIDED 9
''' 
VINCENT
def cari_pasangan(list, target):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if (list[i] + list[j]) == target:
                print("{} dan {}" .format(i,j))
                return

    print("Tidak ada")

KA KAREND
def cari_pasangan(list,target):
    a = 0 
    b = 1
    total = 0
    hasil_idx = []
    for j in range(len(list)): #mengulang sebanyak isi didalam list
        for i in range(len(list)-1): #proses 1 kali iterasi
            total = list[a] + list[b]
            if total == target and a != b:
                hasil_idx.append(a)
                hasil_idx.append(b)
            else:
                b = b + 1
        b = 0
        a = a + 1

    if len(hasil_idx) == 0:
        print("Tidak ada")
 
else:
        x = []
        x.append(hasil_idx[0])
        x.append(hasil_idx[1])
        x.sort()
        print("%d dan %d" %(x[0],x[1]))

'''
#UNGAIDED
'''
RIKE VANEO
def total_tanpa_tigabelas(list):
    hasil = 0
    for i in list:
        if i == 13:
            break
        else:
            hasil = hasil + i
    return hasil
'''

'''
CHRISTO
def total_tanpa_tigabelas(list):
    total = 0
    a = len(list)
    b = 0
    for i in range(0,a):
        if list[b] == 13:
            break
        else:
            total = total + list[b]
            b = b + 1
    return(total)
'''
'''
#1. Tanpa angka tigabelas
def total_tanpa_tigabelas(list):
    hasil = 0

    for i in range(len(list)):
        if list[i] != 13:
            hasil += list[i]
        else:
            return hasil
    return hasil

#2. Filter duplikasi
def filter_duplikasi (list, batas):
    hasil = []
    
    for i in range(len(list)):
        if hasil.count(list[i]) < batas:
            hasil.append(list[i])
        else:
            continue

    print(hasil)
#3. Nol di depan
def nol_depan(list):
    hasil = []
    pindah = list.count(0)

    for i in range(pindah):
        hasil.append(0)

    for j in range(len(list)):
        if list[j] != 0:
            hasil.append(list[j])

    print(hasil)
#4. Simpan
def simpan(list_ukuran, kapasitas):
    beban = 0
    count = 0

    for i in range(len(list_ukuran)):
        if beban + list_ukuran[i] <= kapasitas:
            beban += list_ukuran[i]
            count += 1
        else:
            return count
    return count

''' 
