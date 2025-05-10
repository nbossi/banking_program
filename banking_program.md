# Tutoriel : Création d'un programme bancaire simple

## Étape 1 : Structure de base du programme

### Principe clé
Divisez toujours un projet complexe en petites sections gérables. Nous allons :
1. Déclarer d'abord toutes les fonctions nécessaires
2. Définir les variables globales
3. Implémenter la logique principale

### Code de base

```python
# simple_banking.py
# Fonctions principales du programme bancaire

def show_balance(balance):
    """Affiche le solde actuel"""
    print(f"Votre solde est de : ${balance:.2f}")

def deposit(balance):
    """Gère les dépôts d'argent"""
    amount = float(input("Montant à déposer : $"))
    return balance + amount

def withdraw(balance):
    """Gère les retraits d'argent"""
    amount = float(input("Montant à retirer : $"))
    if amount > balance:
        print("Fonds insuffisants !")
        return balance
    return balance - amount

# Variables globales
balance = 0.0
is_running = True

### Menu principal
while is_running:
    print("\n" + "="*20)
    print("  Programme Bancaire")
    print("="*20)
    print("1. Afficher le solde")
    print("2. Effectuer un dépôt")
    print("3. Effectuer un retrait")
    print("4. Quitter")

    choice = input("Votre choix (1-4) : ")

    if choice == '1':
        show_balance(balance)
    elif choice == '2':
        balance = deposit(balance)
    elif choice == '3':
        balance = withdraw(balance)
    elif choice == '4':
        is_running = False
        print("Merci d'avoir utilisé notre service bancaire !")
    else:
        print("Choix invalide. Veuillez entrer un nombre entre 1 et 4.")



  