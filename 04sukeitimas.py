bokalas = 'pienas'
stiklineVaikiska = 'alus'
print('bokale yra', bokalas)
print('stiklineje yra', stiklineVaikiska)
puodas = bokalas #su papildomu kintamuoju
bokalas = stiklineVaikiska
stiklineVaikiska = puodas
print (puodas, bokalas, stiklineVaikiska)
bokalas, stiklineVaikis = stiklineVaikiska, bokalas #be papildomo kintamojo