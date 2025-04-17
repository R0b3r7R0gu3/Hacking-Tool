import requests

def scan_vulnerabilities():
    url = input("Inserisci URL del sito da scansionare per vulnerabilità: ")
    common_vulns = ["/wp-admin", "/phpmyadmin", "/test", "/login"]

    for vuln in common_vulns:
        vuln_url = url + vuln
        response = requests.get(vuln_url)
        if response.status_code == 200:
            print(f"Vulnerabilità trovata: {vuln_url}")
        else:
            print(f"Nessuna vulnerabilità trovata in: {vuln_url}")
