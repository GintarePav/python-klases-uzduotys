a = 2
b = 2.0
c = '2'

print (a == b)
print (a == c) # python nera === kaip js, todel yra tik true ir false pagal tipa. Nebus kaip JS, kad 2 == '2' yra true. Su Python tik false.

###

# Įvedami du skaičiai, rasti didžiausią ir mažiausią:

a  = int(input('a = ...'))
b  = int(input('b = ...'))

# did = max(a, b) kol kas nenaudojam

if a > b:
    did = a
    maz = b
else :
    did = b
    maz = a

###
    
if a > b:
    did = a
    maz = b
elif a < b:
    did = b
    maz = a
else :
    print('Skaičiai lygūs')

print(f'{did} yra didesnis už {maz}') # nieko neatspausdins, jei skaičiai lygūs, nes neatitiko sąlygų ir neturi did ir maz kintamųjų
# Print reiktų dėti prie visų sąlygų, bet būtų kodo kartojimas, tad kai daugiau kodo, geriau kurti funkciją ir ją kviesti