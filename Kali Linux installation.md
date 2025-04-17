## 🐧 KALI LINUX
---
### Comandi di installazione:
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
