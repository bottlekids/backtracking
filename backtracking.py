"""
This is a simple backtracking algorithm which uses a bit of reccursion to plot hotel reservations on a list of lists which represents 
week days and rooms. Some of the guests are already checked in and can't be moved. All rooms are of the same type. 
"""

from tabulate import tabulate 

guest_list = []
empty_cell = " ______ "


week_overview = [[empty_cell for day in range(7)] for room in range(10)]


class Booking:

	def __init__ (self, name, check_in, check_out, fix, room):
		self.name = name 
		self.check_in = check_in
		self.check_out = check_out
		self.fix = fix
		self.room = room
		self.assigned = False

		guest_list.append(self)

	def __repr__(self):
		return self.name[:8]

	def populate_week_overview(self, room_number, reverse):
		date_counter = self.check_in
		# Because a backtracking algorithm requires that the object erase itself if it doesn't satisfy the 
		# conditions, I add a parameter "reverse". If it returns True, the object erases itself. 
		if reverse:
			while date_counter <= self.check_out:
				week_overview [room_number][date_counter] = empty_cell
				date_counter += 1
		while date_counter <= self.check_out:
			week_overview [room_number][date_counter] = self
			date_counter += 1
				
# Creating some guests:
guest1 = Booking("Tom", 0, 4, True, 1)
guest2 = Booking("Ron", 0, 1, True, 3)
guest3 = Booking("Leslie", 1, 5, False, None)
guest4 = Booking("April", 4, 6, False, None)
guest5 = Booking("Andy", 0, 3, False, None)
guest6 = Booking("Ben", 5, 6, False, None)
guest7 = Booking("Dona", 3, 4, True, 9)
guest8 = Booking("Li'l Sebastian", 1, 4, False, None)
guest9 = Booking("Jerry", 2, 4, False, None)
guest10 = Booking("Chris", 1, 2, False, None)
guest11 = Booking("Ann", 0, 6, False, None)
guest12 = Booking("Perd", 0, 6, False, None)
guest13 = Booking("Mark", 1, 6, False, None)
guest14 = Booking("Tammy2", 0, 4, False, None)

#to overbook uncomment guest
#guest15 = Booking("Tammy1", 4, 6, False, None)


guest_list.sort(key=lambda x: x.check_in)

def plot_fixed():
	for guest in guest_list:
		if guest.fix == True:
			guest.populate_week_overview(guest.room, reverse=False)
			guest.assigned = True

# This function checks if all fields from check-in to check-out are free so the guest can be given a room
def is_possible(guest, room):
	for cell in room[guest.check_in:guest.check_out]:
		if isinstance (cell, Booking):
			return False
	return True	
	
def optimal_arrangement():
	for guest in guest_list:
		# "assigned" is a class variable which returns True if the guest already has a room
		if guest.assigned == False:
			# Now for each guest we go through every room to see if there is space for them
			for index, room in enumerate(week_overview):
				if is_possible(guest, room):
					# If there is space, we plot the guest and run the function again
					guest.populate_week_overview(index, reverse=False)
					guest.assigned = True
					optimal_arrangement()
					"""
					Our function runs recursively and every time it finds a spot for a guest it will change their
					"assigned" variable to True so eventually there will be none left and the function will 
					print out the solution. For this to make sense there has to be a meaningful relationship between 
					the objects we iterate over in our guest list so that a step back could enable an efficient 
					second attempt in the future. If the guests are randomly arranged in the guest list
					maybe the function will have to go back hundreds of times to a very early instance of its 
					recursion which is inefficient. So the guest list is ordered by check-in and we go
					from left to right.    
					""" 
					guest.populate_week_overview(index, reverse=True)
					guest.assigned = False
			return
	print(tabulate(week_overview))	
	input("Satisfactory? ")



plot_fixed()

optimal_arrangement()

# If there are solutions we will remain in the recursive function. Otherwise we print out the error message:
print("Overbooked")

