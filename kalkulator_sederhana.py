import os

def tambah(a,b):
  tambah = int(a) + int(b);
  return tambah;
def kurang(a,b):
  kurang = int(a) - int(b);
  return kurang;
def bagi(a,b):
  bagi = int(a) / int(b);
  return bagi
def kali(a,b):
  kali = int(a) * int(b);
  return kali

print("------kalkulator Sederhana--------")
a = int(input("Masukan angka: "))
b = int(input("Muaskan angka: "))
print("1. tambah 2. kurang 3. bagi 4. kali 5. Batal ")
c = (input("Pilih 1-5 : "))
 
if c == '1':
   print(f"{a} + {b} = ", tambah(a,b))
   input("Tekan enter untuk reset")
   os.system("cls")

elif c == '2':
   print(f"{a} - {b} = ", kurang(a,b))
   os.system("cls")
elif c == '3':
   print(f"{a} / {b} = ", bagi(a,b))
   
   input("Tekan enter untuk Reset")
   os.system("cls")
elif c == '4':
   print (f"{a} * {b} = ", kali(a,b))
   input("Tekan enter untuk Reset")
   os.system("cls")
elif c == '5':
   print('Batal')
   os.system("cls")
else:
   print('operator tidak di temukan')
   input("Tekan enter untuk Reset")
   os.system("cls")



