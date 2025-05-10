# 💰 Simple Banking Program - Tutorial

## 🧩 Étape 1 : Structure du projet

Lorsque vous créez un programme, commencez par le diviser en sections simples que vous pourrez développer une par une. Dans ce tutoriel, nous allons créer les fondations d'une application bancaire en Python.

---

## 📌 Objectif

Créer un squelette fonctionnel d'un programme bancaire simple avec les fonctionnalités suivantes :

1. Afficher le solde
2. Déposer de l'argent
3. Retirer de l'argent
4. Quitter le programme

---

## 🔧 Déclaration des fonctions

On commence par déclarer toutes les fonctions nécessaires :

```python
def show_balance():
    pass  # Placeholder pour afficher le solde

def deposit():
    pass  # Placeholder pour le dépôt

def withdrawal():
    pass  # Placeholder pour le retrait
```

## 📦 Variables globales
Nous définissons deux variables principales :

```python
balance = 0
is_running = True  # Utilisé pour savoir quand quitter la boucle principale
```

## 🔁 Boucle principale du programme
Nous allons créer une boucle principale qui s'exécute tant que l'utilisateur ne demande pas de quitter :

```python
while is_running:
    print("Banking program")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        show_balance()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdrawal()
    elif choice == '4':
        is_running = False  # Quitter la boucle
    else:
        print("That is not a valid choice")
```
💡 Remarque : la fonction main() n’est pas encore utilisée. Elle pourra être ajoutée à la fin pour encapsuler tout le programme.

À ce stade, vous avez :
- Les fonctions déclarées (même si elles sont encore vides)
- La logique de menu en boucle avec des entrées utilisateur
- Un système de contrôle de flux simple avec des conditions

La prochaine étape consiste à implémenter le contenu des fonctions show_balance, deposit et withdrawal.

## 🧩 Étape 2 : Titre ? 
