def tampilAngka(batas,i = 1):
    prefix = '--' * (i-1)

    print(f'{prefix} Sebelum rekursif ({i})')

    if (i < batas) :
        tampilAngka(batas, i+1)

    print(f'{prefix} Setelah rekursif ({i})')

tampilAngka(30)
