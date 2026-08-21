# Exercices sur les commandes VS Code

> Dans cet exercice, vous devez utiliser les raccourcis et commandes pour répondre aux questions suivantes.

Si vous n'êtes pas encore familier avec les commandes VS Code, allez dans le playground interactif (palette de commandes, entrez `playground`) ou voir les notes de cours : https://app.gitbook.com/o/qWn6Tbh1thQPZRNnvYTk/s/t7y2VZ521uD26unwRYFw/outils-et-environnement-de-developpement/vs-code

## 1. Auto-formatage

1. Le code fourni est mal formaté. Suivez les étapes des notes de cours pour configurer Ruff et activer le formatage automatique à la sauvegarde : https://app.gitbook.com/o/qWn6Tbh1thQPZRNnvYTk/s/t7y2VZ521uD26unwRYFw/outils-et-environnement-de-developpement/vs-code#auto-formattage-avec-ruff

## 2. Renommage (F2)

2. Dans `main.py`, renommez la variable `h` en `heure_actuelle` avec `F2`. Vérifiez qu'aucun autre fichier n'a changé.
3. Depuis sa définition dans `distributeur_iot/distributeur.py`, renommez la méthode `rapport` en `afficher_rapport` avec `F2`. Vérifiez que `main.py` s'est mis à jour automatiquement.

## 3. Multi-curseur

4. Dans `main.py`, à l'aide du multi-curseur, ajoutez `# ` devant les constantes `SEUIL_BAS`, `HEURE_MATIN` et `HEURE_MIDI` en même temps.
5. Dans `distributeur_iot/capteurs.py`, sélectionnez toutes les occurrences de `valeur_min` pour les renommer en `valeur_minimale` simultanément.

## 4. Recherche dans tous les fichiers

6. Ouvrez la recherche globale et cherchez `activer`. Combien de fichiers contiennent ce mot ?

## 5. Pliage de code

7. Dans `distributeur_iot/distributeur.py`, pliez uniquement la méthode `verifier_distribution`.
8. Utilisez la palette de commandes pour exécuter **Fold All**, puis **Unfold All**.