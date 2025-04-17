import os
import socket
import requests
import dns.resolver
from bs4 import BeautifulSoup
import whois

# ========== IP / URL / DNS Lookup ==========
def lookup():
    target = input("Inserisci IP o dominio: ")
    try:
        print(f"\n🔍 Lookup per {target}")
        ip = socket.gethostbyname(target)
        print("IP Address:", ip)

        # IPINFO
        ipinfo = requests.get(f"https://ipinfo.io/{ip}/json").json()
        for k, v in ipinfo.items():
            print(f"{k.capitalize()}: {v}")

        # WHOIS
        print("\n📄 WHOIS:")
        w = whois.whois(target)
        print(f"Domain: {w.domain_name}")
        print(f"Registrar: {w.registrar}")
        print(f"Creation Date: {w.creation_date}")
        print(f"Expiration Date: {w.expiration_date}")
    except Exception as e:
        print("Errore nel lookup:", e)

# ========== Port Scanner ==========
def port_scanner():
    target = input("Inserisci IP o host: ")
    ports = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3306, 8080, 3389]
    print("🔎 Scansione porte comuni...")

    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Porta {port}: OPEN")
            sock.close()
        except Exception as e:
            print(f"Errore su porta {port}: {e}")

# ========== Subdomain Finder ==========
def subdomain_finder():
    domain = input("Dominio principale: ")
    wordlist = ["www", "mail", "ftp", "cpanel", "webmail", "admin", "test", "dev"]
    found = []

    print("🔎 Ricerca sottodomini...")

    for sub in wordlist:
        subdomain = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(subdomain)
            print(f"[✓] {subdomain} --> {ip}")
            found.append(subdomain)
        except:
            pass

    if not found:
        print("Nessun sottodominio trovato.")

# ========== Host Discovery (Ping Sweep) ==========
def ping_sweep():
    base_ip = input("Inserisci rete (es: 192.168.1): ")

    print(f"📡 Scansione dispositivi attivi in {base_ip}.0/24")

    for i in range(1, 255):
        ip = f"{base_ip}.{i}"
        response = os.system(f"ping -c 1 -W 1 {ip} > /dev/null 2>&1")
        if response == 0:
            print(f"[+] Host attivo: {ip}")
