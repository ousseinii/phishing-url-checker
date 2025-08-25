from core.analyzer import UrlAnalyzer


def main():
    # 🔹 Test avec une URL en dur
    url = "http://192.168.1.1/login"
    analyzer = UrlAnalyzer(url)
    result = analyzer.analyze()

    print("\n--- Résultat de l'analyse ---")
    print(f"URL : {result['url']}")
    print(f"Score : {result['score']}")
    print("Problèmes détectés :")
    for issue in result["issues"]:
        print(f" - {issue}")


if __name__ == "__main__":
    main()
