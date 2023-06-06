# Gibt eine Liste aus mit möglichen Problemen
def findproblem(string : str, department : str, problemdict : dict):

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
def findDepartment(input : str, departmentlist : dict) -> str:
    input = input.replace(" ","")

    for key in departmentlist:
        if input == key:
            return key

    return "notFound"
    
    
