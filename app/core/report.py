from colorama import Fore, Style

class ReportGenerator:
    def __init__(self, score, issues, url=None):
        self.score = int(score)
        self.issues = issues
        self.url = url

    def get_verdict(self, colored=True):
        if self.score == 0:
            return (Fore.GREEN + "SAFE" + Style.RESET_ALL) if colored else "SAFE"
        elif 1 <= self.score <= 2:
            return (Fore.YELLOW + "SUSPICIOUS" + Style.RESET_ALL) if colored else "SUSPICIOUS"
        else:
            return (Fore.RED + "PHISHING" + Style.RESET_ALL) if colored else "PHISHING"

    def generate_report(self, colored=True):
        verdict = self.get_verdict(colored=colored)
        report_lines = []

        if self.url:
            report_lines.append(f"🔗 URL analysée : {self.url}")

        report_lines.append("=== Résultat de l'analyse ===")
        report_lines.append(f"Score : {self.score}")
        report_lines.append(f"Verdict : {verdict}")

        if self.issues:
            report_lines.append("\nIssues détectées :")
            for issue in self.issues:
                report_lines.append(f"- {issue}")
        else:
            report_lines.append("Aucune issue détectée ✅")

        return "\n".join(report_lines)
