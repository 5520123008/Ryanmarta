print('selamat datang dibang BRI')
print('pilih option:')
print('1. chak saldo')
print('2. ambil saldo')
print('3. tabungan anda')
option=int(input('SILAHKAN PILIH OPTION :'))
Uang_kamu=300000
if option==1:
    print('uang saya berjumlah Rp.300.000')
elif option==2:
    print('uang saya berjumlah Rp.300.000,mau ambil berapa')
    print('Rp.200.000')
    print('Rp.100.000')
option2==int(input('option:'))
if option2==1:
    hasil2=uang_kamu-200000
    print('uangkamu sekarang berjumlah',hasil)
elif option2==2:
    hasil12=uang_kamu-100000
    print('uang kamu sekarang berjumlah',hasil)
else:
    print ('kata sandi anda salah,mohon masukan sandi anda lagi!')
if option==3:
    print('uang saya berjumlah Rp300.000 mau tabung berapa?')
    option3=int(input('masukan jumlah uang:'))
    hasil3=uang_kamu+option3
    print('jumlah uang kamu sekarang adalah',hasil)
else:
    print('pilihan anda salah,silahkan ulang kembali!!')
