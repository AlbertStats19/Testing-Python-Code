class Animal:
    def __init__(self,nombre,sonido):
        self.nombre = nombre
        self.sonido = sonido
    
    def hablar(self):
        return f"{self.nombre} dice {self.sonido}"

prueba1 = Animal("Goofy","guau")
print(prueba1.hablar())