## 🛠️ Installazione

---

### 🪟 Windows (PowerShell)

```powershell
# 1. Installa Python (se non già presente):
#    Scaricalo da https://www.python.org/downloads/ e segui le istruzioni.

# 2. Clona il repository:
git clone https://github.com/R0b3r7R0gu3/Hacking-Tool.git
cd Hacking-Tool

# 3. Crea un ambiente virtuale:
python -m venv .venv

# 4. Attiva l'ambiente virtuale:
.\.venv\Scripts\Activate

# 5. Installa le dipendenze:
pip install -r requirements.txt

# 6. (Solo se necessario) Installa manualmente psutil:
pip install psutil

# 7. Avvia il tool:
python main.py

---
## 🐧 KALI LINUX

# 1. Installa Python, pip e Git:
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git -y

# 2. Clona il repository:
git clone https://github.com/R0b3r7R0gu3/Hacking-Tool.git
cd Hacking-Tool

# 3. Crea un ambiente virtuale:
python3 -m venv .venv

# 4. Attiva l'ambiente virtuale:
source .venv/bin/activate

# 5. Installa le dipendenze:
pip install -r requirements.txt

# 6. (Solo se necessario) Installa manualmente psutil:
pip install psutil

# 7. Avvia il tool:
python main.py

---

## >_ TERMUX

# 1. Installa Python e Git:
pkg update && pkg upgrade -y
pkg install python git -y

# 2. Clona il repository:
git clone https://github.com/R0b3r7R0gu3/Hacking-Tool.git
cd Hacking-Tool

# 3. (Opzionale) Crea un ambiente virtuale:
#    pkg install python-virtualenv -y
#    virtualenv .venv
#    source .venv/bin/activate

# 4. Installa le dipendenze:
pip install -r requirements.txt

# 5. (Solo se necessario) Installa manualmente psutil:
pip install psutil

# 6. Avvia il tool:
python main.py

---

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

