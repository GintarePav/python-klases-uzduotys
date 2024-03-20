# with open('03duom.txt', 'r', encoding='utf-8') as f:
#     txt = f.read()
# print(txt)

# with open('03duom.txt', 'r', encoding='utf-8') as f:
#     txt = f.readline() # nuskaito po viena eilute
#     txt2 = f.readline()
# print(txt, txt2) #atspausdins su tarpeliu pries antra eilute; galima su +, bet nerekomenduojama, nes leciau

with open('03duom.txt', 'r', encoding='utf-8') as f:
    txt = f.readlines() # padarys list, tik bus su \n 

print(txt)