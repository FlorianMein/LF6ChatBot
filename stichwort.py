


# gibt eine Liste aus mit möglichen Problemen
def whatistopic(string,problemlist):

    topiclist = []
    string = string.lower()
    string = string.replace(" ","")

    for x in problemlist:
        # Methode find()
        position = string.find(x)
        if position != -1:
            topiclist.append(x)
    
    return topiclist

# gibt die Zuständige abteilung an
def findDepartment(input : str, departmentlist : dict) -> str:
    input = input.replace(" ","")

    for key in departmentlist:
        if input == key:
            return key

    return "notFound"
    
