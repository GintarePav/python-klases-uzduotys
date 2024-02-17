def atimtiDuSkaicius(skaicius1=0, skaicius2=0):
    skirtumas = skaicius1 - skaicius2
    return skirtumas

sk1 = 15
sk2 = 9

print(atimtiDuSkaicius(sk1, sk2))
print(atimtiDuSkaicius(sk2, sk1))
print(atimtiDuSkaicius(skaicius2=sk2, skaicius1=sk1))
