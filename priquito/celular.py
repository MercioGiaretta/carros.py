class Animal():
    quantidade_patas = 4
    tem_rabo = False
    tem_pelo = True
    especie = ''

class Cachorro(Animal):
    tem_rabo = True
    especie = 'Canis Lupus familiaris'
    raca = 'Shitzu'
    nome = 'Sérgio'
    porte = "Pequeno"

    def latir():
        return 'auau'

    def beber():
        return 'schlopschlopschlopschlopschlopschlopschlopschlopschlopschlopschlopschlopschlopschlopschlopschlopschlopschlopschlopschlopschlopschlop'

    def dormir():
        return 'zzz'

print(Cachorro.beber())
print(Cachorro.dormir())
print(Cachorro.latir())
print(Cachorro.especie())
print(Cachorro.nome())
print(Cachorro.quantidade_patas())
print(Cachorro.tem_pelo())
print(Cachorro.tem_rabo())        