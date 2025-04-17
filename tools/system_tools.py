import psutil
import platform

# ========== Monitoraggio del Sistema ==========
def system_monitor():
    print(f"\n🔧 Sistema: {platform.system()} {platform.release()}")
    print(f"CPU Usage: {psutil.cpu_percent()}%")
    print(f"RAM Usage: {psutil.virtual_memory().percent}%")
    print(f"Spazio Disco: {psutil.disk_usage('/').percent}%")
    print("\nProcessi attivi:")
    
    # Visualizza i primi 5 processi
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            print(f"{proc.info['name']} - PID: {proc.info['pid']} - CPU: {proc.info['cpu_percent']}% - Memoria: {proc.info['memory_percent']}%")
        except psutil.NoSuchProcess:
            pass

# ========== Task Killer (per terminare un processo) ==========
def kill_process():
    pid = input("Inserisci il PID del processo da terminare: ")
    try:
        proc = psutil.Process(int(pid))
        proc.terminate()
        print(f"Processo {pid} terminato con successo.")
    except psutil.NoSuchProcess:
        print("Processo non trovato.")
