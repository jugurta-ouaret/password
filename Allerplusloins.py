import hashlib
import json

def verifier_mot_de_passe(mot_de_passe):
    # Ajoute tes règles de vérification de mot de passe ici
    # (longueur, caractères requis, etc.)
    return True

def hasher_mot_de_passe(mot_de_passe):
    hashed_password = hashlib.sha256(mot_de_passe.encode()).hexdigest()
    return hashed_password

def ajouter_mot_de_passe():
    mot_de_passe = input("Entrez votre mot de passe : ")

    if verifier_mot_de_passe(mot_de_passe):
        mot_de_passe_hashe = hasher_mot_de_passe(mot_de_passe)

        # Charger les mots de passe existants depuis le fichier
        try:
            with open('mots_de_passe.json', 'r') as fichier:
                mots_de_passe = json.load(fichier)
        except FileNotFoundError:
            mots_de_passe = {}

        # Ajouter le nouveau mot de passe au dictionnaire avec un identifiant unique
        nouvel_id = len(mots_de_passe) + 1
        mots_de_passe[nouvel_id] = mot_de_passe_hashe

        # Enregistrer les mots de passe dans le fichier
        with open('mots_de_passe.json', 'w') as fichier:
            json.dump(mots_de_passe, fichier)

        print("Mot de passe ajouté avec succès.")
    else:
        print("Le mot de passe ne répond pas aux exigences de sécurité.")

def afficher_mots_de_passe():
    try:
        with open('mots_de_passe.json', 'r') as fichier:
            mots_de_passe = json.load(fichier)
            if not mots_de_passe:
                print("Aucun mot de passe enregistré.")
            else:
                print("Mots de passe enregistrés:")
                for identifiant, mot_de_passe in mots_de_passe.items():
                    print(f"ID: {identifiant}, Mot de passe haché: {mot_de_passe}")
    except FileNotFoundError:
        print("Aucun mot de passe enregistré.")

def main():
    while True:
        choix = input("Choisissez une option:\n1. Ajouter un mot de passe\n2. Afficher les mots de passe\n3. Quitter\n")

        if choix == '1':
            ajouter_mot_de_passe()
        elif choix == '2':
            afficher_mots_de_passe()
        elif choix == '3':
            print("Au revoir!")
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")

if __name__ == "__main__":
    main()
