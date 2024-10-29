import re

def add_items():
    includes = re.split(r'[,]+', (input("Enter items to add: ")))
    for include in includes:
        shopping_list.append(include.strip())
    return shopping_list

def view_list():
    print(shopping_list)
    
def remove_from():
    removals = re.split(r'[,]+', (input("Enter items to remove: ")))
    for removal in removals:
        item = removal.strip()
        if item in shopping_list:
            shopping_list.remove(item)

def save_as():
    # Implement save to file function
    # User chooses file name
    print("List saved!")

def quit_program():
    print("Exiting the program...")
    return True  

ACTIONS = {"a": add_items, "v": view_list, "r": remove_from, "s": save_as, "q": quit_program}
shopping_list = []

def main():
    print("Welcome to your shopping list!")
    while True:
        print("\n'a' = add items | 'v' = view list | 'r' = remove an item | 's' = save | 'q' = quit") 
        menu_choice = input("Choose an action: ")
        
        if menu_choice in ACTIONS:
            if ACTIONS[menu_choice]() == True:
                 break
        else:
            print("Invalid entry")


if __name__ == "__main__":
    main()