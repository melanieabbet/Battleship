# Description du programme actuel

## 1) Début du jeu

Le joueur commence par saisir son nom et son rôle.

- La saisie du rôle doit être contrôlée dans `terminalHandler.py`.
- Si la saisie est incorrecte : message d'erreur et nouvelle tentative.
- Les choix disponibles **"host"** et **"join"** devraient apparaître.

## 2) Connexion des joueurs (À faire)

(Les adresses IP sont définies par défaut sur la machine pour tester)

- L'adresse IP de l'hôte doit être remontée à l'hôte.
- L'adresse IP doit être demandée au client (avec contrôle de l'entrée -> format IPv4).
- Si le client n'arrive pas à se connecter *n* fois, elle est redemandée.

## 3) Gestion des sockets

Une fois les deux joueurs connectés :

- La socket de l'hôte (serveur) est conservée dans l'instance.
- Celle du client est détruite et sera recréée à chaque dialogue.

## 4) Placement des bateaux

- Lorsqu'un bateau est en train d’être posé, il faudrait voir les coordonnées déjà saisies.

## 5) Premier tir

- Une fois que les coordonnées sont saisies par les deux joueurs :
- Le résultat est retourné sous forme de string.

### **À faire :**
- La grille du joueur doit être mise à jour (voir où l’adversaire a tiré).
- Il faut afficher une nouvelle grille avec les tentatives et résultats des tirs du joueur.
- Il faut tester les conditions de fin de jeu :
  - **Si** *game over* → fin.
  - **Sinon** → nouveau tour.

---

# Notes

- Pour le moment, les "messages" ne sont que des strings.
  - Voir s'il est possible de passer un objet `Coordonnee` et `Content` pour le résultat du tir.
- Il faut ajouter la gestion des erreurs et exceptions côté client et serveur.
- **Si l'application quitte, les sockets doivent être fermées.**
- **Le jeu doit pouvoir être arrêté par le joueur avec "Échap"** :
  - L'information doit être transmise dans le message suivant.
  - Une fois le message transmis, l'application quitte pour les deux joueurs.
