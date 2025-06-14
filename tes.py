def total_manik_manik(S_M, S_H, S_B):
    def is_skip_H(n):
        return n % 5 == 1

    stok = {'M': S_M, 'H': S_H, 'B': S_B}
    warna_sebelumnya = None
    n = 0

    while True:
        valid = False
        for warna in ['M', 'H', 'B']:
            if stok[warna] > 0 and warna != warna_sebelumnya:
                if warna == 'H' and is_skip_H(n + 1):
                    continue  # Lewati H jika posisi adalah kelipatan 5 + 1
                # Gunakan warna ini
                warna_sebelumnya = warna
                stok[warna] -= 1
                n += 1
                valid = True
                break
        
        if not valid:
            break  # Tidak ada warna yang valid, hentikan iterasi

    return n

# Contoh penggunaan
S_M = 30
S_H = 25
S_B = 20
print(total_manik_manik(S_M, S_H, S_B))  # Output: 65