import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Phishing URL Checker - Analyze URLs for suspicious patterns."
    )

    # Argument pour une seule URL
    parser.add_argument(
        "-u", "--url",
        type=str,
        help="Single URL to analyze"
    )

    # Argument pour un fichier d’URLs
    parser.add_argument(
        "-f", "--file",
        type=str,
        help="Path to a file containing multiple URLs"
    )

    # Argument pour fichier de sortie (optionnel)
    parser.add_argument(
        "-o", "--output",
        type=str,
        help="Optional output file to save the report"
    )

    return parser.parse_args()
