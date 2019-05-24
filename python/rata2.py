from __future__ import print_function

def main():
    #Jumlah bilangan yang akan dirata-ratakan
    n = int(raw_input("Masukan jumlah bilangan yang anda ingin rata-ratakan: "))
   
    #List data yang akan dirata-ratakan
    data = []
    jumlah = 0
 
    for i in range (0,n):
        temp = int(raw_input("Masukan nilai ke-%d: " % (i+1)))
        data.append(temp)
        
        #Menghitung jumlah data
        jumlah += data[i]
        
    #Menghitung rata-rata
    avg = jumlah/n

    #Menampilkan hasil
    print("Nilai rata-ratanya adalah: ")
    print("%s" % avg)
        
if __name__ == "__main__":
    main()
