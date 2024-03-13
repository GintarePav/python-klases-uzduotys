# Jei isivedam 5, programa atsapusdina:
# 1 
# 2 2 
# 3 3 3 
# etc

sk = int(input('sk='))

# for j in range(1, sk+1):
#     for i in range(1, sk+1):
#         if i <= j:
#             print(j, end=(' '))
#     print()

for j in range(1, sk + 1):
    for i in range(1, j+1):
        print(j, end=(' '))
    print()