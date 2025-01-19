def parse_input(user_input):
    """
    Розбирає введений рядок на команду та аргументи.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    """
    Додає новий контакт до словника.
    """
    if len(args) != 2:
        return "Error: Please provide both a name and a phone number."
    
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added with phone {phone}."

def change_contact(args, contacts):
    """
    Змінює номер телефону для існуючого контакту.
    """
    if len(args) != 2:
        return "Error: Please provide both a name and a new phone number."
    
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return f"Contact {name} updated with new phone {new_phone}."
    else:
        return f"Error: Contact {name} not found."

def show_phone(args, contacts):
    """
    Показує номер телефону для вказаного контакту.
    """
    if len(args) != 1:
        return "Error: Please provide exactly one name."
    
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        return f"Error: Contact {name} not found."

def show_all(contacts):
    """
    Показує всі контакти зі збереженими номерами.
    """
    if not contacts:
        return "No contacts found."
    
    result = "All contacts:"
    for name, phone in contacts.items():
        result += f"\n{name}: {phone}"
    return result

def main():
    """
    Головна функція для роботи бота.
    """
    contacts = {}  # Словник для зберігання контактів
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ").strip()
        if not user_input:
            continue
        
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))
        
        elif command == "change":
            print(change_contact(args, contacts))
        
        elif command == "phone":
            print(show_phone(args, contacts))
        
        elif command == "all":
            print(show_all(contacts))
        
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

 
 