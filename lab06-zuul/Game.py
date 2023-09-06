from Parser import *
from Room import *
from CommandWords import *

class Game:
    # create the game and initialize the map
	def __init__(self):
		self.__createRooms()
		self.__parser = Parser()
	# create the rooms and the exits
	def __createRooms(self):
		# create the rooms
		outside = Room("outside the main entrance of the university")
		theatre = Room("in a lecture theatre")
		pub = Room("in the campus pub")
		lab = Room("in a computing lab")
		office = Room("in the computing admin office")
		upstairs = Room("upstairs")
		basement = Room("in the basement")
        
		# initialise room exits
		outside.setExits("east", theatre)
		outside.setExits("south", lab)
		outside.setExits("west", pub)
		theatre.setExits("west", outside)
		pub.setExits("south", outside)
		lab.setExits("north", outside)
		lab.setExits("east", office)
		office.setExits("west", lab)
		office.setExits("up", upstairs)
		office.setExits("down", basement)
		upstairs.setExits("down", office)
		basement.setExits("up", office)
        
		self.currentRoom = outside  # start game outside

	# game loop
	def play(self):          
		self.__printWelcome()

		# execute commands until quit command
		finished = False
		while (not finished):
			command = self.__parser.getCommand()
			finished = self.__processCommand(command)
		print("Thank you for playing.  Good bye.")

	def __printWelcome(self):
		print("\nWelcome to the World of Zuul!")
		print("World of Zuul is a new, incredibly boring adventure game.")
		print("Type 'help' if you need help.\n")
		print(self.currentRoom.printLocationInfo())

	def __processCommand(self, command):
		wantToQuit = False

		if(command.isUnknown()):
			print("I don't know what you mean...")
			return False

		commandWord = command.getCommandWord()	# first word
		if(commandWord == "help"):
			self.__printHelp()
		elif (commandWord == "go"):
			self.__goRoom(command)
		elif (commandWord == "quit"):
			wantToQuit = self.__quit(command)

		return wantToQuit

	def __printHelp(self):
		print("You are lost. You are alone. You wander")
		print("around at the university.\n")
		print("Your command words are:")
		print("   go quit help")

	def __goRoom(self, command):
		if(not command.hasSecondWord()):
            # if there is no second word, we don't know where to go...
			print("Go where?")
			return

		direction = command.getSecondWord()

        # Try to leave current room.
		nextRoom = self.currentRoom.getExit(direction)
		if nextRoom == None:
			print("There is no door.")
			print(self.currentRoom.getExitString())
		else:
			self.currentRoom = nextRoom
			print(self.currentRoom.printLocationInfo())
		
	# command to quit the game
	def __quit(self, command):
		if(command.hasSecondWord()):
			print("Quit what?")
			return False
		else:
			return True  # signal that we want to quit
