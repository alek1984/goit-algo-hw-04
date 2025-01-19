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
        
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
 