from Domain.addOperation import AddOperation
from Domain.masina import Masina
from Domain.masinaValidator import MasinaValidator
from Repository.repository import Repository
from Service.undoRedoService import UndoRedoService


class MasinaService:
    def __init__(self,
                 masinaRepository: Repository,
                 masinaValidator: MasinaValidator,
                 undoRedoService: UndoRedoService):
        self.__masinaRepository = masinaRepository
        self.__masinaValidator = masinaValidator
        self.__undoRedoService = undoRedoService

    def getAll(self):
        return self.__masinaRepository.read()

    def adauga(self, idMasina, indicativ, nivelConfort, plataCard, model):
        masina = Masina(idMasina, indicativ, nivelConfort, plataCard, model)
        self.__masinaValidator.valideaza(masina)
        self.__masinaRepository.adauga(masina)
        self.__undoRedoService.addUndoOperation(
            AddOperation(self.__masinaRepository, masina))

    def sterge(self, idMasina):
        self.__masinaRepository.sterge(idMasina)

    def modifica(self, idMasina, indicativ, nivelConfort, plataCard, model):
        masina = Masina(idMasina, indicativ, nivelConfort, plataCard, model)
        self.__masinaValidator.valideaza(masina)
        self.__masinaRepository.modifica(masina)
