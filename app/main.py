from app.core.analyzer import UrlAnalyzer
from app.core.report import ReportGenerator
from app.cli.arguments import parse_arguments


def process_url(url):
    analyzer = UrlAnalyzer(url)
    analyzer.analyze()
    report = ReportGenerator(url, analyzer.score, analyzer.issues)  # ✅ on passe aussi l’URL
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

    # Affichage / sauvegarde des résultats
    output_text = "\n\n".join(results)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output_text)
        print(f"✅ Rapport sauvegardé dans {args.output}")
    else:
        print(output_text)
