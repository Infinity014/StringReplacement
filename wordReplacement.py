def selectAndGenerate():
    choice = input("Enter [s] for string and [f] for file: ")
    
    if (choice.lower() == 's'):
        string  = input("Enter the statement: ")
        word_to_replace = input("Enter the word to replace: ")
        wrd = input("Enter the word replacement: ")
        return(string.replace(word_to_replace, wrd))
        
    elif(choice.lower() == 'f'):
        fileName = input("Enter the file name: ")
        f = open(fileName,'r')
        contents = f.read()
        word_to_replace = input("Enter the word to replace: ")
        wrd = input("Enter the word replacement: ")
        return(contents.replace(word_to_replace,wrd))

    else:
        return("There was a error please look at what to input")

print(selectAndGenerate())