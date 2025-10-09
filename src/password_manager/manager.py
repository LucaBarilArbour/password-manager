import os, json, sys, hashlib, json
from prompt_toolkit import prompt
from prompt_toolkit.document import Document
from prompt_toolkit.validation import Validator, ValidationError

def modifier_mdp(mdp):
    """
    :return: mot de passe modifier 
    """
    mdp = prompt("modifier le mot de passe: ", default=mdp)
    return mdp

def creation_master_password():
    mot_de_passe = prompt("Entré un mot de passe: ", is_password=True)
    if mot_de_passe == "":
        print("Le mot de passe est vide il faut mettre un mot_de_passe")
        mot_de_passe = prompt("Entré un mot de passe: ", is_password=True)

    if len(mot_de_passe) <= 12:
        choix_mdp_faible = input("Votre mot de passe est faible.\n Voulez vous continuer avec un mot de passe faible?(y/n): ")
        if choix_mdp_faible == "n":
            mot_de_passe = modifier_mdp(mot_de_passe)
    mot_de_passe_a_confirmer = prompt("Confirmer le mot de passe: ", is_password=True)

    if mot_de_passe == mot_de_passe_a_confirmer:
        mot_de_passe_confirmer = mot_de_passe
    else:
        valide = False
        while valide is False:
            print("mot de passe")
            mot_de_passe_a_confirmer = input("Confirmer le mot de passe: ")
            if mot_de_passe == mot_de_passe_a_confirmer:
                valide = True
        mot_de_passe_confirmer = mot_de_passe

    return hashlib.sha256(mot_de_passe_confirmer.encode()).hexdigest()

def overture_base_de_donnee(path: str, mot_de_passe_hashed: str, mot_de_passe: str) -> str:
    """
    :param path: Le path vers l'emplacement du vault
    :return: Le mot de passe hashed
    """
    vault = os.path.abspath(path + "/master.json")

    with open(vault, "r") as vault_mdp:
        master_mdp = json.load(vault_mdp)
        
    if master_mdp != mot_de_passe_hashed:
        invalide = True
        while invalide is True:
            print("mot de passe incorect")
            nouv_mdp_entre = prompt("Entré le mot de passe de nouveau: ", is_password=True)
            if master_mdp == hashlib.sha256(nouv_mdp_entre.encode()).hexdigest():
                invalide = False
                return nouv_mdp_entre
    return mot_de_passe
