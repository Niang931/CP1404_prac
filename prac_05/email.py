"""estimate:20min
    Actual time:"""

email_to_name ={}
def main():
    email = input("Enter your email:")
    while email != "":
        name = extarct_name(email)
        is_name = input(f'Is this your name? {name}. Y/n:').upper()
        if is_name != "" and is_name != 'Y':
            name = input("Name:")
        email_to_name[email] = name
        email = input("Enter your email:")
    display_user(email_to_name)


def extarct_name(email):
    email_index = email.find('@')
    name = email[:email_index].capitalize()
    if '.' in name:
        name_index = name.find('.')
        name = name[:name_index].capitalize() +' '+ name[name_index+1:].capitalize()
    return name

def display_user(email_to_name):
    for key,item in email_to_name.items():
        print(f"{item} ({key})")

main()