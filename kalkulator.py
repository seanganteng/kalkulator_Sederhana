#INPUT DARI USER/PENGGUNA
print('=====KALKULATOR SEDERHANA=====')
print('(+ , - , * , /)')
print('==============================')
print('+ = TAMBAH')
print("- = KURANG")
print("* = KALI")
print("/ = BAGI")
print('==============================')
simbol = (input('pilih operator :'))
angka1 = float (input('masukan angka ke 1 : '))
angka2 = float (input('masukan angka ke 2 : '))

#PROSES PERHITUNGAN

if simbol== '+':
  perhitungan = angka1 + angka2
  print(f"hasilnya {perhitungan}")
  
elif simbol=='-':
  perhitungan = angka1 - angka2 
  print(f"hasilnya {perhitungan}")

elif simbol=='*':
	perhitungan = angka1 * angka2 
	print(f"hasilnya {perhitungan}")
	
elif simbol=='/':
	perhitungan= angka1 / angka2
	print(f'hasilnya {perhitungan}')
	
#MR SMF

print('===========END================')