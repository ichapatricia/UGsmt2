# #GUIDED
# import re

# def sensor_nohp(kalimat):
#     pattern = r"\d{11,13}"
#     no_hp = re.findall(pattern, kalimat)
#     hasil = ""
#     x = len(no_hp)
#     y = 0
#     if x != 0:
#         for i in no_hp:
#             if y < x-1:
#                 hasil = str(i)
#                 y = y + 1
#                 z = len(i)-7
#                 a = z + 4
#                 print(i[:4] + "x"*z + i[a:])
            
#             else:
#                 hasil = i
#                 z = len(i)-7
#                 a = z + 4
#                 return i[:4] + "x"*z + i[a:]
#     else:
#         return ""


# Validasi Kartu Kredit
'''
import re

def validasi_kartu_kredit(nomor_kartu):
    awal = "456"
    if len(nomor_kartu) == 16 and nomor_kartu[0] in awal and re.search(r"\d{16}", nomor_kartu):
        if re.search(r"8{4}", nomor_kartu):
            return "Valid Platinum"
        return  "Valid Reguler"
    return "Tidak valid"
'''

# Cek Password
'''
import re
def cek_password(password):
    re_password = re.search("\s",password)
    if re_password or len(password) < 6 or len(password) > 20:
        print("Password tidak valid")
    else:
        lower = re.search("[a-z]",password)
        upper = re.search("[A-Z]",password)
        angka = re.search("\d",password)
        symbol = re.search("\W",password)
        status = lower and upper and angka and symbol
        if status:
            print("Password kuat")
        else:
            print("Password lemah")
'''
#Sensor Komentar
'''
import re
def sensor_komentar(kalimat, terlarang, pengganti):
    a = terlarang
    b = pengganti
    c = kalimat
    for i in a:
        c = re.sub(i, b, c)
        print(c)
    return c
'''

# Cek Kode Pos
'''
def cek_kodepos(kodePos):
    ulang = 0
    sblh = True

    for i in range(len(kodePos)-2):
        if kodePos[i] != kodePos[i+1] and kodePos[i] == kodePos[i+2]:
            ulang += 1
    
    for i in kodePos:
        if i*4 in kodePos:
            sblh = False

    if int(kodePos) > 10000 and int(kodePos) < 99999:
        if ulang < 2:
            if sblh == True:
                print("Valid")
                return
    print("Tidak Valid")
'''
