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

print(creation_master_password())
