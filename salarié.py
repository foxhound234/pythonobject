from entreprise import Entreprise

class Salarié(Entreprise):

    def __init__(self,nom,salaire,poste):
        super().__init__(nom)
        self.salaire=salaire
        self.poste=poste

    def modifiersalaire(self,salaire):
        self.salaire=salaire



    def poste(self,poste):
        self.poste=poste

