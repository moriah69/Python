import pyttsx3
import os

print(" I can open applications for you!")
print(" Some of the applications that I can open for you are:")
print(" ~ Calculator")
print(" ~ Browser")
print(" ~ Text Editor")
print(" ~ Media Player")
print(" and some other more!")
print()

pyttsx3.speak("Welcome to my small menu program.")

while True:
    print(" Requirements: ", end='')
    a =input()

    if ("do not" in a) or ("dont" in a) or ("don't" in a):
        print("Okay!")

    elif  ("exit" in a)  or ("quit" in a) or ("leave" in a):
        break

    elif (("open" in a) or ("run" in a) or ("launch" in a) or ("execute" in a)) and ("browser" in a):
        print(" 1. Firefox")
        print(" 2. Chrome")
        print(" 3. Opera")
        print()

        while True:
            print("Please choose a browser: ",end='')
            chck = input()

            if ((("open" in chck) or ("run" in chck) or ("launch" in chck) or ("execute" in chck)) and ("firefox" in chck)) or ("1" in chck):
                c = os.system("firefox")

                if(c == 0):
                    break
                else:
                    print(" Sorry!!Firefox is not installed on your system.")

            elif ((("open" in chck) or ("run" in chck) or ("launch" in chck) or ("execute" in chck)) and ("chrome" in chck)) or ("2" in chck):
                c = os.system("chrome")

                if(c == 0):
                    break
                else:
                    print(" Sorry!!Chrome is not installed on your system.")

            elif (("open" in chck) or ("run" in chck) or ("launch" in chck) or ("execute" in chck)) and (("opera" in chck)) or ("3" in chck):
                c = os.system("opera")

                if(c == 0):
                    break
                else:
                    print(" Sorry!!Opera Browser is not installed on your system.")
            elif (("exit" in chck) or ("close" in chck)):
                break

            elif (("open" in a) or ("run" in a) or ("launch" in a) or ("execute" in a)):
                print("Sorry! Your Instruction was unclear. Please repeat.")

    elif (("open" in a) or ("run" in a) or ("launch" in a) or ("execute" in a)) and (("firefox" in a) or ("chrome" in a)):
        os.system("firefox")

    elif (("open" in a) or ("run" in a) or ("launch" in a) or ("execute" in a)) and ("chrome" in a):
        os.system("chrome")

    elif (("open" in a) or ("run" in a) or ("launch" in a) or ("execute" in a)) and (("editor" in a)):
            print(" 1. Notepad")
            print(" 2. Sublime")
            print(" 3. Atom")
            print()

            while True:
                print("Please choose a text editor: ",end='')
                chck = input()

                if ((("open" in chck) or ("run" in chck) or ("launch" in chck) or ("execute" in chck)) and ("notepad" in chck)) or ("1" in chck):
                    os.system("notepad")
                    break

                elif ((("open" in chck) or ("run" in chck) or ("launch" in chck) or ("execute" in chck)) and ("sublime" in chck)) or ("2" in chck):
                    c = os.system("sublime_text")

                    if(c == 0):
                        break
                    else:
                        print(" Sorry!!Sublime is not installed on your system.")

                elif ((("open" in chck) or ("run" in chck) or ("launch" in chck) or ("execute" in chck)) and ("atom" in chck)) or ("3" in chck):
                    c = os.system("atom")

                    if(c == 0):
                        break
                    else:
                        print(" Sorry!!Atom is not installed on your system.")
                elif (("exit" in chck) or ("close" in chck)):
                    break

                elif (("open" in a) or ("run" in a) or ("launch" in a) or ("execute" in a)):
                    print("Sorry! Your Instruction was unclear. Please repeat.")

    elif (("open" in a) or ("run" in a) or ("launch" in a) or ("execute" in a)) and (("notepad" in a)):
            os.system("notepad")

    elif (("open" in a) or ("run" in a) or ("launch" in a) or ("execute" in a)) and (("atom" in a) or ("3" in a)):
        c = os.system("atom")

    elif (("open" in a) or ("run" in a) or ("launch" in a) or ("execute" in a)) and (("sublime" in a) or ("2" in a)):
        c = os.system("sublime_text")

    elif (("open" in a) or ("run" in a) or ("launch" in a) or ("execute" in a)) and (("calculator" in a) or ("calc" in a)):
        os.system("calc")

    elif (("open" in a) or ("run" in a) or ("launch" in a) or ("execute" in a)) and (("window media player" in a) or ("media player" in a)):
        os.system("wmplayer")

    elif (("open" in a) or ("run" in a) or ("launch" in a) or ("execute" in a)) and (("vlc" in a)):
        os.system("vlc")

    elif ("open" in a) or ("run" in a) or ("launch" in a) or ("execute" in a):
        print("Sorry! Your Instruction was unclear. Please repeat.")
