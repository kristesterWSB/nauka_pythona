zakupy = {'ser': 10, 'mleko':15, 'konsola': 1500}


#dodawanie do slownika
zakupy['xbox']= 1400
#print(samolot['xyz'])
suma = 0.0
lista=[]
#petla po kluczu
for key, value in zakupy.items():
    suma+=value
    lista.append(key)

# if samolot.get('ser') and samolot.get('mleko') = True
#     suma*=0.9

print(','.join(lista))
print(f'koszt zakupow {suma}')


#petla po klucz wartosc
# for key, value in samolot.items():
#     print("{0}: {1}".format(key, value))
