# callback: Fonction qui est passée en paramètre à une autre fonction

class MoteurGaz:
    def __init__(self, puissance, type_moteur):
        self.puissance = puissance
        self.type_moteur = type_moteur

    def action(self):
        print("Vroom Vroom"*self.puissance)


class MoteurElectrique:
    def __init__(self, puissance, type_moteur):
        self.puissance = puissance
        self.type_moteur = type_moteur

    def action(self):
        print("Zzzzzz"*self.puissance)


class Vehicule:
    def __init__(self, marque, modele, prix, callback_moteur):
        self.marque = marque
        self.modele = modele
        self.prix = prix
        self.action_moteur = callback_moteur

    def rouler(self):
        self.action_moteur()


class Voiture(Vehicule):
    def __init__(self, marque, modele, prix, nb_portes, callback_moteur):
        super().__init__(marque, modele, prix, callback_moteur)
        self.nb_portes = nb_portes

    def __str__(self):
        return f"{self.marque} {self.modele} {self.prix} {self.nb_portes}"



motor = MoteurGaz(4, "V8")
ma_voiture = Voiture("Toyota", "corolla", 25000, 4, motor.action)

ma_voiture.rouler()