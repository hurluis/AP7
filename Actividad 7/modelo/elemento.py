from dataclasses import dataclass

@dataclass
class Elemento:
    nombre:str

    def __eq__(self, otro):
        if isinstance(otro, Elemento):
            return self.nombre == otro.nombre
        return False

@dataclass
class Conjunto:
    contador = 0

    def __init__(self, nombre):
        self.elementos = []
        self.nombre = nombre
        self.__id = Conjunto.contador
        Conjunto.contador += 1

    @property
    def id(self):
            return self.__id
    
    def contiene(self, elemento):
        return any(e.nombre == elemento.nombre for e in self.elementos)
    
    def agregar_elemento(self, elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def __add__(self, otro):
        if isinstance(otro, Conjunto):
            nuevo_conjunto = Conjunto(f"{self.nombre} UNION {otro.nombre}")
            for elemento in self.elementos:
                nuevo_conjunto.agregar_elemento(elemento)
            for elemento in otro.elementos:
                nuevo_conjunto.agregar_elemento(elemento)
            return nuevo_conjunto
    
    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        if isinstance(conjunto1, Conjunto) and isinstance(conjunto2, Conjunto):
            interseccion = []
            for elemento in conjunto1.elementos:
                if conjunto2.contiene(elemento):
                    interseccion.append(elemento)
            nombre_interseccion = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
            nuevo_conjunto = Conjunto(nombre_interseccion)
            nuevo_conjunto.elementos = interseccion
            return nuevo_conjunto
        
    def __str__(self):
        elementos_str = ", ".join(elemento.nombre for elemento in self.elementos)
        return f"Conjunto {self.nombre}: ({elementos_str})"
    