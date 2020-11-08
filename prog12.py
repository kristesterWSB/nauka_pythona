produkt = ['slodycze', 'chleb', 'woda', 'owoce']
cena = [5.23, 2.42, 1.59, 4.99]
koszt=0
koszyk=[]

for i in range(len(produkt)):
    print('twoj produkt to: ' + produkt[i] + ' a cena to: ' + str(cena[i]))
    koszyk.append(produkt[i])
    koszt+=float(cena[i])

if len(koszyk)>2:
    print("Brawo masz 5 procent rabatu")
    koszt*=0.95
else:
    print('Brak rabatu')
if koszt > 500:
    koszt*=0.9
    print('twoje zakupy sa wieksze niz 500 zl masz 10 procent rabatu')
else:
    print('Twoje zakupy sa mniejsze niz 500, kup wiecej')

print(f'\nKoszt twoich zakupw to {round(koszt,2)} zl \ntwoje zakupy to: '+ ','.join(koszyk))
