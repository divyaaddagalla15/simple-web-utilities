def check_security():
    print("--- Password Security Scanner ---")
    pwd = input("Enter a password to test: ")
    
    length = len(pwd) >= 8
    has_number = any(char.isdigit() for char in pwd)
    
    if length and has_number:
        print("Result: STRONG ✅")
    elif length:
        print("Result: MEDIUM (Add a number) ⚠️")
    else:
        print("Result: WEAK (Too short) ❌")

check_security()
