a  = int(input('a = ...'))
b  = int(input('b = ...'))

def isvesti(did, maz):
    print(f'{did} yra didesnis už {maz}')
    
if a > b:
    isvesti(did=a, maz=b)
elif a < b:
   isvesti(maz=a, did=b)
else :
    print('Skaičiai lygūs')