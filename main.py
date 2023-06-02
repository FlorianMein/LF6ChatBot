import json
import stichwort

json_path_ans = "answers.json"
anfrage_level = 0 # Wert auf welcher Anfragestufe sich das System bewegt
anfrage_department = "" #Das zuständige Department
anfrage_probleme = [] #Die erfassten Probleme

# Vordefinierte Antworten des Chatbots
# JSON-Datei öffnen und Daten laden
with open(json_path_ans, 'r') as file:
    antworten = json.load(file)




# Funktion zum Generieren einer Antwort basierend auf der Benutzereingabe
def generiere_antwort(eingabe,stufe):
    if stufe == 0:
        anfrage_department = stichwort.whatisdepartment(eingabe,antworten)
        if anfrage_department == "":
            print("Das habe ich leider nicht verstanden. In welchem unserer Fachbereiche brauchen sie Unterstüzung")
        return anfrage_department

    if stufe == 1:
        anfrage_probleme = stichwort.whatistopic(eingabe,antworten)
        return anfrage_probleme
        
        

# Funktion zum Starten des Chats
def starte_chat():
    print("Willkommen beim 1st-Level-Support-Chatbot!")
    print("Geben Sie 'Auf Wiedersehen' ein, um den Chat zu beenden.\n")
    print("Wie kann ich ihnen weiterhelfen?\n")

    chat_aktiv = True
    while chat_aktiv:
        benutzereingabe = input("Benutzereingabe: ")
        antwort = generiere_antwort(benutzereingabe,anfrage_level)
        print("Chatbot: " + antwort)

        if benutzereingabe == "Auf Wiedersehen":
            print("Auf wiedersehen")
        
            chat_aktiv = False

starte_chat()
