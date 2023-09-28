# Aluno: Romulo Menezes de Santana

from candidato import Candidato
from candidatoI import CandidatoI


class CadastroCandidato:
    def __init__(self):
        self.__cadastro = list()

    def insereCandidato(self, candidato):
        if isinstance(candidato, Candidato):
            self.__cadastro.append(candidato)
        else:
            raise ValueError("O objeto a ser inserido deve ser do tipo candidato.")
        
    def listarCandidatosIndigenas(self):
        for candidatoI in self.__cadastro:
            if isinstance(candidatoI, CandidatoI):
                candidatoI.imprimeDadosI()
    
    def listarCandidatos(self):
        for candidato in self.__cadastro:
            if isinstance(candidato, Candidato):
                candidato.imprimeDados()
            elif isinstance(candidato, CandidatoI):
                candidato.imprimeDadosI()

    def numeroCandidatos(self):
        print(f"Numero de candidatos: {len(self.__cadastro)}")

    def tipoCandidato(self, candidato):
        if isinstance(candidato, CandidatoI):
            print(f"O candidato {candidato.getNome()} é do tipo Candidato Indigena.")
        elif isinstance(candidato, Candidato):
            print(f"O candidato {candidato.getNome()} é do tipo Candidato Comum.")
        else:
            print("Tipo desconhecido.")

    def removeCandidato(self, candidato):
        if isinstance(candidato, Candidato):
            self.__cadastro.remove(candidato)
        else:
            raise ValueError("O objeto a ser removido deve ser do tipo candidato.")