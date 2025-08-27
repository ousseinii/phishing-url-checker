class UrlAnalyzer:
    def __init__(self, url: str):
        """
        Initialise l'analyseur d'URL.
        
        Args:
            url (str): L'URL à analyser
        """
        self.url = url
        self.score = 0
        self.issues = []

    def check_https(self):
        """Vérifie si l'URL utilise HTTPS, sinon ajoute une issue."""
        if not self.url.startswith("https://"):
            self.issues.append("L'URL n'utilise pas HTTPS")
            self.score += 1

    def check_ip_instead_of_domain(self):
        """Vérifie si l'URL contient une adresse IP au lieu d’un domaine."""
        import re
        ip_pattern = re.compile(r"(\d{1,3}\.){3}\d{1,3}")
        if ip_pattern.search(self.url):
            self.issues.append("L'URL utilise une adresse IP au lieu d'un domaine")
            self.score += 1

    def check_suspicious_words(self):
        """Vérifie si des mots suspects sont présents dans l'URL."""
        from app.utils.helpers import get_suspicious_words
        for word in get_suspicious_words():
            if word in self.url.lower():
                self.issues.append(f"Mot suspect détecté dans l'URL : {word}")
                self.score += 1

    def analyze(self):
        """Lance l’analyse complète de l’URL et met à jour score + issues."""
        self.check_https()
        self.check_ip_instead_of_domain()
        self.check_suspicious_words()
