"""
Консольний бот-помічник: книга контактів (ім'я -> номер телефону).
Команди: hello, add, change, phone, all, close/exit.
"""


def parse_input(user_input: str) -> tuple[str, ...]:
    parts = user_input.strip().split()
    if not parts:
        return ("",)
    cmd = parts[0].lower()
    return cmd, *parts[1:]


def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    if len(args) != 2:
        return "Invalid command. Use: add <name> <phone>"
    name, phone = args[0], args[1]
    contacts[name] = phone
    return "Contact added."


def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    if len(args) != 2:
        return "Invalid command. Use: change <name> <phone>"
    name, phone = args[0], args[1]
    if name not in contacts:
        return "Contact not found."
    contacts[name] = phone
    return "Contact updated."


def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    if len(args) != 1:
        return "Invalid command. Use: phone <name>"
    name = args[0]
    if name not in contacts:
        return "Contact not found."
    return contacts[name]


def show_all(contacts: dict[str, str]) -> str:
    if not contacts:
        return "No contacts saved."
    lines = [f"{name}: {phone}" for name, phone in contacts.items()]
    return "\n".join(lines)


def main() -> None:
    contacts: dict[str, str] = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break
        if command == "hello":
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
            if command:
                print("Invalid command.")
            else:
                print("Invalid command.")


if __name__ == "__main__":
    main()
