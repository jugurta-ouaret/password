import hashlib
import json
import random
import string

def generer_mot_de_passe():
    longueur_mot_de_passe = 12
    caracteres = string.ascii_letters + string.digits + string.punctuation
    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur_mot_de_passe))
    return mot_de_passe

def verifier_mot_de_passe(mot_de_passe):
    
    return True

def hasher_mot_de_passe(mot_de_passe):
    hashed_password = hashlib.sha256(mot_de_passe.encode()).hexdigest()
    return hashed_password

def ajouter_mot_de_passe():
    
    mot_de_passe = generer_mot_de_passe()

    while not verifier_mot_de_passe(mot_de_passe):
        mot_de_passe = generer_mot_de_passe()

    mot_de_passe_hashe = hasher_mot_de_passe(mot_de_passe)

    print(f"Le mot de passe généré est : {mot_de_passe}")

    
    try:
        with open('mots_de_passe.json', 'r') as fichier:
            mots_de_passe = json.load(fichier)
    except FileNotFoundError:
        mots_de_passe = {}

    
    if mot_de_passe_hashe not in mots_de_passe.values():
        
        nouvel_id = len(mots_de_passe) + 1
        mots_de_passe[nouvel_id] = mot_de_passe_hashe

        
        with open('mots_de_passe.json', 'w') as fichier:
            json.dump(mots_de_passe, fichier)

        print("Mot de passe ajouté avec succès.")
    else:
        print("Le mot de passe existe déjà. Génération d'un nouveau mot de passe.")

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
