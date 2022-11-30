# a karakterláncok (str, string) valójában összetett típusok
# "karakterek" (chr, character) listája
# MINDENT, amit egy listával meg lehet csinálni, azt egy sima egyszerű str-el is

string:str = "ÁrVíZtŰrŐ TüKörRfÚrÓgÉp"

# pl. le tudom kérdezni az 'elemszámát' (karakterek száma az str-ben)
hossz:int = len(string)
print(f'az {string} {hossz} karakterből áll')

# vagy végig tudom iterálni ciklusokkal
for c in string: print(c, end='  ')

# tudom hivatkozni index alapján adott elemét:
print(f'\n{string} első karaktere: {string[0]}')

# viszont 'csak olvasható', tehát az értékadás a 'lista elemeire' nem működik:
# string[0] = "D"

if 'Ű' in string: print('van benne "Ű" betű')
else: print('nincs benne "Ű" betű')

print(string)

# van sok beépített függvény, amit lehet használni, pl:

cspupa_nagy:str = string.upper()
print(cspupa_nagy)

csupa_kicsi:str = string.lower()
print(csupa_kicsi)

kapitalizalt:str = string.capitalize()
print(kapitalizalt)

cim:str = string.title()
print(cim)

p_az_eleje:bool = string.startswith('p')
if p_az_eleje: print('"P" betűvel kezdődik')
else: print('NEM "P" betűvel kezdődik')

p_a_vege:bool = string.endswith('p')
if p_a_vege: print('"P" betűvel végződik')
else: print('NEM "P" betűvel végződik')

print('gépre végződik' if string.endswith('gÉp') else 'nem gépre végződik')

xekkel:str = string.replace('T', 'X')
print(xekkel)
toval:str = string.replace('ÁrVíZ', 'Tó')
print(toval)

szavak:list[str] = string.split()
print(szavak)

tablazat_sora:str = 'Kovács József;férfi;1981;Peugeto'

mezok:list[str] = tablazat_sora.split(';')
print(mezok)

csunya_karakterlanc = "  \t      ;;;karácsonyfa;\n\n\n       \t"
szep_karakterlanc = csunya_karakterlanc.strip().strip(';')
print(szep_karakterlanc)