# Koks laikas bus po 1 min?
# 15:25 po 1 min bus 15:26
# 15:59 po 1 min bus 16:00
# 23:59 po 1 min bus 00:00

val = int(input('Kiek valandu? '))
min = int(input('Kiek minuciu? '))

minNauja = min + 1
valNauja = val + minNauja // 60
minNauja = minNauja % 60
valNauja = valNauja % 24

print(f'Po minutes bus {valNauja}:{minNauja}')
