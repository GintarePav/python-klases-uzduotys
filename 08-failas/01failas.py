# raktai:
# w - write
# a - append
# r - read

rasyk = open('data01.txt', 'w', encoding='utf-8')
rasyk.write('Pirmas kartas su byla')
a = 5
sar = [1, 8, 9, 'Labas']
#rasyk.write(a) bus klaida, nes ivedimas priima tik string
rasyk.write(f'{a}')
rasyk.write(f'\n{sar}')
rasyk.write(str(a))
#rasyk.write('Ačiū') neparasys lietuviskom raidem, jei nebus encoding='utf-8'
rasyk.close()
