'''Acciones del sitemas puede hacer con el usuario (ABC)'''

#esto servira para migrar al futuro al cualquier base de dato
#guardar un usario y buscar usuario por cedula

from abc import ABC, abstractmethod

#Definiicon de contracto (puerto)

class ClsUserRepository(ABC):

    @abstractmethod
    def save(self, user_data: dict):
        """Regla de la base de datos guardar el diccionario de usuarios"""
        pass

    @abstractmethod
    def find_by_cedula(self,cedula: str):
        """regla de la base d e datos debe poner buscar si una cedula ya existe"""
        pass