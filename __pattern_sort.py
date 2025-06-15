def susun_pola():
    obyek_A = 22
    obyek_B = 19
    obyek_C = 18
    obyek_D = 17
    
    pola = ""
    
    while True:
        if obyek_A >= 0:
            pola += "A"
            obyek_A -= 1
        if obyek_B >= 0:
            pola += "B"
            obyek_B -= 1
        if obyek_C >= 0:
            pola += "C"
            obyek_C -= 1
        if obyek_D >= 0:
            pola += "D"
            obyek_D -= 1
        
        # Memeriksa apakah ada obyek yang telah habis
        if obyek_A == 0 or obyek_B == 0 or obyek_C == 0 or obyek_D == 0:
            break
        
        # Memeriksa apakah ada obyek yang bertemu dengan obyek yang sejenis
        if pola[-1] == pola[-2]:
            break

    return pola

hasil_pola = susun_pola()
print(hasil_pola)
