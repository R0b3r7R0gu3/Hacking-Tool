import scapy.all as scapy

# Funzione per sniffare pacchetti
def packet_sniffer():
    def packet_callback(packet):
        print(f"Pacchetto catturato: {packet.summary()}")
    
    print("📡 Sniffer attivo... Premi Ctrl+C per fermarlo.")
    scapy.sniff(prn=packet_callback, store=0)
