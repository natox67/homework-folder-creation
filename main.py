from dataclasses import dataclass  # On importe dataclass pour créer facilement des classes de données


@dataclass(frozen=True)  # Déclare une dataclass immuable (frozen=True empêche toute modification après création)
class Row:  # Classe Row qui représente une ligne (une personne)
    last_name: str  # Champ pour le nom de famille
    first_name: str  # Champ pour le prénom
    age: int  # Champ pour l'âge

    @classmethod  # Méthode de classe (on l'appelle depuis la classe directement, pas depuis un objet)
    def from_dict(cls, row):  # Permet de créer un Row à partir d'un dictionnaire
        return cls(
            row["last_name"],  # On lit "last_name" dans le dictionnaire
            row["first_name"],  # On lit "first_name" dans le dictionnaire
            row["age"],  # On lit "age" dans le dictionnaire
        )


def part1() -> None:  # Première partie : montrer un simple dictionnaire
    dic1 = {  # On crée un dictionnaire avec un prénom, un nom et un âge
        "last_name": "Doe",
        "prenom": "John",  # ⚠️ Ici la clé est "prenom" au lieu de "first_name"
        "age": 42,
    }
    print(dic1)  # On affiche le dictionnaire


def part2() -> set[Row]:  # Deuxième partie : créer et stocker plusieurs Row dans un set
    dic1 = {  # Premier dictionnaire
        "last_name": "Doe",
        "first_name": "John",
        "age": 42,
    }
    dic2 = {  # Deuxième dictionnaire
        "last_name": "Martin",
        "first_name": "Pierre",
        "age": 23,
    }
    dic3 = {  # Troisième dictionnaire
        "last_name": "Dune",
        "first_name": "Christine",
        "age": 23,
    }
    dic4 = {  # Quatrième dictionnaire
        "last_name": "Tellaz",
        "first_name": "Marie",
        "age": 12,
    }
    struct = {  # On crée un set de Row (automatiquement sans doublons)
        Row.from_dict(dic1),
        Row.from_dict(dic2),
        Row.from_dict(dic3),
        Row.from_dict(dic4),
    }
    print(struct)  # On affiche le set de personnes
    return struct  # On renvoie le set


def part3() -> None:  # Troisième partie : menu interactif
    data_storage = part2()  # On initialise la "base de données" avec part2
    while True:  # Boucle infinie tant que l'utilisateur ne choisit pas "Quitter"
        print("\nMenu :")  # On affiche le menu
        print("1. Ajouter un nom")
        print("2. Afficher tous les noms")
        print("3. Effacer un nom")
        print("4. Quitter")

        choice = input("Choisissez une option (1-4) : ")  # On demande le choix
        match choice:  # On utilise le pattern matching
            case "1":  # Ajouter un nom
                print("J'ajoute un nom")
                new_row = _read_row()  # On lit un nouvel utilisateur
                if new_row in data_storage:  # Vérifie s'il existe déjà
                    print("Cette donnée est déja présente")
                    continue  # On repart au menu
                data_storage.add(new_row)  # Sinon on l'ajoute

            case "2":  # Afficher tous les noms
                print("J'affiche tous les noms:")
                for row in data_storage:  # On parcourt tous les Row
                    print(row)  # On affiche chaque personne
            case "3":  # Effacer un nom
                print("J'efface le nom")
                existing_row = _read_row()  # On lit la personne à supprimer
                data_storage.remove(existing_row)  # On la retire du set
                print(f"Le nom {existing_row.last_name} a été effacé avec succés")
            case "4":  # Quitter
                print("Quitter")
                return  # On sort de la fonction donc du programme
            case _:  # Cas par défaut (erreur)
                print("Erreur")
                return


def _read_row() -> Row:  # Fonction pour lire une personne depuis le clavier
    dic = {  # On crée un dictionnaire avec les infos demandées à l'utilisateur
        "last_name": input("Le nom : "),
        "first_name": input("Le prénom : "),
        "age": input("L'age : "),  # ⚠️ Attention: age est lu comme une chaîne
    }
    return Row.from_dict(dic)  # On transforme le dict en Row


def main() -> None:  # Fonction principale
    part1()  # On exécute la première partie
    part2()  # On exécute la deuxième partie
    part3()  # On lance le menu interactif


if __name__ == "__main__":  # Point d'entrée du programme
    main()  # On appelle la fonction main
