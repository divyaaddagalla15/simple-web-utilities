import random

def get_motivation():
    quotes = [
        "Code is like humor. When you have to explain it, it’s bad.",
        "First, solve the problem. Then, write the code.",
        "Programmer: A machine that turns coffee into code.",
        "Software and cathedrals are much the same – first we build them, then we pray."
    ]
    
    print("\n--- Daily Dev Quote ---")
    print(random.choice(quotes))
    print("-----------------------\n")

get_motivation()
