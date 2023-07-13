from professorUFS import ProfessorUFS


prof1 = ProfessorUFS("Rom", 2020001, 15)

print(f"Professor 1:\nName: {prof1.getName()}, Registration: {prof1.getRegistration()}, Workload: {prof1.getWorkload()}")

prof1.addHours(6)
print(f"New workload: {prof1.getWorkload()}")

prof1.decreaseHours(2)
print(f"New workload: {prof1.getWorkload()}")
