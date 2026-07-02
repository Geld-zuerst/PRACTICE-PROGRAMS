class School:
    def __init__(self, RRHS):
        self.School = RRHS 

    def info(self, Name):
        self.name = Name

    def Class(self, Class, Roll_no):
        self.Class = Class
        if self.Class > 12 or self.Class <= 0:
            print("You entered invalid format")
        else:
            print(f"Welcome {self.name} from class {self.Class}th in {self.School}")

        self.roll_no = Roll_no
        print("----------------------------------------------------------------------")

    def more_info(self):
        options = {"1" : "See Information",
                   "2" : "See Academics"
            }
        self.Harsh = "His father's name is ABC and mother's name is DEF. He is from Rohtas, Bihar."
        self.Nikhil = "His father's name is MNO and mother's name is PQR. He is from Patna, Bihar."
        self.Ankit = "His father's name is GHI and mother's name is KLM. He is from Arrah, Bihar."


        self.Harsh_info = "He have a Very Good Academics. He scored 95% in 8th, 97% in 9th or 93% in pre boards. Harsh is an outstanding student who excels both in academics and sports. He consistently performs well in all subjects, showing a strong grasp of concepts and a disciplined approach to learning. His curiosity and active participation in class make him a valuable asset to the academic environment. In addition to his academic achievements, Harsh is a talented athlete with remarkable skills in cricket, basketball, and football. He has represented his house in multiple inter-house competitions and brought home several medals and trophies. Harsh exemplifies a perfect balance between academics and extracurricular excellence, making us proud as an institution."
        self.Nikhil_info = "Nikhil is a sincere and academically strong student who consistently performs well in his studies. He has shown a keen interest in subjects like Mathematics and Science, often going beyond classroom learning to explore concepts deeply. His discipline, punctuality, and dedication make him a role model for his peers. While academics remain his strong suit, Nikhil also participates in sports and physical activities. Though he maintains an average performance in sports, he displays good team spirit and willingness to improve. With the right balance, Nikhil continues to grow as a well-rounded student both in academics and extracurricular areas."
        self.Ankit_info = "Ankit is a bright and dedicated student who has consistently performed well in his academics. He demonstrates a clear understanding of subjects and approaches his studies with focus and sincerity. His disciplined nature and positive attitude make him a respected member of the classroom. Beyond academics, Ankit stands out as an exceptional cricket player. His performance on the field is commendable, and he has brought great pride to the school with his talent and sportsmanship. Balancing both studies and sports with excellence, Ankit is a fine example of an all-rounder and continues to inspire his peers with his achievements."
    

        operation = input(f"Enter what you want to see? \n{options} ").strip()

        if operation == "1":
            if self.name == "Harsh":
                print(f"\nAbout Harsh: {self.Harsh}")
            elif self.name == "Nikhil":
                print(f"\nAbout Nikhil: {self.Nikhil}")
            elif self.name == "Ankit":
                print(f"\nAbout Ankit: {self.Ankit}")
            else:
                print("\nInvalid information about student")
        elif operation == "2":
            if self.name == "Harsh":
                print(f"\nAcademics profile of Harsh: {self.Harsh_info}")
            elif self.name == "Nikhil":
                print(f"\nAcademics profile of Nikhil: {self.Nikhil_info}")
            elif self.name == "Ankit":
                print(f"\nAcademics profile of Ankit: {self.Ankit_info}")
            else:
                print("\nInvalid information about student")

S1 = School("RRHS")
S1.info((input(str("Enter Student Name: "))))
S1.Class(int(input("Enter Class: ")), int(input("Enter Roll no: ")))
S1.more_info()
