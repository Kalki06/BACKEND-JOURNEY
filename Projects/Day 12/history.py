def show_history():
    try:
        with open("history.txt", "r") as file:
            content = file.read()
            if(len(content) != 0):
                    print(content)
            else:
                print("There is no history available now. \n ")
    except FileNotFoundError:
         print("There is no such file.\n")
    
def clear_history():
    try:
        with open("history.txt", "w") as file:
             file.write("")
             
    except FileNotFoundError:
        print("There is no such file.\n")
              
