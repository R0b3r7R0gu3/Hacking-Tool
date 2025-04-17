import subprocess

def crack_wifi():
    wifi_name = input("Inserisci il nome della rete Wi-Fi (SSID): ")
    password_list = ["123456", "password", "qwerty", "admin"]

    print("Inizio cracking della rete Wi-Fi...")
    for password in password_list:
        
        subprocess.run(command, shell=True)

        command = f"airmon-ng start wlan0"
        subprocess.run(command, shell=True)

        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        if "Key Found" in result.stdout:
            print(f"Password trovata: {password}")
            break
        else:
            print(f"Password tentata: {password} - Non corretta")
