import random
import time
import sys
import os
from colorama import Fore, Style, init
import pyfiglet

init()

# Liste de SNI
sni_list = [
    "www.netflix.com",
    "play.google.com",
    "www.instagram.com",
    "cdn.cloudflare.net",
    "discord.com",
    "update.android.com"
]

# Affichage du logo principal
def afficher_logo():
    os.system("clear")
    logo = pyfiglet.figlet_format("SOLITAIRE HACK")
    print(Fore.CYAN + logo)
    print(Fore.GREEN + Style.BRIGHT + "     SNI Generator – By Solitaire\n")

afficher_logo()

# Effet de chargement
def loading_animation(text="Génération en cours"):
    for i in range(3):
        sys.stdout.write(Fore.BLUE + f"\r{text}" + "." * (i + 1) + " " * (3 - i))
        sys.stdout.flush()
        time.sleep(0.5)
    print()

# Générer un seul SNI
def generate_sni():
    loading_animation()
    sni = random.choice(sni_list)
    print(Fore.YELLOW + "[+] Generated SNI: " + Fore.CYAN + sni + "\n")

# Générer plusieurs SNIs
def generate_multiple_sni():
    count = int(input(Fore.LIGHTBLUE_EX + "Combien de SNIs veux-tu générer ? "))
    loading_animation("Préparation")
    for _ in range(count):
        sni = random.choice(sni_list)
        print(Fore.YELLOW + " - " + Fore.CYAN + sni)

# Sauvegarder dans un fichier
def save_to_file():
    filename = input(Fore.LIGHTBLUE_EX + "Nom du fichier (ex: snis.txt) : ")
    with open(filename, "w") as f:
        for sni in sni_list:
            f.write(sni + "\n")
    print(Fore.GREEN + f"[✓] Sauvegardé dans {filename}\n")

# Menu À propos avec voix française
def afficher_about():
    os.system("clear")
    os.system('espeak -v fr "Je suis Solitaire Hack. Le hacking c\'est une bonne chose, surtout quand tu le fais pour le bien de l\'humanité."')
    logo = pyfiglet.figlet_format("ABOUT")
    print(Fore.CYAN + logo)

    print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "    Je suis SOLITAIRE HACK")
    print(Fore.YELLOW + Style.BRIGHT + "    LE HACKING C'EST UNE BONNE CHOSE")
    print(Fore.YELLOW + Style.BRIGHT + "    SURTOUT QUAND TU LE FAIS POUR LE BIEN DE L'HUMANITÉ\n")

    print(Fore.LIGHTMAGENTA_EX + "    Version : 1.0")
    print(Fore.LIGHTBLUE_EX + "    Projet  : Générateur de SNI pour Termux")
    print(Fore.LIGHTWHITE_EX + "\n    Appuie sur Entrée pour revenir au menu...")
    input()
    afficher_logo()

# Boucle principale
while True:
    print(Fore.MAGENTA + "\n1 - Générer un SNI")
    print("2 - Générer plusieurs SNIs")
    print("3 - Sauvegarder dans un fichier")
    print("4 - Quitter")
    print("5 - À propos")
    choix = input(Fore.WHITE + "\nChoix: ")

    if choix == "1":
        generate_sni()
    elif choix == "2":
        generate_multiple_sni()
    elif choix == "3":
        save_to_file()
    elif choix == "4":
        print(Fore.RED + "Fermeture...")
        break
    elif choix == "5":
        afficher_about()
    else:
        print(Fore.RED + "Choix invalide !")