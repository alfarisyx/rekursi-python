import sys #import modul sys 

sys.setrecursionlimit(10000) # untuk membatasi dan menambah , karena limit recursion asli 966

def a(spam): # fungsi untuk menghitung nilai a
    if spam == 0 : # jika spam sama dengan 0 maka return 0
        return  
    a(spam - 1) # jika spam tidak sama dengan 0 maka akan menjalankan fungsi a
    print("hallo semuanya", spam) # fungsi a akan mencetak hallo semuanya dan nilai spam yang diinputkan
    
b = int(input("spam berapa kali:")) # inputan dari user untuk mengetahui berapa kali akan dijalankan fungsi a

a(b) # memanggil fungsi a dengan inputan dari user


#membuat faktorial dengan rekursi  

print("\n membuat faktorial dengan rekursi" )
def faktorial(n): # fungsi untuk menghitung faktorial
    if n == 0: # jika n sama dengan 0 maka return 1
        return 1
    else: # jika n tidak sama dengan 0
        return n * faktorial(n-1) # maka akan menjalankan fungsi faktorial
   
n = int(input("masukkan angka:")) # inputan dari user untuk mengetahui berapa kali akan dijalankan fungsi a
b = faktorial(n) # memanggil fungsi a dengan inputan dari user
print("hasil faktorial dari", n, "adalah", b)
