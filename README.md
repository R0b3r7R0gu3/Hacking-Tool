# =========================================
# WINDOWS (PowerShell)
# =========================================
# 1. Clona il repository
git clone https://github.com/R0b3r7R0gu3/Hacking-Tool.git
cd Hacking-Tool

# 2. Crea un ambiente virtuale
python -m venv .venv

# 3. Attiva l’ambiente virtuale
.\.venv\Scripts\Activate.ps1

# 4. Installa le dipendenze
pip install -r requirements.txt

# 5. Avvia lo strumento
python main.py


# =========================================
# KALI LINUX / Debian-based
# =========================================
# 1. Aggiorna il sistema
sudo apt update && sudo apt upgrade -y

# 2. Installa Python e Git
sudo apt install python3 python3-pip git -y

# 3. Clona il repository
git clone https://github.com/R0b3r7R0gu3/Hacking-Tool.git
cd Hacking-Tool

# 4. (Opzionale) Crea e attiva un ambiente virtuale
python3 -m venv .venv
source .venv/bin/activate

# 5. Installa le dipendenze
pip install -r requirements.txt

# 6. Avvia lo strumento
python3 main.py


# =========================================
# TERMUX (Android)
# =========================================
# 1. Aggiorna Termux
pkg update && pkg upgrade -y

# 2. Installa Python e Git
pkg install python git -y

# 3. Clona il repository
git clone https://github.com/R0b3r7R0gu3/Hacking-Tool.git
cd Hacking-Tool

# 4. Installa le dipendenze
pip install -r requirements.txt

# 5. Avvia lo strumento
python main.py


## 🧠 Funzionalità del Tool

Questo tool offre una raccolta di strumenti di sicurezza e monitoraggio:

| Modulo               | Descrizione                                                       |
|----------------------|-------------------------------------------------------------------|
| 🔍 Monitoraggio Sistema  | Mostra CPU, RAM, e processi attivi.                             |
| 🎹 Keylogger            | Registra i tasti premuti in background.                          |
| 🌐 Sniffer di Rete      | Cattura pacchetti sulla rete locale.                             |
| 🔐 Brute Force Login    | Tenta un attacco brute force su login (esempio educational).     |
| 🛡️ Vulnerability Scanner | Scansiona porte e cerca vulnerabilità note.                      |
| 🎣 Simulatore Phishing  | Simula pagine di login per scopi dimostrativi.                   |
| 📡 Cracking Wi-Fi       | Simula il cracking di reti Wi-Fi (funziona solo su Linux root).   |
| 🔏 Monitoraggio Privacy | Verifica la presenza di dati personali esposti online.           |

> ⚠️ **ATTENZIONE:** Questo progetto è solo a scopo didattico. Non usarlo per attività non etiche o illegali.

