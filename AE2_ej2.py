class Alumno:
    def __init__(self, codigo, nombre, genero, n1, n2, n3, n4):
        self.codigo = codigo
        self.nombre= nombre
        self.genero= genero
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
    def promedio(self):
        return (self.n1 + self.n2 + self.n3 + self.n4)/4
    def estado(self): 
        if self.promedio() < 5:
            return "Pésimo"
        elif 5 <= self.promedio() < 10:
            return "Malo"
        elif 10 <= self.promedio() < 15:
            return "Regular"
        elif 15 <= self.promedio() < 17:
            return "Bueno"
        elif 17 <= self.promedio() < 19:
            return "Muy bueno"
        else:
            return "Excelente"       
    def obsequio(self):
        if self.promedio() < 18:
            return "\nSiga esforzandose"
        
        return "\nPor su esfuerzo, le obsequiamos un polo" if self.genero == "masculino" else "\nPor su esfuerzo, le obsequiamos un maletín"
    def __str__(self):
        return self.estado() + self.obsequio()        
oAlumno = Alumno(
    input("Código: "),
    input("Nombre: "),
    input("Género [masculino - femenino]: "),
    float(input("Ingrese la nota de la E1: ")),
    float(input("Ingrese la nota de la EP: ")),
    float(input("Ingrese la nota de la E2: ")),
    float(input("Ingrese la nota de la EF: "))
)

print(oAlumno)