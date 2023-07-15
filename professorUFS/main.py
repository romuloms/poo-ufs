from professorUFS import ProfessorUFS


name = input("Type in the name of the professor: ")
registration = input("Type in the Registration of the professor: ")

prof1 = ProfessorUFS(name, registration)

print(f"Professor 1:\nName: {prof1.getName()}, Registration: {prof1.getRegistration()}, Workload: 8h (default workload).")

userChoice = 0

while userChoice != 3:
    userChoice = input("Type 1 to add hours to professor\'s workload, 2 to decrease or 3 to leave: ")
    if userChoice.isalpha():
        print("Invalid choice.")
    elif int(userChoice) == 1:
        amount = int(input("Type how many hours you wish to add: "))
        prof1.addHours(amount)
        print(f"New workload: {prof1.getWorkload()}h")
    elif int(userChoice) == 2:
        amount = int(input("Type how many hours you wish to decrease: "))
        prof1.decreaseHours(amount)
        print(f"New workload: {prof1.getWorkload()}h")
    elif int(userChoice) == 3:
        break
    else:
        print("Invalid choice.")
