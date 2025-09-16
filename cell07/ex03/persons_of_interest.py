def famous_births(people):
    sorted_people = sorted(people.values(), key=lambda x: int(x["date_of_birth"]))
    
    for person in sorted_people:
        print(f"{person['name']} is a great scientist born in {person['date_of_birth']}.")

famous_scientists = {
    "jane": { "name": "Jane Goodall", "date_of_birth": "1934" },
    "marie": { "name": "Marie Curie", "date_of_birth": "1867" },
    "rosalind": { "name": "Rosalind Franklin", "date_of_birth": "1920" },
    "barbara": { "name": "Barbara McClintock", "date_of_birth": "1902" },
    "mae": {"name": "Mae Jemison", "date_of_birth": "1956" }
}

famous_births(famous_scientists)
