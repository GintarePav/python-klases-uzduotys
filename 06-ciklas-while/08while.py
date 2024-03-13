# programa sveikinasi ir klausia ar norime sveikintis dar (T/N)
pasirinkimas = True
while pasirinkimas:
    print('Labas rytas')
    ats = input('Ar norite dar karta pasisveikinti? (T/N)')
    if ats != "T" and ats !="t":
        pasirinkimas = False
print('Baigeme')