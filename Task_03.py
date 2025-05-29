contacts={}

while True:
    choice = input("Enter your Choice [Add/Delete/update/search/exit]\n :")
    choice = choice.lower()

    if choice == "add":
        name = str(input("Enter your Name :"))
        name=name.lower()
        number = input("Enter your Number :")
        contacts[name] = number
        print(f"contact{name} added sucessfully ✅")
        print(contacts)
    elif choice == "delete":
        name = input("Enter your name :").lower()
        if name in contacts:
            del contacts[name]
            print(f"Contact{name} Deleted Sucessfully ")
            print(contacts)
        else :
            print("Contact not fount ❌")
    elif choice == "update":
        name = input("Enter the name you want to update :").lower()
        if name in contacts:
            number = input("Enter your number :")
            contacts[name] = number
            print(contacts)
        else :
            print("Contact not found ❌")
    elif choice == "search":
        name = input("Enter your name :").lower()
        if name in contacts:
            print(f"The {name} contact number is {contacts[name]}")
        else :
            print("Contact not Found ❌")
    elif choice == "exit":
        print("Good bye ....")
        break
    else:
        print("Invalid choice ❌.Try again...")


