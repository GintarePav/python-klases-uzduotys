#Turime statu trikampi, statine a ir izampine c.
#Rasti plota S
import math
staninisA = float(input('ivesk statinio a dydi: ')) #statinis turi buti mazesnis nei izambine
izambineC = float(input('ivesk izambines c dydi: '))
#b2 = c2 - a2
#b = Vc2 - a2 (V = saknis)
statinisB  = math.sqrt(math.pow(izambineC, 2) - math.pow(staninisA, 2))
print(statinisB)
plotas = round((staninisA * statinisB) / 2)
print('Plotas = ', plotas)
