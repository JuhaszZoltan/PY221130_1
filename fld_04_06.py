szoveg:str = input('szöveg: ')
c:int = 0
for b in szoveg:
    if b in 'Ee': c += 1
print(f'"e" betűk száma a szövegben: {c}')