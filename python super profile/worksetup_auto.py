import webbrowser as wb 
import os 

def workauto():
    codepath= "C:/Program Files/VirtualDJ/virtualdj.exe"
    os.startfile(codepath)
    Chrome_path= "C:/ProgramData/Microsoft/Windows/Start Menu/Programs/msedge.exe %s"
    URLS= ( "https://gmail.com", "https://google.com", "https://youtube.com", "https://github.com")
    
    # for url in URLS:
    #     print (url)
    #     wb.get(Chrome_path).open(url)
    #     wb.open_new_tab(url)

    # url = input("Enter name of the website ")
    print ("Hello programmers ")

workauto()
