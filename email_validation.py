def validate_email(email):

    # Remove extra spaces
    email = email.strip()

    # Convert to lowercase
    email = email.lower()

    # Check for spaces
    if " " in email:
        return False

    # Check @
    if "@" not in email:
        return False

    # @ should appear only once
    if email.count("@") != 1:
        return False

    # Split email
    username, domain = email.split("@")

    # Username should not be empty
    if username == "":
        return False

    # Domain should contain .
    if "." not in domain:
        return False

    # Domain should not start or end with .
    if domain.startswith(".") or domain.endswith("."):
        return False

    # Extension should contain at least 2 characters
    extension = domain.split(".")[-1]

    if len(extension) < 2:
        return False

    return True


email = input("Enter your email: ")

if validate_email(email):
    print("Valid Email ")
else:
    print("Invalid Email ")
