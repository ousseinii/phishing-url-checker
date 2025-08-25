class ReportGenerator:
    def __init__(self, score, issues):
        self.score = score
        self.issues = issues

    def get_verdict(self):
        if self.score == 0:
            return "SAFE"
        elif 1 <= self.score <= 2:
            return "SUSPICIOUS"
        else:
            return "PHISHING"

    def generate_report(self):
        verdict = self.get_verdict()
        print("\n=== Résultat de l'analyse ===")
        print(f"Score : {self.score}")
        print(f"Verdict : {verdict}")
        if self.issues:
            print("\nIssues détectées :")
            for issue in self.issues:
                print(f"- {issue}")
        else:
            print("Aucune issue détectée ✅")
