# Aluno: Romulo Menezes de Santana

from cadastroCandidato import CadastroCandidato
from candidato import Candidato
from candidatoI import CandidatoI

cadastro = CadastroCandidato()
candidatoIndigena = CandidatoI("Kauan", "77777678910", "32146789", "kauan@gmail.com", "1199887766", 70, 2000)
candidatoIndigena2 = CandidatoI("Tucuman", "88888678910", "12346789", "tucuman@gmail.com", "1199883000", 50, 2001)
candidatoComum = Candidato("Joao", "12345678910", "42146789", "joao@gmail.com", "1199881111", 80)
candidatoComum2 = Candidato("Robson", "12345678911", "52146789", "robson@gmail.com", "1199882222", 20)

cadastro.numeroCandidatos()
cadastro.insereCandidato(candidatoIndigena)
cadastro.insereCandidato(candidatoIndigena2)
cadastro.insereCandidato(candidatoComum)
cadastro.insereCandidato(candidatoComum2)
cadastro.numeroCandidatos()
cadastro.listarCandidatosIndigenas()

try:
    cadastro.insereCandidato(2000)
except ValueError as erro:
    print(erro)

try:
    cadastro.removeCandidato("Josue")
except ValueError as erro:
    print(erro)

try:
    cadastro.removeCandidato(candidatoIndigena)
except ValueError as erro:
    print(erro)

cadastro.listarCandidatosIndigenas()