# 💰 Simple Banking Program - Tutorial

## 🧩 Étape 1 : Structure du projet

Lorsque vous créez un programme, commencez par le diviser en sections simples que vous pourrez développer une par une. Dans ce tutoriel, nous allons créer les fondations d'une application bancaire en Python.

---

### 📌 Objectif

Créer un squelette fonctionnel d'un programme bancaire simple avec les fonctionnalités suivantes :

1. Afficher le solde
2. Déposer de l'argent
3. Retirer de l'argent
4. Quitter le programme

---

### 🔧 Déclaration des fonctions

On commence par déclarer toutes les fonctions nécessaires :

```python
def show_balance():
    pass  # Placeholder pour afficher le solde

def deposit():
    pass  # Placeholder pour le dépôt

def withdraw():
    pass  # Placeholder pour le retrait
```

### 📦 Variables globales
Nous définissons deux variables principales :

```python
balance = 0
is_running = True  # Utilisé pour savoir quand quitter la boucle principale
```

### 🔁 Boucle principale du programme
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
        withdraw()
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

## 🧩 Étape 2 : Implémentation des fonctions
Dans cette étape, nous allons transformer les fonctions "vides" de l'étape 1 en vraies fonctions fonctionnelles. L'idée est de leur faire effectuer leur rôle (afficher le solde, déposer, retirer), tout en gardant une structure claire, maintenable et sûre.

---
### ⚠️ À faire attention lorsqu'on implémente les fonctions

Voici les points de vigilance à garder à l'esprit pour chaque fonction :

#### 1. `show_balance(balance)`
- ✅ Elle doit afficher correctement le solde actuel.
- 🎯 Attention au format d'affichage : on utilise `:.2f` pour afficher deux décimales même si ce n’est pas obligatoire techniquement, c’est plus propre pour un montant d’argent.

#### 2. `deposit()`
- ✅ Elle demande un montant à l'utilisateur.
- ⚠️ On doit convertir l’entrée utilisateur en float (nombre décimal), ce qui peut causer une erreur si l’utilisateur tape une chaîne invalide (ex : "abc").
- 🔒 Il faut vérifier que le montant est positif. Un dépôt négatif n’a pas de sens : on retourne alors 0 ou on affiche un message d’erreur.

#### 3. `withdraw(balance)`
- ✅ Elle vérifie que le montant à retirer est disponible.
- ⚠️ Deux vérifications importantes :
  - Le montant ne doit pas être supérieur au solde.
  - Le montant ne doit pas être négatif.
- 🔁 Si l’un de ces cas est détecté, on retourne 0 pour éviter que le solde ne soit modifié par erreur.

---

### 🔄 Pourquoi encapsuler le code dans une fonction `main()`

Au lieu d’écrire le code principal directement en dehors de toute fonction, on le place dans une fonction `main()` pour plusieurs raisons :

### ✅ Lisibilité & organisation
- Cela permet de structurer le programme de manière claire : les définitions en haut, la logique principale dans une seule fonction.

### 🔁 Réutilisabilité
- Si ce fichier est importé dans un autre fichier Python, le code ne sera pas exécuté automatiquement. Cela est rendu possible grâce à :

```python
if __name__ == "__main__":
    main()
```

## 🧩 Étape 3 : Input Error Handling & Menu Beautification
Dans cette étape, on améliore deux aspects importants du programme bancaire : la gestion des erreurs d'entrée utilisateur et l'affichage du menu.
---
### ✅ Gestion des entrées utilisateur avec vérification d'erreurs

Au lieu de laisser le programme planter ou se comporter de façon imprévisible en cas de mauvaise saisie, on ajoute :

- Un bloc try/except dans les fonctions deposit() et withdraw() pour intercepter les erreurs de conversion (ex : si l'utilisateur tape "abc" au lieu d’un nombre).
- La possibilité pour l'utilisateur de taper "quit" pour revenir au menu principal sans effectuer d'opération.

➡ Exemple dans deposit() :

```python
user_input = input("Enter an amount to be deposited (or type 'quit' to return): ").strip()
if user_input.lower() == "quit":
    print("Returning to main menu.")
    return 0
try:
    amount = float(user_input)
    ...
except ValueError:
    print("Invalid input.")
    return deposit()
```
### 🧱 Amélioration visuelle : délimitations et mise en forme
Pour rendre l’interface utilisateur plus agréable :

Une fonction add_delimitation() a été ajoutée pour afficher des lignes horizontales (ex : "------------------------------") séparant les différentes sections.
Des titres comme "***** Section Deposit *****" permettent à l’utilisateur de mieux se repérer.
Le menu est indenté avec des tabulations (\t) pour un affichage plus clair.

## Étape 4 (Bonus) : Historique des transactions
