from app.core.analyzer import UrlAnalyzer

def test_https_check():
    analyzer = UrlAnalyzer("http://example.com")
    analyzer.check_https()
    assert analyzer.score == 1
    assert "HTTPS" in analyzer.issues[0]

def test_ip_detection():
    analyzer = UrlAnalyzer("http://192.168.1.1")
    analyzer.check_ip_instead_of_domain()
    assert analyzer.score == 1
    assert "adresse IP" in analyzer.issues[0]

def test_suspicious_words():
    analyzer = UrlAnalyzer("https://login-example.com")
    analyzer.check_suspicious_words()
    assert analyzer.score == 1
    assert "login" in analyzer.issues[0]
