'''
Class Room - a room in an adventure game.

This class is part of the "World of Zuul" application. 
"World of Zuul" is a very simple, text based adventure game.  

A "Room" represents one location in the scenery of the game.  It is 
connected to other rooms via exits.  The exits are labelled north, 
east, south, west.  For each direction, the room stores a reference
to the neighboring room, or null if there is no exit in that direction.

@author  Michael Kolling and David J. Barnes
@version 2008.03.30
'''
class Room:

	'''
	Create a room described "description". Initially, it has
	no exits. "description" is something like "a kitchen" or
	"an open court yard".
	@param description The room's description.
	'''
	def __init__(self, description):
		self.description = description
		self.exits = {}
	
	'''
	Define the exits of this room.  Every direction either leads
	to another room or is null (no exit there).
	@param north The north exit.
	@param east The east east.
	@param south The south exit.
	@param west The west exit.
	'''
	def setExits(self, direction, neighbor):
		self.exits[direction] = neighbor

	'''
	@return The description of the room.
	'''
	def getDescription(self):
		return self.description
	
	def printLocationInfo(self):
		return f"You are {self.description}.\n{self.getExitString()}"

	def getExitString(self):
		return "Exits: " + " ".join(self.exits.keys())
	
	def getExit(self, direction):
		return self.exits.get(direction)

