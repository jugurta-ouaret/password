import hashlib
import re

def verifier_mot_de_passe(mot_de_passe):
    if len(mot_de_passe) < 8:
        return False
    if not re.search("[A-Z]", mot_de_passe):
        return False
    if not re.search("[a-z]", mot_de_passe):
        return False
    if not re.search("[0-9]", mot_de_passe):
        return False
    if not re.search("[!@#$%^&*]", mot_de_passe):
        return False
    return True

def hasher_mot_de_passe(mot_de_passe):
    hashed_password = hashlib.sha256(mot_de_passe.encode()).hexdigest()
    return hashed_password

def demander_mot_de_passe():
    while True:
        mot_de_passe = input("Veuillez entrer votre mot de passe : ")
        if verifier_mot_de_passe(mot_de_passe):
            return mot_de_passe
        else:
            print("Le mot de passe ne répond pas aux exigences de sécurité. Veuillez choisir un nouveau mot de passe.")

def main():
    mot_de_passe = demander_mot_de_passe()
    mot_de_passe_hashe = hasher_mot_de_passe(mot_de_passe)
    print("Mot de passe valide. Mot de passe haché avec SHA-256 :", mot_de_passe_hashe)

if __name__ == "__main__":
    main()
