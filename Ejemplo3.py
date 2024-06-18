class convocado:
    def __init__(self,jugador,razon_minutos):
        self.jugador = jugador
        self.razon_minutos = razon_minutos
        if self.razon_minutos<0.7:
            self.estado = "no es útil"
        else:
            self.estado = "es útil"

    def es_correcto(self,convocatoria):
        self.convocatoria = convocatoria
        return f"El jugador {self.jugador} {self.estado} y {self.convocatoria} es convocado"

class seleccion_juego:
    def __init__(self,victoria,jugador,razon_minutos):
        self.victoria = victoria
        self.jugador = jugador
        self.razon_minutos = razon_minutos
        self.input = convocado(self.jugador,self.razon_minutos)

    def resumen(self):
        if (self.victoria=="Si") & (self.razon_minutos<0.7):
            return f"La selección gana jugando con uno menos"
        elif (self.victoria=="Si") & (self.razon_minutos>0.7):
            return f"La selección gana porque no juega para un solo jugador. ¡Es un equipo!"
        elif (self.victoria=="No") & (self.razon_minutos<0.7):
            return f"El técnico debe asumir el hecho de convocar y alinear mal"
        else:
            return f"El técnico debe planificar mejor los partidos pese a convocar bien"

prueba1 = seleccion_juego("No","James",0.05)
print(prueba1.input.es_correcto("Si"))
print(prueba1.resumen())
