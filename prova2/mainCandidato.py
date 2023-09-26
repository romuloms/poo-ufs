# Aluno: Romulo Menezes de Santana

from candidato import Candidato


candidato = Candidato("Joao", "12345678910", "12346789", "joao@gmail.com", "1199887766", 10)

candidato.imprimeDados()

try:
    candidato.setNome("")
except ValueError as erro:
    print(erro)

try:
    candidato.setNome("Robson")
except ValueError as erro:
    print(erro)

try:
    candidato.aumentaPontos(-20)
except ValueError as erro:
    print(erro)

try:
    candidato.setCPF(20)
except ValueError as erro:
    print(erro)

try:
    candidato.setRG("039120391")
except ValueError as erro:
    print(erro)

try:
    candidato.setEmail("")
except ValueError as erro:
    print(erro)

try:
    candidato.setTelefone("1132013932")
except ValueError as erro:
    print(erro)

try:
    candidato.setPontos(120)
except ValueError as erro:
    print(erro)

try:
    candidato.aumentaPontos(20)
except ValueError as erro:
    print(erro)

candidato.imprimeDados()