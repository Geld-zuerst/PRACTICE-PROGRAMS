# ~~~~~~~~~CLASSROOM~~~~~~~~~

info = {
    "Harsh Tiwari": {
        "Name": "Harsh Tiwari",
        "Class": "12th",
        "Academics": "Harsh is an outstanding student who excels both in academics and sports. Harsh is a talented athlete with remarkable skills in cricket and football."
    },

    "Ankit Dubey": {
        "Name": "Ankit Dubey",
        "Class": "12th",
        "Academics": "Ankit is an outstanding student who excels both in academics and sports. Ankit is a talented athlete with remarkable skills in cricket and volleyball."
    },

    "Nikhil Tiwari": {
        "Name": "Nikhil Tiwari",
        "Class": "12th",
        "Academics": "Nikhil is an outstanding student who excels both in academics and sports. Nikhil is a talented athlete with remarkable skills in cricket and football."
    }
}

# Add info
# Add info
def add_info():
    print("\n===== ADD NEW STUDENT =====")

    name = input("Enter Student Name: ")
    student_class = input("Enter Class: ")
    academics = input("Enter Academics Description: ")

    info[name] = {
        "Name": name,
        "Class": student_class,
        "Academics": academics
    }

    print(f"\n{name} has been added successfully!")

# Delete info
def delete_info(name):
    if name in info:
        info.pop(name)
        print("\nStudent deleted successfully!")
    else:
        print("\nStudent not found!")

# Main Logic

while True:
    print("\n========== CLASSROOM ==========")
    print("1 : See Student Informations")
    print("2 : Edit Student Informations")
    print("3 : Exit")

    choice = input("\nWhat do you want to do? ")

    if choice == "1":
        print("\n===== STUDENT DETAILS =====")
        for key, value in info.items():
            print(f"{key}:")
            print(value)
            print("-" * 40)

    elif choice == "2":
        print("\n~~ Editable Options ~~")
        print("1 : Add New Student Information")
        print("2 : Delete Student Information")

        edit = input("What do you want to do? ")

        if edit == "1":
            add_info()

            print("\n===== UPDATED DETAILS =====")
            for key, value in info.items():
                print(f"{key}:")
                print(value)
                print("-" * 40)

        elif edit == "2":
            print("\nAvailable Students:")
            for key in info:
                print("-", key)

            delete = input("\nEnter full name of student: ")
            delete_info(delete)

            print("\n===== UPDATED DETAILS =====")
            for key, value in info.items():
                print(f"{key}:")
                print(value)
                print("-" * 40)

        else:
            print("\nInvalid edit option!")

    elif choice == "3":
        print("\nThank you for using the Classroom Management System.")
        print("Goodbye! 👋")
        break

    else:
        print("\nInvalid choice! Please enter 1, 2, or 3.")
