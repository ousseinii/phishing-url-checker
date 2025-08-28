# 🕵️‍♂️ Phishing Checker

Un outil CLI permettant d’analyser des URLs et de détecter les risques de phishing.  
Le projet a été conçu comme un **mini scanner pédagogique** , avec des fonctionnalités simples mais réalistes.

<p align="center">
  <img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExb3l2azRrNTlhd215NThsYmY1ZWp6Zmt2czJ0aDF0d2J0N2RpM2QxYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/42wQXwITfQbDGKqUP7/giphy.gif" alt="Picachu with magnifying glass"/>
</p>


## 🚀 Fonctionnalités

<ul>
  <li>Analyse d’URLs individuelles ou d’un fichier contenant une liste d’URLs</li>
  <li>Détection de :
    <ul>
      <li>Absence de HTTPS</li>
      <li>Utilisation d’adresse IP au lieu d’un domaine</li>
      <li>Mots suspects (ex: <code>login</code>, <code>secure</code>, <code>verify</code>, <code>update</code>, etc.)</li>
    </ul>
  </li>
  
  <li>Attribution d’un <strong>score de risque</strong> :
  <ul>
      <li>✅ <code>SAFE</code> (score 0)</li>
      <li>⚠️ <code>SUSPICIOUS</code> (score 1–2)</li>
      <li>❌ <code>PHISHING</code> (score ≥ 3)</li>
    </ul>
  </li>
</ul>

<p>Résultats disponibles :</p>
<ul>
  <li><strong>Dans le terminal</strong> (colorés avec <code>colorama</code>)</li>
  <li><strong>Dans un fichier rapport</strong> automatiquement généré dans <code>/reports/</code></li>
</ul>



## 📂 Architecture du projet

```
├── app/                  # Code principal
│   ├── cli/              # Gestion des arguments en ligne de commande
│   │   └── arguments.py
│   ├── core/             # Cœur du projet
│   │   ├── analyzer.py   # Analyse des URLs
│   │   └── report.py     # Génération des rapports
│   ├── utils/            # Fonctions utilitaires
│   │   └── helpers.py    # Liste des mots suspects centralisée
│   └── main.py           # Point d’entrée principal
│
├── tests/                # Tests unitaires avec pytest
│   ├── test_analyzer.py
│   └── test_report.py
│
├── reports/              # Dossiers des rapports générés
│   └── 2025-08-27_04-21-42_rapport.txt
│
├── urls.txt              # Exemple de fichier d’URLs à analyser
├── Dockerfile            # Configuration Docker
├── requirements.txt      # Dépendances (requests, colorama, pytest)
├── README.md             # Documentation du projet
├── LICENSE               # Licence open-source
└── .dockerignore         # Fichiers ignorés par Docker

```

## ⚙️ Installation & Usage
Tout d'abords clonez le projet depuis son repos, puis accédez à la racine du projet.

    git clone https://github.com/ousseinii/phishing-url-checker.git
    
    cd phishing-url-checker/

 1. ### Option 1 : Exécution locale (Python installé)
 Assurez-vous d’avoir **Python 3.11+** installé.
 	
**Sur Windows**

    # Installation des librairies requises
    pip install -r requirements.txt

    # Tester avec une URL. 
	python -m app.main -u https://example.com/{path}
	
	# Tester avec une liste d’URLs (fichier urls.txt)
	python -m app.main -f urls.txt
	
	# Tester avec une liste d’URLs et générer un rapport
	python -m app.main -f urls.txt -o rapport.txt

#### macOS / Linux
    # Installation des librairies requises
    pip3 install -r requirements.txt
	
	# Tester avec une URL. 
	python3 -m app.main -u https://example.com/{path}
	
	# Tester avec une liste d’URLs (fichier urls.txt)
	python3 -m app.main -f urls.txt
	
	# Tester avec une liste d’URLs et générer un rapport
	python3 -m app.main -f urls.txt -o rapport.txt

 2.  ### Option 2 : Exécution via Docker
 Assurez vous d'avoir installer et configurer **Docker** sur votre machine
 
    # Construisez l’image Docker
    docker build -t phishing-checker .
    
    #  Tester avec une URL
	docker run phishing-checker -u https://example.com/{path}
	
	# Tester avec une liste d’URLs (fichier urls.txt)
	docker run -v ${PWD}/urls.txt:/app/urls.txt phishing-checker -f urls.txt
	
	# Tester avec une liste d’URLs et générer un rapport
	docker run -v ${PWD}:/app phishing-checker -f urls.txt -o rapport.txt


💡 **Explication :**
- `{path}` représente le **chemin ou la page spécifique** à tester sur ce domaine.
Par exemple :
	-  `https://example.com/login` → pour tester la page login

	-  `https://example.com/update` → pour tester une page update

💡 `${PWD}` correspond au **répertoire courant**, donc assurez vous d’être dans le dossier du projet quand tu lances ces commandes.

⚡ Chaque exécution avec `-o rapport.txt` crée un **nouveau rapport horodaté** dans le dossier `/reports/`.  
Exemple : `2025-08-27_04-21-42_rapport.txt`


## 📝 Exemple de sortie terminal
	🔗 URL analysée : http://192.168.0.1/login
	=== Résultat de l'analyse ===
	Score : 3
	Verdict : PHISHING
    
	Issues détectées :
	- L'URL n'utilise pas HTTPS
	- L'URL utilise une adresse IP au lieu d'un domaine
	- Mot suspect détecté dans l'URL : login


## 🧪 Tests unitaires
Les tests valident les 2 modules principaux :
-   `UrlAnalyzer` (détection HTTPS, IP, mots suspects)
-   `ReportGenerator` (score, verdict, formatage)

```
# Lancer le test
pytest -v
```

Sortie attendue : ✅ tous les tests passent.

## 📌 Fichiers importants
-  **`urls.txt`** → fichier exemple contenant une liste d’URLs à analyser

-  **`/reports/`** → tous les rapports générés automatiquement avec date/heure

-  **`Dockerfile`** → permet d’utiliser le projet en mode portable avec Docker