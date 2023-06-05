# Gibt zu einem bekannten Problem mögliche Lösungsvorschläge zurück
# Wenn das Problem nicht bekannt ist, wird "notFound" zurückgegeben
def findSolution(string,problemlist):

    topiclist = []
    string = string.lower()
    string = string.replace(" ","")

    for x in problemlist:
        if position != -1:
            topiclist.append(x)
    
    return topiclist

# Gibt die zuständige Abteilung an
# Wenn die keine Abteilung zu dem string existiert, wird "notFound" zurückgegeben
def findDepartment(input : str, departmentlist : dict) -> str:
    input = input.replace(" ","")

    for key in departmentlist:
        if input == key:
            return key

    return "notFound"
    
    
