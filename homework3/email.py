def is_valid_email(email):
    if '@' in email and '.' in email:
        return True
    else:
        return False

user_email = input("Enter an email please: ")

if is_valid_email(user_email):
    print("YES")
else:
    print("NO")
