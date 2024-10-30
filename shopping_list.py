import re
from pathlib import Path

def add_items():
    includes = re.split(r'[,]+', (input("Enter items to add: ")))
    for include in includes:
        item = include.strip()
        if item:
            shopping_list.append(item)

def view_list():
    print(shopping_list)
    
def remove_items():
    removals = re.split(r'[,]+', (input("Enter items to remove: ")))
    for removal in removals:
        item = removal.strip()
        if item in shopping_list:
            shopping_list.remove(item)

def load_list():
    filename = input("File to open: ")
    # check_input = filename.strip().split()
    # if check_input[-2] == "."
    #     filename = filename.pop(-2, 1)
    with open (f"shopping_lists/{filename}", "r") as file:
        for row in file:
            item = row.strip()
            shopping_list.append(item)
    print("List opened and loaded.")
    return shopping_list

def save_as():
    filename = input("Save file as: ")
    with open(f"shopping_lists/{filename}", "w") as file:
        for item in shopping_list:
            file.write(f"{item}\n")

    # Implement save to file function
    # User chooses file name
    print("List saved!")

def quit_program():
    print("Exiting the program...")
    return True  

ACTIONS = {"a": add_items, "v": view_list, "r": remove_items, "o": load_list, "s": save_as, "q": quit_program}
shopping_list = []

def main():
    print("Welcome to your shopping list!")
    while True:
        print("\n'a' = add items | 'v' = view list | 'r' = remove an item | 'o' = open txt file | 's' = save txt file | 'q' = quit") 
        menu_choice = input("Choose an action: ")
        
        if menu_choice in ACTIONS:
            if ACTIONS[menu_choice]() == True:
                 break
        else:
            print("Invalid entry")


if __name__ == "__main__":
    main()