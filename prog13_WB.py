
samolot = {'name': 'boeing', 'przebieg':1000.50, 'type': 'pasazerski'}

print(samolot['name'])
print(samolot['przebieg'])
print(samolot['type'])
#dodawanie do slownika
samolot['silnik']= 'odrzutowy'
#print(samolot['xyz'])
print('\n sprawdzenie czy obiekt istnieje w slowniku')
print(samolot.get('xyz'))
print('petla po kluczu \n')
#petla po kluczu
for klucz in samolot:
    print("{0}: {1}".format(klucz, samolot[klucz]))
print('petla po kluczu i wartosci \n')
#petla po klucz wartosc
for key, value in samolot.items():
    print("{0}: {1}".format(key, value))
