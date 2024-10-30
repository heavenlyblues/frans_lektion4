import re
import os

shopping_list = []

def add_items():
    includes = re.split(r'[,]+', (input("Enter items to add: ")))
    for include in includes:
        item = include.strip()
        if item:
            shopping_list.append(item)

def view_list():
    if not shopping_list:
        print("Nothing on the list yet!")
    else: 
        for item in shopping_list:
            print(f"• {item}")
        print("\n")
    
def remove_items():
    removals = re.split(r'[,]+', (input("Enter items to remove: ")))
    for removal in removals:
        item = removal.strip()
        if item in shopping_list:
            shopping_list.remove(item)

def load_list():
    global shopping_list
    print("\nAvailable Shopping Lists:")
    for item in os.listdir():
        if os.path.isdir(item) and not item.startswith('.'):
            folder_name = item
            print(f"{folder_name}/")
            for file in os.listdir(folder_name): 
                if os.path.isfile(os.path.join(folder_name, file)):
                    print(f" -- {file}")
            
    path_and_file = input("File to load: ").strip().lower()
    try:
        temp_list = []
        with open (path_and_file, "r") as file:
            for row in file:
                item = row.strip()
                temp_list.append(item)
        if shopping_list:
            while True:
                new_or_combine = input("Combine lists [Y/n]? ").strip().lower()
                if new_or_combine == "y":
                    shopping_list.extend(temp_list)
                    print(f"'{path_and_file}' loaded and combined with current list.")
                    break
                elif new_or_combine == "n":
                    shopping_list = temp_list
                    print(f"Current list cleared. '{path_and_file}' opened and loaded.")
                    break
                else:
                    print("Invalid entry. Please enter 'y' for 'YES' or 'n' for 'NO'.")
        else:
            shopping_list = temp_list
            print(f"'{path_and_file}'ist opened and loaded.")

        return shopping_list
    
    except FileNotFoundError:
        print("Error: The specified file was not found.")

def save_as():
    global shopping_list
    filename = input("Save file as: ").strip().lower()
    directory = input("Create directory: ").strip().lower()
    
    os.makedirs(directory, exist_ok=True)

    with open(f"{directory}/{filename}", "w") as file:
        for item in shopping_list:
            file.write(f"{item}\n")
            
    print(f"File '{filename}' saved in '{directory}/'")

def help_commands():
    print("| a = add item(s) | v = view list | r = remove item(s) | o = load list | s = save as | q = quit |") 

def quit_program():
    print("Exiting the program...")
    return False  

ACTIONS = {
    "a": add_items, 
    "v": view_list, 
    "r": remove_items, 
    "o": load_list, 
    "s": save_as, 
    "help": help_commands, 
    "q": quit_program
}

def main():
    print("\nWelcome to your shopping list!")
    print("(Type 'help' for a list of commands)\n")

    while True:
        menu_choice = input("Choose an action: ").strip().lower()
        
        if menu_choice in ACTIONS:
            if ACTIONS[menu_choice]() == False:
                 break
        else:
            print("Invalid entry")


if __name__ == "__main__":
    main()