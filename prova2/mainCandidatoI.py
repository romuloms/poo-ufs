# Aluno: Romulo Menezes de Santana

from candidatoI import CandidatoI

candidatoI = CandidatoI("Kauan", "12345678910", "12346789", "kauan@gmail.com", "1199887766", 10, 2000)

candidatoI.imprimeDadosI()

try:
    candidatoI.setNumRANI("123")
except ValueError as erro:
    print(erro)

try:
    candidatoI.setNumRANI(-2)
except ValueError as erro:
    print(erro)

try:
    candidatoI.setNumRANI(1200)
except ValueError as erro:
    print(erro)

candidatoI.imprimeDadosI()