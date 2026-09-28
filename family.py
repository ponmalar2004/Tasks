


while True:

    print("\n===== FAMILY MEMBER MANAGEMENT =====")
    print("1. Add Member")
    print("2. View Members")
    print("3. Update Member")
    print("4. Delete Member")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter name: ")
        age = input("Enter age: ")
        relation = input("Enter relation: ")

        with open("family.csv", "a") as file:
            file.write(name + "|" + age + "|" + relation + "\n")

        print("Member added successfully!")

    elif choice == "2":

        print("\n===== FAMILY MEMBERS =====")

        with open("family.csv", "r") as file:
            for line in file:
                print(line.strip())

    elif choice == "3":
        members = []

        with open("family.csv", "r") as file:
            for line in file:
                members.append(line.strip())

        name = input("Enter the member name to update: ")

        for i in range(len(members)):

            if name in members[i]:

                new_name = input("Enter new name: ")
                new_age = input("Enter new age: ")
                new_relation = input("Enter new relation: ")

                members[i] = new_name + "|" + new_age + "|" + new_relation

                break

        with open("family.csv", "w") as file:
            for member in members:
                file.write(member + "\n")

        print("Member updated successfully!")


    elif choice == "4":
        members = []

        with open("family.csv", "r") as file:
            for line in file:
                members.append(line.strip())

        name = input("Enter the member name to delete: ")

        for i in range(len(members)):

            if name in members[i]:

                members.pop(i)

                break

        with open("family.csv", "w") as file:
            for member in members:
                file.write(member + "\n")

        print("Member deleted successfully!")

    elif choice == "5":

        print("Program ended!")
        break


    else:

        print("Invalid choice! Please enter 1 to 5.")