# WH, SH, JQ 2nd

from will_code_rpg import character_creator

characters = dict()

races = {
    "human": (1,1,1,1,1,1,1,1,1,1)
}
classes = {
    "human": (1,1,1,1,1,1,1,1,1,1)
}

def main_menu():
    while True:
        match input("Do you want to (as a number).\n1: Make a character \n2: Edit a character \n3: Compare a character \n4: Exit\n").strip():
            case "1":
                character_creator(races,classes,characters)
            case "2":
                ediding_menu()
            case "3":
                pass
            case "4":
                break
            case _:
                pass

def ediding_menu():
    while True:
        if characters == {}:
            print("no characters.")
            break
        else:
            match input("Do you want to (as a number).\n1: Edit a character \n2: Edit a character \n3: Edit a character \n4: Exit\n").strip():
                case "1":
                    pass
                case "2":
                    pass
                case "3":
                    pass
                case "4":
                    break
                case _:
                    pass
main_menu()