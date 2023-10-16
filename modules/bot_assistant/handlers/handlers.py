def add_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        contacts[name] = phone
    else:
        return f"Contact {name} already exists."
    return f"Contact {name} added."


def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
    else:
        return f"Contact {name} doesn't exist."
    return f"Contact {name} changed."


def get_contact_phone(args, contacts):
    name = args[0]
    if name not in contacts:
        return f"Contact {name} doesn't exist."
    return f"Phone: {contacts[name]}"


def get_all_contacts(contacts):
    if not contacts:
        return "You don't have any contacts."
    return "".join([f"{name} - {phone}\n" for name, phone in contacts.items()])
