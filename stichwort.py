


# gibt eine Liste aus mit möglichen Problemen
def whatistopic(string : str ,department:str ,problemlist:dict):

    topiclist = []
    string = string.lower()
    string = string.replace(" ","")
    
    key_list = problemlist[department]
    for x in key_list:
        # Methode find()
        position = string.find(x)
        if position != -1:
            topiclist.append(x)

    if topiclist == []:
        return "notFound"
    
    return topiclist

# gibt die Zuständige abteilung an
def findDepartment(input : str, departmentlist : dict) -> str:
    input = input.replace(" ","")

    for key in departmentlist:
        if input == key:
            return key

    return "notFound"
    
