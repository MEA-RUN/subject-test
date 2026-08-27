# Guide Rapide : Match The Shape (Python)

## Objectif

Déplacer **4 formes** jusqu'à leurs **destinations** (formes en contour). Victoire quand toutes les 4 sont sur leurs destinations !

## Créer une Forme

```python
s = shape.Square("red")      # Carré rouge
c = shape.Circle("blue")      # Cercle bleu
t = shape.Triangle("green")   # Triangle vert
```

**Règle** : Maximum 4 formes, pas de doublons (même couleur + même type).

## Commandes Essentielles

```python
s.set_position(2, 3)  # Positionner à (colonne 2, ligne 3)
s.forward(2)          # Avancer de 2 cases
s.backward(1)         # Reculer de 1 case
s.left()              # Tourner à gauche
s.right()             # Tourner à droite
s.get_position()      # Voir la position actuelle
```

## Démarrage Rapide

### Étape 1 : Créer et Positionner

```python
s = shape.Square("red")
s.set_position(1, 1)  # Une destination apparaît automatiquement !
```

### Étape 2 : Se Déplacer

```python
s.forward(1)   # Avance
s.right()      # Tourne
s.forward(2)   # Continue
```

### Étape 3 : Atteindre la Destination

Déplacez la forme jusqu'à ce qu'elle soit exactement sur sa destination (forme en contour).

## Progression

1. **1 forme** : Destination sur la même ligne/colonne (selon direction)
2. **2 formes** : Destinations à max 2 cases
3. **3-4 formes** : Destinations à min 3 cases

## Concepts Appris

### Vocabulaire

- **Variable** : Un nom qui stocke une valeur ou un objet
  - `s = shape.Square("red")` : On stocke un **Objet** (ici un carré rouge) dans une **variable** nommée `s`

- **Méthode** : Une fonction qui modifie ou retourne des informations sur un objet
  - `s.set_position()`, `s.forward()`, etc. : On utilise une **méthode** pour modifier l'**état** de notre **Objet** représenté par la variable `s`

- **Séquence** : Les instructions s'exécutent dans l'ordre

## Astuces

- Commencez avec 1 forme
- Utilisez `shape_entities` pour voir toutes vos formes
- Planifiez votre chemin avant de coder
- Les rotations sont essentielles pour changer de direction
- **Enchaînement de méthodes** : Les méthodes peuvent être enchaînées
  ```python
  s.forward(1).right().forward(2).left().left().backward(1)
  ```

## Exemple Complet

```python
# Créer 4 formes
s = shape.Square("red")
c1 = shape.Circle("blue")
c2 = shape.Circle("green")
t = shape.Triangle("yellow")

# Positionner
s.set_position(0, 0)
c1.set_position(1, 1)
c2.set_position(2, 2)
t.set_position(3, 3)

# Déplacer jusqu'aux destinations
# ... votre code ici ...

# Victoire : "Congratulation !!!" apparaît quand toutes sont arrivées !
```

## Erreurs Courantes

```python
# ❌ Deux cercles bleus
c1 = shape.Circle("blue")
c2 = shape.Circle("blue")

# ✅ Solution : couleurs différentes
c1 = shape.Circle("blue")
c2 = shape.Circle("green")
```

## ⚠️ Avertissement

**Évitez les boucles infinies !** 

Les boucles infinies peuvent faire planter votre navigateur. Ne créez pas de boucles qui ne se terminent jamais, comme :

```python
# ❌ Ne faites pas ça !
while True:
    s.forward(1)
```

Si vous utilisez des boucles, assurez-vous qu'elles ont une condition de sortie claire.

🚀
