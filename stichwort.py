


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
def whatisdepartment(string,departmentlist):
    department = ""
    string = string.lower()
    string = string.replace(" ","")

    for x in departmentlist:
        # Methode find()
        position = string.find(str(x))
        if position != -1:
            department = str(x)
    
    return department