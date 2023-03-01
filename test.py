class Perro:
    """ Clase de Perro """
    def __init__(self, nombre):
        """Metodo contructor

        Args:
            nombre (str): nombre de la clase de Perro
        """
        self.nombre = nombre

    def ladrar(self):
        print("Wao, wao")

    def __str__(self):
        return "Perro: {}".format(self.nombre)

class Firulai(Perro):
    """Clase hija Chihuahua de Perro

    Args:
        Perro (classobj): Clase base Perro
    """
    def __init__(self, nombre):
        """Metodo contructor

        Args:
            nombre (str): nombre de la clase de Perro
        """
        super().__init__(nombre)
        self.__tipo = "chauchau"

    def ladrar(self):
        print("Grrrrrrrrrrrrrrr")

    def __str__(self):
        return "Firulai: {}, es un tipo de perro: {}".format(self.nombre, self.__tipo)

class Chihuahua(Perro):
    """Clase hija Chihuahua de Perro

    Args:
        Perro (classobj): Clase base Perro
    """
    def __init__(self, nombre, ejercita):
        """Metodo contructor

        Args:
            nombre (str): nombre de la clase de Perro
            ejercita (bool): si ejercita el perro Chihuahua
        """
        super().__init__(nombre)
        self.__ejercita = ejercita

    def ladrar(self):
        print("ladra mucho")

    def __str__(self):
        return "Firulai: {} y el hace ejercios: {}".format(self.nombre, self.__ejercita)

perro1 = Perro("Pixel")
print(perro1)

perro2 = Firulai("Dexter")
print(perro2)

perro3 = Chihuahua("Cocum", True)
print(perro3)
