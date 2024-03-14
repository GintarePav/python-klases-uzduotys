ugis = [186, 198, 158, 175, 202, 187, 185, 180, 172]
# sukurti sarasa su tekstu Aukstas, jei ugis >= 186, jei 175<= vidutinis <= 185, kitais atvejais zemas
ugisTxt = ['Aukstas' if i >= 186 else 'Vidutinis' if 175<=i<=185 else "Zemas" for i in ugis]
print(ugisTxt)

#galima supaprastinti:
ugisTxt = ["Aukstas" if i >= 186 else "Vidutinis" if i >= 175 else "Zemas" for i in ugis]

