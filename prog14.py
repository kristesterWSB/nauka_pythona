# produkty = {'SS12': 'sukienka_trojka', 'P12': 'spodnie'}
#
# igla = 'P12'
#
# if igla in produkt:
#     print('istnieje')
#     print(produkt['P12'])

produkty = {'SS12' : {'nazwa':'sukienka_trojka', 'rozmiary':['s','l', 'xl']},
'P12': {'nazwa':'spodnie','rozmiary':['s','xl']}}

for id in produkty:
    p = produkty[id]
    rozmiary = p['rozmiary']
    print(p['nazwa'])
    for r in rozmiary:
        print(r)
