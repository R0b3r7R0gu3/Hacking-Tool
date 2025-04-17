import requests

def check_data_leaks():
    email = input("Inserisci la tua email per controllare le perdite di dati: ")
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"

    headers = {"User-Agent": "PrivacyLeakScanner"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        breaches = response.json()
        if breaches:
            print("I seguenti data breaches sono stati trovati per la tua email:")
            for breach in breaches:
                print(f"- {breach['Name']}")
        else:
            print("Nessun data breach trovato.")
    else:
        print("Errore nel controllare i breach.")
