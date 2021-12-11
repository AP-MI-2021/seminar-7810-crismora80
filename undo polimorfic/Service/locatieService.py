from Domain.addOperation import AddOperation
from Domain.locatie import Locatie
from Domain.modifyOperation import ModifyOperation
from Repository.repository import Repository
from Service.undoRedoService import UndoRedoService


class LocatieService:
    def __init__(self, locatieRepository: Repository, undoRedoService: UndoRedoService):
        self.__locatieRepository = locatieRepository
        self.__undoRedoService = undoRedoService

    def getAll(self):
        return self.__locatieRepository.read()

    def adauga(self, idLocatie, numeStrada, numar, bloc, scara, alteIndicatii):
        locatie = Locatie(
            idLocatie,
            numeStrada,
            numar,
            bloc,
            scara,
            alteIndicatii)
        self.__locatieRepository.adauga(locatie)
        self.__undoRedoService.addUndoOperation(AddOperation(self.__locatieRepository, locatie))

    def sterge(self, idLocatie):
        self.__locatieRepository.sterge(idLocatie)

    def modifica(self,
                 idLocatie,
                 numeStrada,
                 numar,
                 bloc,
                 scara,
                 alteIndicatii):
        locatieVeche = self.__locatieRepository.read(idLocatie)

        locatie = Locatie(
            idLocatie,
            numeStrada,
            numar,
            bloc,
            scara,
            alteIndicatii)
        self.__locatieRepository.modifica(locatie)
        self.__undoRedoService.addUndoOperation(ModifyOperation(self.__locatieRepository, locatieVeche, locatie))

    def ordoneazaLocatiiDupaIndicatii(self):
        return sorted(self.__locatieRepository.read(),
                      key=lambda locatie: len(locatie.alteIndicatii),
                      reverse=True)
