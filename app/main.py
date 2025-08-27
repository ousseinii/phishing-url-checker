import os
from datetime import datetime
from app.core.analyzer import UrlAnalyzer
from app.core.report import ReportGenerator
from app.cli.arguments import parse_arguments

def process_url(url):
    analyzer = UrlAnalyzer(url)
    analyzer.analyze()
    # score, issues, puis url (respect de l’ordre dans ReportGenerator)
    report = ReportGenerator(analyzer.score, analyzer.issues, url)
    return report.generate_report()

if __name__ == "__main__":
    args = parse_arguments()
    results = []

    # Cas 1 : une seule URL
    if args.url:
        results.append(process_url(args.url))

    # Cas 2 : fichier d’URLs
    elif args.file:
        try:
            with open(args.file, "r") as f:
                urls = [line.strip() for line in f.readlines() if line.strip()]
                for url in urls:
                    results.append(process_url(url))
        except FileNotFoundError:
            print(f"❌ Erreur : fichier {args.file} introuvable")
            exit(1)
    else:
        print("❌ Veuillez fournir une URL (-u) ou un fichier (-f). Utilisez -h pour l’aide.")
        exit(1)

    # Préparation du rapport
    output_text = "\n\n".join(results)

    # Cas 1 : sauvegarde dans un fichier avec timestamp
    if args.output:
    # Créer un dossier reports si besoin
        os.makedirs("reports", exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filepath = os.path.join("reports", f"{timestamp}_{args.output}")

        with open(filepath, "w", encoding="utf-8") as f:
            # Générer le texte sans couleur
            plain_results = []
            for url in urls:  # urls venant de fichier ou args.url
                analyzer = UrlAnalyzer(url)
                analyzer.analyze()
                report = ReportGenerator(analyzer.score, analyzer.issues, url)
                plain_results.append(report.generate_report(colored=False))
            f.write("\n\n".join(plain_results))

        print(f"✅ Rapport sauvegardé dans {filepath}")
    # Cas 2 : affichage console
    else:
        print(output_text)
