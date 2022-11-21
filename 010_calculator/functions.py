def format_name(fname : str, lname : str) -> str:
    return "".join([fname, " ", lname]).title()
# or 
    return f"{fname.capitalize()} {lname.capitalize()}"

def format_name_separately(fname : str, lname : str) -> tuple:
    return fname.title(), lname.title()

print(f"Your name is {format_name(input('Give me your first name: '), input('Give me your surname: '))}")

print(format_name("ota", "kočí"))