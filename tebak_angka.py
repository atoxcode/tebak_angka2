import random


#untuk tebakan komputer yang ditujukan ke manusia
def tebak(x):
    angka_acak = random.randint(1, x)
    tebak = 0
    while tebak != angka_acak:
        tebak = int(input(f'Coba tebak sebuah angka antara 1 sampai dengan {x}: '))
        if tebak < angka_acak:
            print('Maaf, coba lagi. Angka Anda terlalu rendah')
        elif tebak > angka_acak:
            print('Maaf, coba lagi. Angka Anda terlalu tinggi')

    print(f'Horee.. Selamat. Anda berhasil menebak angka {angka_acak} dengan benar')


#untuk tebakan manusia yang ditujukan kepada komputer
def komputer_tebak(x):
    rendah = 1
    tinggi = x
    umpan_balik = ''
    while umpan_balik != 'b':
        if rendah != tinggi:
            tebak = random.randint(rendah, tinggi)
        else:
            tebak = rendah #boleh juga tinggi karena rendah = tinggi
        umpan_balik = input(f'Apakah {tebak} terlalu tinggi (T), terlalu rendah (R), atau sudah benar (B) ?')
        if umpan_balik == 't':
            tinggi = tebak - 1
        elif umpan_balik == 'r':
            rendah = tebak + 1

print(f'Horeeee... Tebakan Anda (komputer) pada angka {tebak} adalah benar')

tebak(10)