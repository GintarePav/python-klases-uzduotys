sar1 = [5, 8, 4, 7, 9]
sar2 = [2, 14, 4, 11, 3]
# map leidzia pritaikyti iteruojama funkcija
sar3 = list(map(lambda a, b: a + b if a > b else a - b, sar1, sar2))
print(sar3)

# galima su filter, bet reikia boolean:
# syntax: filter(function, iterable)
# function - A Function to be run for each item in the iterable
# iterable - The iterable to be filtered
# e.g. 

# Filter the array, and return a new array with only the values equal to or above 18:

# ages = [5, 12, 17, 18, 24, 32]

# def myFunc(x):
#   if x < 18:
#     return False
#   else:
#     return True

# adults = filter(myFunc, ages) (cia vietoj myFunch galima pateikti lambda, i.e. anonimine funkcija)

# for x in adults:
#   print(x)