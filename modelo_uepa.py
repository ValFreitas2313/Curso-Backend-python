class MembroUEPA:
    def __init__(self, nome, matricula, email):
        self.nome = nome
        self.matricula = matricula
        self.email = email
        
    def apresentar(self):
        print(f"sou membro da uepa. nome: {self.nome}, matricula: {self.matricula}, email: {self.email}")
        
class Aluno(MembroUEPA):
    def __init__(self, nome, matricula, email, curso):
        super(). __init__(nome, matricula, email)
        self.curso = curso
        self.matricula = matricula
        self.email = email
        
    def verificar_notas(self):
        print(f"O aluno {self.nome}, está verificando as notas no curso de {self.curso}.")
    
    def apresentar(self):
        print(f"Sou o aluno {self.nome}, matricula {self.matricula}, do curso de {self.curso}.")
        
class Professor(MembroUEPA):
    def __init__(self, nome, matricula, email, departamento):
        super().__init__(nome, matricula, email)
        self.departamento = departamento
        
    def lancar_frequencia(self):
        print(f"O professor {self.nome}, do departamento {self.departamento}, está lançando frequência.")
        
        if __name__ == "__main__":
            aluno1 = Aluno("Valéria", "202501", "valeria@uepa.br", "Quimica")
            Professor1 = Professor("Carlos", "P12345", "carlos@uepa.br", "Ciências Exatas")
            
            
            aluno1.apresentar()
            aluno1.verificar_notas()
            
            Professor1.apresentar()
            Professor1.lancar_frequencia()
            
aluno1 = Aluno("valeria", 202501, "valeria@uepa.br", "Quimica")
aluno1.apresentar()