# Documentation de l'API Bbox Bouygues Telecom

Voir https://teuze.github.io/posts/bbox pour l'article complet.

## Démarrage rapide

```shell
# Installation de mitmproxy
python3 -m pip install mitmproxy

# Récupération du projet
git clone https://github.com/Teuze/bbox
cd bbox

# Lancement d'un reverse proxy vers la box (bypass CORS)
mitmdump -s script.py --mode reverse:https://mabbox.bytel.fr

# Lancement du projet
python3 -m http.server
```

Il ne reste plus qu'à visiter l'adresse http://localhost:8000/ pour interagir avec l'API.
