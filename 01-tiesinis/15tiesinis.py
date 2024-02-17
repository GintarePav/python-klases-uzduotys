# Statybininkas pirma diena paklojo m1 metru, cm1 centimetru ir mm1 plyteliu. 
# Antra diena - m2 metru, cm2 centimetru ir mm2 milimetru plyteliu.

m1 = int(input("kiek metru per pirma diena? "))
cm1 = int(input("kiek centimetru per pirma diena? "))
mm1 = int(input("kiek milimetru per pirma diena? "))

m2 = int(input("kiek metru per antra diena? "))
cm2 = int(input("kiek centimetru per antra diena? "))
mm2 = int(input("kiek milimetru per antra diena? "))

visoMm = (m1 * 1000) + (cm1 * 10) + m1 + (m2 * 1000) + (cm1 * 10) + m1
visoMetrai = visoMm // 1000
likutis = visoMm % 1000
visoCm = likutis // 10
likeMm = likutis % 10

print(f'Viso {visoMetrai} m., {visoCm} cm., {likeMm} mm.')

