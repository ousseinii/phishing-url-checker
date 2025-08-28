from app.core.report import ReportGenerator

def test_safe_report_text():
    report = ReportGenerator(score=0, issues=[], url="https://example.com")
    text = report.generate_report(colored=False)
    assert "SAFE" in text
    assert "Aucune issue détectée" in text

def test_phishing_report_text():
    report = ReportGenerator(score=3, issues=["Fake issue"], url="http://phishing.com")
    text = report.generate_report(colored=False)
    assert "PHISHING" in text
    assert "Fake issue" in text

def test_suspicious_report_text():
    report = ReportGenerator(score=2, issues=["Suspicious word"], url="http://suspicious.com")
    text = report.generate_report(colored=False)
    assert "SUSPICIOUS" in text
    assert "Suspicious word" in text