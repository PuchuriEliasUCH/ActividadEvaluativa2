class Trabajador: 
    cate = {"a": 4500, "b": 3500, "c": 2800, "d": 2500, "e": 2000}

    def __init__(self, codigo: str, nombre: str, categoria: str, num_hijos: int):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.num_hijos = num_hijos

    def bono(self):
        return self.cate[self.categoria] * 0.095
    
    def asignacion(self):
        return self.cate[self.categoria] * 0.05 * self.num_hijos
    
    def __str__(self):
        return f"El sueldo neto de {self.nombre} es S/{self.cate[self.categoria] + self.bono() + self.asignacion()}"
    
oTrabajador = Trabajador(
    input("Código: "), 
    input("Nombre: ").capitalize(), 
    input("Categoría [A-B-C-D-E]: ").lower(), 
    int(input("Número de hijos: "))
)
print(oTrabajador)