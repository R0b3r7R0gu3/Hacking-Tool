import smtplib
from email.mime.text import MIMEText

def simulate_phishing():
    target_email = input("Inserisci l'email target per il phishing: ")
    subject = "Attenzione! Verifica il tuo account"
    body = "Clicca sul link per aggiornare il tuo account: http://phishingsite.com"
    
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = "admin@phishingsite.com"
    msg["To"] = target_email

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("admin@phishingsite.com", "yourpassword")
        server.sendmail("admin@phishingsite.com", target_email, msg.as_string())
        server.quit()
        print("Email di phishing inviata!")
    except Exception as e:
        print(f"Errore nell'invio dell'email: {e}")
