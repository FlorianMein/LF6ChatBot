import json
import mysql.connector
from jinja2 import Environment, PackageLoader, select_autoescape
from datetime import date

json_path_ans = "answers.json" # Pfad zur json Datei mit vorgefertigten Antworten-
level = 0 # Wert auf welcher Anfragestufe sich das System bewegt

# Vordefinierte Antworten des Chatbots
# JSON-Datei öffnen und Daten laden
with open(json_path_ans, 'r') as file:
    base_dict = json.load(file)

# Erstellen des Archivtexts für die DB 
def append_archiv(archiv : str, text : str):
    new_archiv = ""
    if archiv == "":
        new_archiv = text
    else:
        new_archiv = archiv + " || " + text
    
    return new_archiv

# Gibt eine Liste aus mit möglichen Problemen
def find_problem(string : str, department : str, problemdict : dict):

    topiclist = []
    string = string.replace(" ","")
    
    key_list = problemdict[department]
    for x in key_list:
        position = string.find(x)
        if position != -1:
            topiclist.append(x)

    if topiclist == []:
        return "notFound"
    
    return topiclist

# Gibt die zuständige Abteilung an
# Wenn die keine Abteilung zu dem string existiert, wird "notFound" zurückgegeben
def find_department(input : str, departmentlist : dict) -> str:
    input = input.replace(" ","")

    for key in departmentlist:
        if input == key:
            return key

    return "notFound"
        
# Funktion zum Dump eines Chatverlaufs in eine Datenbank
def archiv_chat_to_db(chatlog: list, dep_id : int):
    # Öffnen der Connection zur DB
    connector = mysql.connector.connect(host="localhost", user="root", password="", database="solutions_it_support")
    cursor = connector.cursor()

    # Laden und rendern der SQL Templates
    env = Environment(loader=PackageLoader('templates', 'templates'), autoescape=select_autoescape())
    insert_template = env.get_template("insert.sql")

    datum = date.today()

    print("Ihre Daten werden zur Verbesserung des Service gespeichert. Wenn Sie etwas dagegen haben schreiben Sie jetzt \n Nein" )
    user_input = input("(Ja/Nein) ")
    if user_input != "Nein":
        print("Ihre Daten helfen uns diesen Service zu verbessern.")
        # Insert in die Datenbank
        cursor.execute(insert_template.render(datum=datum, abteilung_id=dep_id, chatlog=chatlog))
        connector.commit()

        # Schließen der Connection
        cursor.close()
        connector.close()

# Abfrage der jeweiligen Abteilungs-ID aus der DB
def get_dep_id(department : str):
    # Öffnen der Connection zur DB
    connector = mysql.connector.connect(host="localhost", user="root", password="", database="solutions_it_support")
    cursor = connector.cursor()
    
    # Laden der SQL Templates
    env = Environment(loader=PackageLoader('templates', 'templates'), autoescape=select_autoescape())
    dep_id_template = env.get_template("dep_id.sql")

    # Abfrage in der DB
    cursor.execute(dep_id_template.render(department=department))
    dep_id = cursor.fetchall()
    dep_id = dep_id[0][0]

    # Schließen der Connection
    cursor.close()
    connector.close()

    return dep_id

# Abfrage der Kontaktdaten einer Abteilung aus der DB
def get_dep_contact(dep_id: int):
    # Öffnen der Connection zur DB
    connector = mysql.connector.connect(host="localhost", user="root", password="", database="solutions_it_support")
    cursor = connector.cursor()
    
    # Laden der SQL Templates
    env = Environment(loader=PackageLoader('templates', 'templates'), autoescape=select_autoescape())
    dep_id_template = env.get_template("dep_contact.sql")

    # Abfrage in der DB
    cursor.execute(dep_id_template.render(dep_id=dep_id))
    dep_contact = cursor.fetchall()

    
    # Schließen der Connection
    cursor.close()
    connector.close()

    return dep_contact


# Funktion zum Starten des Chats
def starte_chat(level: int, base_dict: dict):
    chat_archiv = ""

    # Erste Begrüßung durch den Bot und Hinweise zur Nutzung
    print("Chatbot: " + "Willkommen beim 1st-Level-Support-Chatbot! \n")
    print("Chatbot: " + "Mit der Nutzung dieses Servies stimmen Sie unserer Datenschutzvereinbarung zu. Diese finden Sie unter 'URL' \n"+ "Geben Sie 'Auf Wiedersehen' ein, um den Chat zu beenden.\n"+ "Starten wir damit, ihr Problem einzugrenzen:\n"+ "Wenn Sie ein Problem im Bereich der Abrechnung haben, schreiben Sie bitte Buchhaltung.\n"+ "Wenn Sie ein Problem mit ihrer Hardware haben, schreiben Sie bitte Systemintegration.\n"+ "Wenn Sie ein Problem mit ihrem Netzwerk haben, schreiben Sie bitte Netzwerkbetreuung.\n"+ "Wenn Sie ein Problem mit einer Software haben, schreiben Sie bitte Softwareentwicklung.\n")

    # Start des Bots
    chat_aktiv = True
    while chat_aktiv:
        user_input = input("Nutzer: ").lower()
        chat_archiv = append_archiv(chat_archiv, user_input)

        # Auf Level 0 soll festgestellt werden, in welcher der Abteilungen das Problem liegt
        if level == 0 and user_input != "auf wiedersehen":
            department = find_department(user_input, base_dict)
            dep_id = get_dep_id(department)
            if department == "notFound":
                print("Chatbot: " + "Bitte nutzen Sie die vorgegebenen Antwortmöglichkeiten.\n")
            else:
                print("Chatbot: " + "Was ist ihr genaues Problem?")
                level = 1
                user_input = input("Nutzer: ").lower()
                chat_archiv = append_archiv(chat_archiv, user_input)

        # Auf Level 1 wird das konkrete Problem in der jeweiligen Abteilung gesucht
        if level == 1 and user_input != "auf wiedersehen":
           
            # Im letzten Input wird geguckt, ob das Problem bereits bekannt ist
            antwort = find_problem(user_input,department,base_dict)
            if antwort == "notFound":
                # Ist das Problem nicht bekannt, wird an weiteren Support verwiesen...
                contacts = get_dep_contact(dep_id)[0]
                print("Chatbot: Entschuldigen Sie, dass ich ihnen nicht helfen konnte. Bitte wenden Sie sich an die Abteilung %s unter %s oder per Telefon unter %s" % (department.capitalize(), contacts[0], contacts[1]))
                # und potentiell ein DB-Eintrag erstellt
                archiv_chat_to_db(chat_archiv, dep_id)
                print("Chatbot: " + "Haben Sie ein weiteres Problem in diesem Bereich? Ansonsten beenden Sie den Chat mit: Auf Wiedersehen")
            else:
                # Ist das Problem bekannt, werden die möglichen Lösungen ausgegeben
                antwort_list = []
                for problem in antwort:
                    for id in base_dict[department][problem]:
                        antwort_list.append(id)
            
                for solution in antwort_list:
                    print("Chatbot: " + solution)
                    chat_archiv = append_archiv(chat_archiv, solution)
                    user_input = input("Konnte ich ihnen weiter helfen: (Ja/Nein) ")
                    chat_archiv = append_archiv(chat_archiv, user_input)
                    if user_input == "ja":
                        print("Auf Wiedersehen")
                        chat_aktiv = False
                        break
                # Sollte keine funktionierende Lösung dabei gewesen sein, wird an die jeweilige Abteilung verwiesen
                if chat_aktiv != False:
                    contacts = get_dep_contact(dep_id)[0]
                    print("Chatbot: Entschuldigen Sie, dass ich ihnen nicht helfen konnte. Bitte wenden Sie sich an die Abteilung %s unter %s oder per Telefon unter %s" % (department.capitalize(), contacts[0], contacts[1]))
                    archiv_chat_to_db(chat_archiv, dep_id)
                    chat_aktiv = False
                    break
        # Ende des Chats
        if user_input == "auf wiedersehen":
            print("Auf Wiedersehen")
            chat_aktiv = False
            break

starte_chat(level, base_dict)