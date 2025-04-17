from tools import system_tools, keylogger, sniffer, brute_force, vuln_scanner, phishing_sim, wifi_cracker, privacy_leak

def menu():
    print("\n🔥 MULTI TOOLBOX 🔥")
    print("1. Monitoraggio Sistema")
    print("2. Keylogger")
    print("3. Sniffer di Rete")
    print("4. Brute Force Login")
    print("5. Vulnerability Scanner")
    print("6. Simulatore di Phishing")
    print("7. Cracking Wi-Fi")
    print("8. Monitoraggio Privacy")
    print("0. Esci")

def system_tools_menu():
    print("\nSistema - Monitoraggio:")
    print("1. Monitoraggio CPU e Memoria")
    print("2. Visualizza Processi Attivi")
    print("0. Indietro")

def brute_force_menu():
    print("\nBrute Force - Login:")
    print("1. Avvia Attacco Brute Force")
    print("0. Indietro")

def wifi_cracker_menu():
    print("\nWi-Fi Cracker:")
    print("1. Avvia Cracking Wi-Fi")
    print("0. Indietro")

def main():
    while True:
        menu()
        scelta = input("Scegli: ")
        
        if scelta == "1":
            system_tools_menu()
            sub_choice = input("Scegli un'opzione: ")
            if sub_choice == "1":
                system_tools.system_monitor()
            elif sub_choice == "2":
                system_tools.show_processes()
            elif sub_choice == "0":
                continue

        elif scelta == "2":
            keylogger.start_keylogger()

        elif scelta == "3":
            sniffer.packet_sniffer()

        elif scelta == "4":
            brute_force_menu()
            sub_choice = input("Scegli un'opzione: ")
            if sub_choice == "1":
                brute_force.brute_force_login()
            elif sub_choice == "0":
                continue

        elif scelta == "5":
            vuln_scanner.scan_vulnerabilities()

        elif scelta == "6":
            phishing_sim.simulate_phishing()

        elif scelta == "7":
            wifi_cracker_menu()
            sub_choice = input("Scegli un'opzione: ")
            if sub_choice == "1":
                wifi_cracker.crack_wifi()
            elif sub_choice == "0":
                continue

        elif scelta == "8":
            privacy_leak.check_data_leaks()

        elif scelta == "0":
            print("Ciao! 👋")
            break

        else:
            print("Scelta non valida.")
if __name__ == "__main__":
    main()
