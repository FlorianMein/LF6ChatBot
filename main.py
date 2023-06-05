import json
from stichwort import findDepartment, whatistopic

json_path_ans = "answers.json"
level = 0 # Wert auf welcher Anfragestufe sich das System bewegt
department = "" # Das zuständige Department
probleme = [] # Die erfassten Probleme

# Vordefinierte Antworten des Chatbots
# JSON-Datei öffnen und Daten laden
with open(json_path_ans, 'r') as file:
    base_dict = json.load(file)




# Funktion zum Generieren einer Antwort basierend auf der Benutzereingabe
def generiere_antwort(eingabe,stufe):
    if stufe == 0:
        anfrage_department = findDepartment(eingabe,base_dict)
        if anfrage_department == "":
            print("Das habe ich leider nicht verstanden. In welchem unserer Fachbereiche brauchen sie Unterstützung")
        return anfrage_department

    if stufe == 1:
        anfrage_probleme = whatistopic(eingabe,base_dict)
        return anfrage_probleme
        
        

# Funktion zum Starten des Chats
def starte_chat(level: int, base_dict: dict):
    
    # Erste Begrüßung durch den Bot und Hinweise zur Nutzung
    print("Willkommen beim 1st-Level-Support-Chatbot!")
    print("Geben Sie 'Auf Wiedersehen' ein, um den Chat zu beenden.\n")
    print("Starten wir damit, ihr Problem einzugrenzen:\n")
    print("Wenn sie ein Problem im Bereich der Abrechnung haben, schreiben sie bitte Buchhaltung.\n")
    print("Wenn sie ein Problem mit ihrer Hardware haben, schreiben sie bitte Systemintegration.\n")
    print("Wenn sie ein Problem mit ihrem Netzwerk haben, schreiben sie bitte Netzwerkbetreuung.\n")
    print("Wenn sie ein Problem mit einer Software haben, schreiben sie bitte Softwareentwicklung.\n")

    # Start des Bots
    chat_aktiv = True
    while chat_aktiv:
        user_input = input("Nutzer: ")
        user_input = user_input.lower()
        if level == 0 and user_input != "auf wiedersehen":
            department = findDepartment(user_input, base_dict)
            if department == "notFound":
                print("Bitte nutzen sie die vorgegebenen Antwortmöglichkeiten.\n")
            else:
                level = 1
        # antwort = generiere_antwort(user_input,level)
        # print("Chatbot: " + antwort)

        if user_input == "auf wiedersehen":
            print("Auf Wiedersehen")
        
            chat_aktiv = False

starte_chat(level, base_dict)
