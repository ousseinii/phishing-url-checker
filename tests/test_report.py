from app.core.report import ReportGenerator

def test_safe_report():
    report = ReportGenerator(0, [], "https://example.com")
    result = report.generate_report()
    assert "SAFE" in result

def test_phishing_report():
    issues = ["L'URL n'utilise pas HTTPS", "Mot suspect détecté dans l'URL : login"]
    report = ReportGenerator(3, issues, "http://192.168.1.1/login")
    result = report.generate_report()
    assert "PHISHING" in result
    assert "login" in result
