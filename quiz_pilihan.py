import random
import os

# Quiz matematika
def quiz():
  soal_ke = 1
  soal_jumlah = 3
  score = 0


  while soal_ke <= soal_jumlah:
    os.system("cls")
    print(f"Soal ke : {soal_ke} dari {soal_jumlah} pertanyaan")
    print(f"score = {score}")
    a = random.randint(1,2)
    b = random.randint(1,2)
    c = a + b

    print(f"Hasil dari {a} + {b}")
    jawab = int(input(">> "))
    cek_pertanyaan(jawab,c)
    print("--------------")
    soal_ke += 1
def cek_pertanyaan(jawab,c):
  if jawab == c:
    print("Jawaban Benar")
    input("Enter untuk soal lanjut >>")
    score += 10
  else:
    input("Enter untuk soal lanjut >>")
    





quiz()