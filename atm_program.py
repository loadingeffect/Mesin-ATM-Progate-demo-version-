import random
import datetime
from customer import Customer

atm=Customer(id)


while True:
    print(' ')
    print(' ')
    print('\nPT. Bank Progate Indonesia\n--------------------------')
    print(' ')
    print(' ')
    id=int(input("Masukkan Pin anda: "))
    Trial = 0
    
    
    while (id != int(atm.checkPin()) and Trial<3):
        id=int(input("Pin anda belum benar, coba lagi! : "))
        
        Trial+=1
        if Trial == 3:
            print('Error. Silahkan ambil kartu dan coba lagi..')
            exit()

    while (id==int(atm.checkPin())):
        print('')
        print('')
        print('PT. Bank Progate Indonesia\n--------------------------')
        print('')
        print('')
        print('\n1 - Cek Saldo \t2 - Penarikan \t3 - Setoran Tunai \t4 - Ganti Pin \t5 - Exit')
        Trial=1
        if Trial == 1:
            selectMenu=int(input('\nSilahkan pilih transaksi anda: '))
    
            if selectMenu == 1:               
                print('\nSaldo anda sekarang: Rp',str(atm.checkBalance())+'\n')
                break
            elif selectMenu == 2:
                print('')
                nominal = float(input('Masukkan jumlah Penarikan: '))
                verify_withdraw = input('Konfirmasi penarikan dengan nominal Rp. '+str(nominal)+'(y/n)? ')
                
                if verify_withdraw == 'y':
                    print('Saldo awal: Rp.',str(atm.checkBalance()),"")
                else:
                    break
                if nominal<=atm.checkBalance():
                    atm.WithdrawBalance(nominal)
                    print('Transaksi berhasil!')
                    print('Saldo terakhir: Rp. ',str(atm.checkBalance()),'')
                else:
                    print('Maaf saldo tidak cukup')
                    print('Silahkan tambahkan saldo dahulu')
                
            elif selectMenu == 3:
                print('')
                nominal = float(input('Masukkan nominal setor tunai: '))
                verify_deposit = input('Konfirmasi deposit dengan nominal Rp. '+str(nominal)+' (y/n)? ')
                
                if verify_deposit == 'y':
                    atm.depositBalance(nominal)                   
                    print('Saldo sekarang: Rp.',str(atm.checkBalance()),"")
                else:
                    break

            elif selectMenu == 4:
                print('')
                verify_pin=int(input('masukkan pin anda: '))
                while verify_pin != int(atm.checkPin()):
                    print('pin anda salah, silahkan ulang: ')
                updated_pin=int(input('silahkan masukkan pin baru:'))
                print('pin anda berhasil diganti!')
                verify_newpin = int(input('Coba masukkan pin baru anda: '))

                if verify_newpin == updated_pin:
                    print('pin baru sudah berhasil')
                else:
                    print('Pin anda salah!')
                    break

            elif selectMenu == 5:   
                print('')             
                print("Resi tercetak otomatis saat anda keluar. \n Harap simpan tanda terima ini \n sebagai bukti transaksi anda.")
                print("No. Rekord: ", random.randint(100000, 1000000))
                print("Tanggal: ", datetime.datetime.now())
                print("Saldo akhir: ", atm.checkBalance())
                print("Terima kasih telah menggunakan ATM Progate!")
                exit()
            else:
                print('')
                print('------Eror. Maaf, menu tidak tersedia-----')
                print('-----------dwi agus sulistiyanto-----------')
