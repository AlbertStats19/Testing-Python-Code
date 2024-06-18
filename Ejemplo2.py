class Animal:
    def __init__(self,clase,nombre,hablo):
        self.clase = clase
        self.nombre = nombre
        self.hablo = hablo
    
    def presentarse(self):
        return f"Soy un {self.clase} y mi nombre es {self.nombre}"


class Sonido(Animal):
    def hablar(self,veces):
        self.hablo = (self.hablo + " ") * veces
        return f"Yo {self.nombre} digo: {self.hablo}"

prueba1 = Sonido("Perro","Goofy","guau")
print(prueba1.presentarse())
print(prueba1.hablar(3))