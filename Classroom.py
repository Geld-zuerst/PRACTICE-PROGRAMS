#                                   ~~~~~~~~~CLASSROOM~~~~~~~~~
info = {
        "Harsh Tiwari" : {
            "Name" : "Harsh Tiwari",
            "Class" : "12th",
            "Academics" : "Harsh is an outstanding student who excels both in academics and sports. Harsh is a talented athlete with remarkable skills in cricket and football."
        },

        "Ankit Dubey" : {
            "Name" : "Ankit Dubey",
            "Class" : "12th",
            "Academics" : "Ankit is an outstanding student who excels both in academics and sports. Ankit is a talented athlete with remarkable skills in cricket and volleyball."
        },

        "Nikhil Tiwari" : {
            "Name" : "Nikhil Tiwari",
            "Class" : "12th",
            "Academics" : "Nikhil is an outstanding student who excels both in academics and sports. Nikhil is a talented athlete with remarkable skills in cricket and football."
        }
    }

# Add info
def add_info():
    pass
# Delete info
def delete_info():
    info.pop(delete)
# Main logic

while True:
    print("\n== Students Details ===")
    print("1 : See Student Informations")
    print("2 : Edit Student Informations")

    choice = input("what u wanna do? ")

    if choice == "1":
        print("\n")
        for key, value in info.items():
            print(f"{key}: {value}")
            print("-" * 40)
    if choice == "2":
        print("\n~~ Editable Options ~~")
        print("1: Add New Student Information")
        print("2: Delete Student Information")
        edit = input("What u wanna do? ")
        if edit == "1":
            add_info()
            print("\n")
            for key, value in info.items():
                print(f"{key}: {value}")
                print("-" * 40)
        if edit == "2":
            for key in info:
                print(key)
            delete = input("Enter full name of student: ")
            delete_info()
            print("\n")
            for key, value in info.items():
                print(f"{key}: {value}")
                print("-" * 40)
