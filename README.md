## 🪟 Windows (PowerShell)

```powershell
# 1. Clona il repository
git clone https://github.com/R0b3r7R0gu3/Hacking-Tool.git
cd Hacking-Tool

# 2. Crea e attiva l'ambiente virtuale
python -m venv .venv
.\.venv\Scripts\Activate

# 3. Installa le dipendenze
pip install -r requirements.txt

# 4. Avvia il tool
python main.py



## 🐧 Kali Linux

sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git -y

git clone https://github.com/R0b3r7R0gu3/Hacking-Tool.git
cd Hacking-Tool

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
python main.py




## > Termux

pkg update && pkg upgrade -y
pkg install python git -y

git clone https://github.com/R0b3r7R0gu3/Hacking-Tool.git
cd Hacking-Tool

pip install -r requirements.txt
python main.py
