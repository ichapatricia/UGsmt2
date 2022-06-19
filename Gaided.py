def bagidesimal(angka):
    tempat = [] 
    a = angka.split(".")
    tempat = tempat + a
    x = 0
    for j in range(len(tempat)): 
        if x < len(tempat) - 1:
            c = int(tempat[x])
            print('%s.'%(decimal_to_binary(c)),end='')
            x = x+1
        else:
            c = int(tempat[x])
            return(decimal_to_binary(c))

def decimal_to_binary(angka):
    hasil = []
    while(angka != 0):
        x = angka % 2
        hasil.append(str(x))
        angka = angka // 2

    hasil.reverse()
    str_hasil = "".join(hasil)

    if len(str_hasil) == 8:
        next
    else:
        z = 8 - len(str_hasil)
        str_hasil = "0" *z + str_hasil
    return (str_hasil)

bagidesimal("192.166.1.1")
bagidesimal("192.168.1.2")
