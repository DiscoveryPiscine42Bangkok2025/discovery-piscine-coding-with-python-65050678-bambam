def greetings(name="noble stranger"): 
    if isinstance(name, str):            
        print(f"Hello, {name}.")
    else:
        print("Error! It was not a name.")
    
greetings("Bambam")
greetings("Pam")
greetings("Tatar")
greetings("Jumpjump")
greetings()
greetings(600000) 