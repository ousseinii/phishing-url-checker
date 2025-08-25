from app.core.analyzer import UrlAnalyzer
from app.core.report import ReportGenerator

if __name__ == "__main__":
    test_urls = [
        "https://example.com",
        "http://192.168.0.1/login",
        "https://secure-update.com",
        "http://verify-account.net"
    ]

    for url in test_urls:
        print(f"\nAnalyse de l'URL : {url}")
        analyzer = UrlAnalyzer(url)
        analyzer.analyze()

        report = ReportGenerator(analyzer.score, analyzer.issues)
        report.generate_report()
