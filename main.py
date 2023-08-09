ADDRESSBOOK = {}

def input_error(wrap):
    def inner(*args):
        try:
            return wrap(*args)
        except IndexError:
            return "Give me name and phone please"
        except KeyError:
            return "Contact not found. Please enter a valid name."
        except ValueError:
            return "Invalid input. Please enter a valid name and phone number."
    return inner

@input_error
def add_handler(name, phone):
    name = name.title()
    ADDRESSBOOK[name] = phone
    return f"Contact {name} with phone {phone} saved"


def exit_handler(*args):
    return "Good bye"

def enter_handler(*args):
    return "How can I help you?"

@input_error
def change_phone(name, phone):
    ADDRESSBOOK[name] = phone
    return f"Phone number for contact {name} has been updated to {phone}."

@input_error
def get_phone(name):
    return f"The phone number for contact {name} is {ADDRESSBOOK[name]}."

def show_all_contacts():
    if not ADDRESSBOOK:
        return "No contacts found."

    result = "Addressbook:\n"
    for name, phone in ADDRESSBOOK.items():
        result += f"{name}: {phone}\n"
    return result

def command_parser(raw_str: str):
    elements = raw_str.split()
    for func, keys in COMMANDS.items():
        if elements[0].lower() in keys:
            return func, elements[1:]

    return None, []

COMMANDS = {
    add_handler: ["add", "+"],
    exit_handler: ["good bye", "close", "exit"],
    enter_handler: ["hello"],
    change_phone: ["change"],
    show_all_contacts: ["show", "show all", "show all contacts"],
    get_phone: ["get", "get phone"]
}


def main():
    while True:
        user_input = input(">>> ")
        if not user_input:
            continue
        func, data = command_parser(user_input)

        if func:
            if func == show_all_contacts:
                result = func()
            else:
                result = func(*data)
            print(result)
            if func == exit_handler:
                break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()