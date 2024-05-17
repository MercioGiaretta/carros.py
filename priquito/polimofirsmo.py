class Animal:
    def emitir_som(self):
        return 'qualquer som'

class Cachorro(Animal):
    def emitir_som(self):
        return 'auau'

cachorro = Cachorro()
print(cachorro.emitir_som())

class Gato(Animal):
    def emitir_som(self):
        return 'miau'