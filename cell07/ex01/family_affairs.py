def find_the_redheads(family):
    redheads = list(filter(lambda name: family[name] == "red", family))
    return redheads

dupont_family = {
    "Junjan": "red",
    "Tatar": "blond",
    "Bambam": "brown",
    "Aof": "brunette",
    "JumpJump": "red",
    "PamPam": "red"
}

print(find_the_redheads(dupont_family))