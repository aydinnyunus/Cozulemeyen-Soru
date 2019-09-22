sayi = 2
toplam=0
while 1:
    for i in range(1,sayi-1):
        if(sayi%i == 0):
            toplam +=i         
        if(sayi == toplam+1):
            print("{} Hafifçe Artık Sayıdır.".format(sayi))
            break
        else:
            sayi = sayi + 1
