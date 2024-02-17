# ledas, skystis
# temp > 0 ledas tirpsta
# temp < 0 vanduo sala
# temp == 0 kazkas

temp = int(input("Kokia temperatura lauke?"))
if temp < 0:
    print("Vanduo sala")
elif temp > 0:
    print("Ledas tirpsta")
else :
    print("Nieko")