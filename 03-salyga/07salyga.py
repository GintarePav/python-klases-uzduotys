# ar laimingas skaicius
# laimingas tarp 5 ir 10 arba tarp 20 ir 25

sk = int(input('sk = ... '))
laimingas = (sk >= 5 and sk <= 10) or (sk >= 20 and sk <= 25) # galima pernaudoti vėliau ir reiks mažiau rašyti ifuose
# laimingas = (5 <= sk <= 10) or (20 <= sk <= 25), atrodo paprasčiau, bet ne visada tinka

if laimingas :
    print(f'Skaicius {sk} laimingas')
else :
    print(f'Skaicius {sk} nelaimingas')