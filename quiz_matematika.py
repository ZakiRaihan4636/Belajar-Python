import random
import os

soal_ke = 1
soal_jumlah = 10
score = 0

while soal_ke <= soal_jumlah:
  os.system("cls")
  print(f"Soal ke : {soal_ke}/{soal_jumlah}")
  print(f"Score : {score}")
  print("Berapa Hasil dari penjumlahan berikut")
  a = random.randint(1,10)
  b = random.randint(1,10)
  c = a + b
  print(f"{a} + {b}")
  jawab = int(input(">> "))

  if jawab == c:
    print("Jawaban Benar")
    score += 10
  else:
    print(f"Jawaban Salah, {a} + {b} = {c}")
  input("Enter untuk soal lanjur >>")
  soal_ke += 1

