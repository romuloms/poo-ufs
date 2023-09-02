class Room:
	# create a room with its description and no exits at first
	def __init__(self, description):
		self.__description = description
		self.__exits = {}
	
	# set room exits
	def setExits(self, direction, neighbor):
		self.__exits[direction] = neighbor
    # return room description
	def getDescription(self):
		return self.__description
	# print room description and exits
	def printLocationInfo(self):
		return f"You are {self.__description}.\n{self.getExitString()}"
    # print room exits
	def getExitString(self):
		return "Exits: " + " ".join(self.__exits.keys())
	# return room exit
	def getExit(self, direction):
		return self.__exits.get(direction)
