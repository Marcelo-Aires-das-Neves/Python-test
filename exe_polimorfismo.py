class Gato:
     def fazer_som(self):
         print("Miau")
class Cachorro:
     def fazer_som(self):
         print("au au")
def fazer_animal_fazer_som(animal):
    animal.fazer_som()
    
gato = Gato()
cachorro1 = Cachorro()

fazer_animal_fazer_som(gato)
fazer_animal_fazer_som(cachorro1)
