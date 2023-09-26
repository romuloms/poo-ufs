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
    
    def numeroCandidatos(self):
        print(f"Numero de candidatos: {len(self.__cadastro)}")

    def removeCandidato(self, candidato):
        if isinstance(candidato, Candidato):
            self.__cadastro.remove(candidato)
        else:
            raise ValueError("O objeto a ser removido deve ser do tipo candidato.")