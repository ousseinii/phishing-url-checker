class ReportGenerator:
    def __init__(self, url, score, issues):
        self.url = url
        self.score = score
        self.issues = issues

    def generate_report(self):
        if self.score == 0:
            verdict = "SAFE"
        elif self.score <= 2:
            verdict = "SUSPICIOUS"
        else:
            verdict = "PHISHING"

        report_lines = [
            f"=== Analyse de l'URL : {self.url} ===",  # ✅ On affiche l’URL
            f"Score : {self.score}",
            f"Verdict : {verdict}"
        ]

        if self.issues:
            report_lines.append("\nIssues détectées :")
            report_lines.extend([f"- {issue}" for issue in self.issues])
        else:
            report_lines.append("Aucune issue détectée ✅")

        return "\n".join(report_lines)
