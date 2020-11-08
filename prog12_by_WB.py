koszyk_items = ['mleko', 'czekolada', 'sok', 'piwo']
koszyk_ilosc = [2,1,3, 6]
koszyk_cena = [30,40,200, 6]

suma = 0.0
for idx in range(len(koszyk_items)):
    item = koszyk_items[idx]
    ile = koszyk_ilosc[idx]
    cena = koszyk_cena[idx] * ile
    # if ile > 2 and item== 'mleko':
    #     print('znizka dla mleka')
    print("{0} {1} {2}".format(item, ile, cena))
    suma = suma +cena
znizka_r1 = 0

if len(koszyk_items) >3: #R1
    print("Znizka R1")
    suma =suma - (suma *5) / 100
    znizka_r1 = 1
if suma >= 500 and znizka_r1 = 0 : #R2
    print("Znizka R2")
    suma - (suma * 10) / 100

print("wartosc koszyka {0}".format(suma))
