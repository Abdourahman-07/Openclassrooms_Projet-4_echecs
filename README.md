## Installation

### 1. Créer un environnement virtuel

Ouvrez un terminal dans le dossier du projet et exécutez :

**Windows :**
```Powershell
python -m env env
```

### 2. Activer l'environnement virtuel

**Windows :**
```Powershell
env\Scripts\activate
```

Vous devriez voir `(env)` apparaître au début de la ligne de commande.

### 3. Installer les dépendances

pip install -r requirements.txt

## Utilisation

### Lancer l'application

Exécutez :

python main.py

### Navigation dans l'application

L'application fonctionne via des menus dans la console. Utilisez les chiffres pour naviguer entre les options.

### Attribution des points
- Victoire : 1 point
- Match nul : 0.5 point
- Défaite : 0 point

## Structure des données

Les données sont automatiquement sauvegardées dans le dossier `data/` :

## Génération du rapport flake8

Pour vérifier la conformité du code aux standards PEP 8 et générer le rapport HTML :

```Powershell
flake8 --max-line-length=119 --format=html --htmldir=flake8_rapport
```

Le rapport sera disponible dans le dossier `flake8_rapport/`. Ouvrez le 
fichier `index.html` dans le navigateur pour consulter les résultats.
