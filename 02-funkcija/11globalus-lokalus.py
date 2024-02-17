x = 5 # globalus

def fun1():
    x = 5 # lokalus
    print(x)

fun1() # nera return; lokalus kintamasis niekur neissaugomas ir negrazinamas funkcijos
print(x) # spausdins globalu kintamaji

# BET

def fun2():
    x = x + 1
    print(x) # error, funkcijoje globalaus kintamojo negalima pakeisti

def fun2(x): # argumentas nera tas pats x, kaip globalus x, susikuria naujas
    x = x + 1
    print(x) # spausdina 6
    return x

x = fun2(x) # kintamaji pakeicia ne funkcija, o sitas kintamasis
print(x) # spausdina 6
