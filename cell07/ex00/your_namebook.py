def array_of_names(persons):
    full_names = []
    for first, last in persons.items():
        full_name = first.capitalize() + " " + last.capitalize()
        full_names.append(full_name)
    return full_names

persons = {
    "alice": "johnson",
    "bob": "smith",
    "carol": "williams",
    "david": "brown",
    "emma": "jones",
    "frank": "miller",
    "grace": "davis",
    "henry": "garcia",
    "isla": "martin",
    "jack": "lee"
}

print(array_of_names(persons))