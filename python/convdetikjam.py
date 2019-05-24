from __future__ import print_function

def main():
    detik = int(raw_input("Masukan jumlah detik yang anda inginkan: "))
    
    hh = detik // 3600
    sisamenit = detik % 3600
    mm = sisamenit // 60
    ss = sisamenit % 60 
   

    print("%s jika dikonversikan ke dalam bentuk jam akan menjadi %s:%s:%s" %(detik,hh,mm,ss))

if __name__ == "__main__":
    main()
    

