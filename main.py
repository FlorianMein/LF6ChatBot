import json
from stichwort import findDepartment, findproblem

json_path_ans = "answers.json"
level = 0 # Wert auf welcher Anfragestufe sich das System bewegt
department = "" # Das zuständige Department
probleme = [] # Die erfassten Probleme

chat_arichv = []

# Vordefinierte Antworten des Chatbots
# JSON-Datei öffnen und Daten laden
with open(json_path_ans, 'r') as file:
    base_dict = json.load(file)



# Funktion zum Generieren einer Antwort basierend auf der Benutzereingabe
def generiere_antwort(eingabe,department,stufe):
    if stufe == 0:
        anfrage_department = findDepartment(eingabe,base_dict)
        if anfrage_department == "":
            print("Das habe ich leider nicht verstanden. In welchem unserer Fachbereiche brauchen sie Unterstützung")
        return anfrage_department

    if stufe == 1:
        anfrage_probleme = findproblem(eingabe,department,base_dict)
        return anfrage_probleme
        
# Funktion zum dump eines Chatverlaufs in eine Datenbank
def arichv_chat_to_db(chatlog: list):
    print("Ihre Daten werrden zu verbesserung des Service gespecihert, wenn sie etwas dagen haben schreiben sie jetzt \n Nein" )
    user_input = input("Ja/Nein")
    if user_input != "Nein":
        print("Ihre daten helfen uns diesen Service zu verbessern")
        #Data Dump

# Funktion zum Starten des Chats
def starte_chat(level: int, base_dict: dict):

    # Erste Begrüßung durch den Bot und Hinweise zur Nutzung
    print("Chatbot: " + "Willkommen beim 1st-Level-Support-Chatbot! \n")
    print("Chatbot: " + "Mit der Ntzung dieses Servies stimmen sie unserer Datenschutzvereinbarung zu  diese finden sie unter 'URL' \n"+ "Geben Sie 'Auf Wiedersehen' ein, um den Chat zu beenden.\n"+ "Starten wir damit, ihr Problem einzugrenzen:\n"+ "Starten wir damit, ihr Problem einzugrenzen:\n"+ "Wenn sie ein Problem im Bereich der Abrechnung haben, schreiben sie bitte Buchhaltung.\n"+ "Wenn sie ein Problem mit ihrer Hardware haben, schreiben sie bitte Systemintegration.\n"+ "Wenn sie ein Problem mit ihrem Netzwerk haben, schreiben sie bitte Netzwerkbetreuung.\n"+ "Wenn sie ein Problem mit ihrem Netzwerk haben, schreiben sie bitte Netzwerkbetreuung.\n"+ "Wenn sie ein Problem mit einer Software haben, schreiben sie bitte Softwareentwicklung.\n")


    # Start des Bots
    chat_aktiv = True
    while chat_aktiv:
        user_input = input("Nutzer: ")
        chat_arichv.append(user_input)
        user_input = user_input.lower()


        if level == 0 and user_input != "auf wiedersehen":
            department = findDepartment(user_input, base_dict)
            if department == "notFound":
                print("Chatbot: " + "Bitte nutzen sie die vorgegebenen Antwortmöglichkeiten.\n")
            else:
                print("Chatbot: " + "Was ist ihr genaues Problem?")
                level = 1
                user_input = input("Nutzer: ")
        
        if level == 1 and user_input != "auf wiedersehen":
            antwort = findproblem(user_input,department,base_dict)
            if antwort == "notFound":
                print("Chatbot: " + "Wir haben keine Lösung für ihr Problem .\n")
            else:
                antwort = findproblem(user_input,department,base_dict)
                chat_arichv.append(antwort)  # Chat wird für spätere nutzung gespeichert 
                antwort_list = []
                for problem in antwort:
                    for id in base_dict[department][problem]:
                        antwort_list.append(id)
            

                for solution in antwort_list:
                    print("Chatbot: " + solution)
                    user_input = input("Konnte ich ihnen weiter helfen: (Ja/Nein)")
                    if user_input == "ja":
                        print("Auf Wiedersehen")
                        chat_aktiv = False
                        break
                if chat_aktiv != False:    
                    print("Chatbot: " +"Entschuldigen sie das ich ihnen nicht helfen konnte bitte wenden sie sich an "+ department)
                    chat_aktiv = False
                    break
        if user_input == "auf wiedersehen":
            print("Auf Wiedersehen")
            chat_aktiv = False
            break

starte_chat(level, base_dict)





#Test
#for x in range(len(base_dict["netzwerkbetreuung"]["langsame internetverbindung"])):
#    print(base_dict["netzwerkbetreuung"]["langsame internetverbindung"][x])
