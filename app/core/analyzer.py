import re
from urllib.parse import urlparse
from app.utils.helpers import get_suspicious_words

class UrlAnalyzer:
    def __init__(self, url: str):
        self.url = url
        self.issues = []
        self.score = 0

    # Vérifie si l'URL utilise HTTPS
    def check_https(self):
        if not self.url.startswith("https://"):
            self.issues.append("L'URL n'utilise pas HTTPS")
            self.score += 1

    # Vérifie si l'URL contient une adresse IP au lieu d'un domaine
    def check_ip_in_url(self):
        parsed = urlparse(self.url)
        domain = parsed.netloc

        if re.match(r"^\d{1,3}(\.\d{1,3}){3}$", domain):  # regex IPv4 simple
            self.issues.append("L'URL utilise une adresse IP au lieu d'un domaine")
            self.score += 1
    
    # Vérifie si l'URL contient des mots suspects
    def check_suspicious_words(self):
        for word in get_suspicious_words():
            if word in self.url.lower():
                self.issues.append(f"Mot suspect détecté dans l'URL : {word}")
                self.score += 1
    
    # Exécute toutes les vérifications
    def analyze(self):
        self.check_https()
        self.check_ip_in_url()
        self.check_suspicious_words()

        return {
            "url": self.url,
            "score": self.score,
            "issues": self.issues,
        }