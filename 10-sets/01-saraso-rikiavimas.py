# isrinkimo algoritmas
def isrinkimas(sar1):
    i = 0
    kiekEl = len(sar1)
    while i < (kiekEl - 1):
        kurisNr = i
        j = i + 1
        while j < kiekEl:
            if sar1[j] < sar1[kurisNr]:
                kurisNr = j
            j += 1
        laikinas = sar1[kurisNr]
        sar1[kurisNr] = sar1[i]
        sar1[i] = laikinas
        i += 1
    return sar1

# burbuliuko isrinkimas
def burbuliukas(sar1):
    i = 0
    kiekEl = len(sar1)
    while i < kiekEl:
        j = 1
        while j < kiekEl:
            if sar1[j-1] > sar1[j]:
                laikinas = sar1[j-1]
                sar1[j-1] = sar1[j]
                sar[j] = laikinas
            j += 1
        i += 1
    return sar1

sar = [8, 6, 5, 2, 9, 4, 1, 13, 1, 4]
print(isrinkimas(sar))
print(burbuliukas(sar))