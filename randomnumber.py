import random

def tebak_angka():
    print("=====================================================")
    print("Selamat datang di permainan Tebak Angka!")
    print("Saya telah memilih sebuah angka antara 1 dan 100.")
    print("Tugas Anda adalah menebak angka tersebut.")
    print("=====================================================")

    angka_benar = random.randint(1, 100)
    tebakan = None
    jumlah_tebakan = 0
    
    while tebakan != angka_benar:
        try:
            tebakan = int(input("Masukkan tebakan Anda: "))
        except ValueError:
            print("Tolong masukkan angka yang valid.")
            continue
        
        jumlah_tebakan += 1
        
        if tebakan < angka_benar:
            print("Tebakan Anda terlalu rendah. Coba lagi!")
        elif tebakan > angka_benar:
            print("Tebakan Anda terlalu tinggi. Coba lagi!")
        else:
            print(f"Selamat! Anda berhasil menebak angka yang benar ({angka_benar}) setelah {jumlah_tebakan} tebakan.")
            break


tebak_angka()
