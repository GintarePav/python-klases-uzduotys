# programa sveikinasi ir klausia ar norime sveikintis dar (T/N)

while True:
    print('Labas rytas')
    ats = input('Ar norite dar karta pasisveikinti? (T/N)')
    if ats != "T" and ats !="t":
        break
print('Baigeme')