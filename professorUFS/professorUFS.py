class ProfessorUFS:
    def __init__(self, name, registration, workload):
        self._name = str(name)
        self._registration = str(registration)
        self._workload = int(workload)
        self._minWorkload = 8
        self._maxWorkload = 20

    def getName(self):
        return self._name
    
    def getRegistration(self):
        return self._registration
    
    def getWorkload(self):
        return self._workload
    
    def setName(self, name):
        self._name = name
    
    def setRegistration(self, registration):
        self._registration = registration

    def setWorkload(self, workload):
        if workload < self._minWorkload or workload > self._minWorkload:
            print("Workload has to be inside the interval 8h~20h.")
        else:
            self._workload = workload
    
    def addHours(self, hours):
        if (self._workload + hours) > self._maxWorkload:
            print("Workload cannot be greater than 20 hours per week. The workload will bet set to 20h.")
            self._workload = self._maxWorkload
        else:
            self._workload += hours
    
    def decreaseHours(self, hours):
        if (self._workload - hours) < self._minWorkload:
            print("Workload cannot be lower than 8 hours per week. The workload will be set to 8h.")
            self._workload = self._minWorkload
        else:
            self._workload -= hours