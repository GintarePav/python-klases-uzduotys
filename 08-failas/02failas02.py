with open('data02.txt', 'w', encoding='utf-8') as f:
    f.write("Test\n")
    a = 656
    f.write(str(a))
    f.write(f'\n{a}')
