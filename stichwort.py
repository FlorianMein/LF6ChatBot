<<<<<<< HEAD



# gibt eine Liste aus mit möglichen Problemen
def whatistopic(string : str ,department:str ,problemlist:dict):
=======
# Gibt zu einem bekannten Problem mögliche Lösungsvorschläge zurück
# Wenn das Problem nicht bekannt ist, wird "notFound" zurückgegeben
def findSolution(string,problemlist):
>>>>>>> 586d31a859aef987a7f66b6fa11d159af02e0476

    topiclist = []
    string = string.lower()
    string = string.replace(" ","")
<<<<<<< HEAD
    
    key_list = problemlist[department]
    for x in key_list:
        # Methode find()
        position = string.find(x)
=======

    for x in problemlist:
>>>>>>> 586d31a859aef987a7f66b6fa11d159af02e0476
        if position != -1:
            topiclist.append(x)

    if topiclist == []:
        return "notFound"
    
    return topiclist

# Gibt die zuständige Abteilung an
# Wenn die keine Abteilung zu dem string existiert, wird "notFound" zurückgegeben
def findDepartment(input : str, departmentlist : dict) -> str:
    input = input.replace(" ","")

    for key in departmentlist:
        if input == key:
            return key

    return "notFound"
    
    
