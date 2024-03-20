try:
    f = open('data02.txt', 'w', encoding='utf-8')
    f.write("Test\n")
    a = 656
    f.write(str(a))
    f.write(f'\n{a}')
finally:
    f.close()
