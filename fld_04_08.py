mondat:str = input('mondat: ')

if mondat[-1] == '.':
    print('Ez egy kijelentő mondat.')
elif mondat[-1] == '?':
    print('Ez egy kérdőmondat.')
elif mondat[-1] == '!':
    print('Ez egy felkiáltó, felszólító vagy óhajtó mondat.')
else: print('erről nem lehet eldönteni, hogy milyen mondat')