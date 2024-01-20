class Elevator:
	def __init__(self, bottom_floor, top_floor, current_floor=0, ):
		self.current_floor = current_floor
		self.bottom_floor = bottom_floor
		self.top_floor = top_floor

	def floor_up(self):
		self.current_floor += 1
		print(f"Elevator is going up.  {self.current_floor}")

	def floor_down(self):
		self.current_floor -= 1
		print(f"Elevator going down. {self.current_floor}")

	def go_to_floor(self, to_floor):
		if self.current_floor < to_floor:
			for i in range(self.current_floor, to_floor):
				self.floor_up()

		if self.current_floor > to_floor:
			for i in range(self.current_floor, to_floor, -1):
				self.floor_down()
		print(f"Thank you for using the elevator. The current floor is {self.current_floor}")


class Building:
	building_counter = 0

	def __init__(self, numbers_of_elevator, bottom_floor, top_floor):
		self.elevator_object = []
		self.bottom_floor = bottom_floor
		self.top_floor = top_floor
		Building.building_counter += 1
		self.building_number = Building.building_counter
		for i in range(0, numbers_of_elevator):
			self.elevator_object.append(Elevator(bottom_floor, top_floor, bottom_floor))

	def run_elevator(self, number_of_elevator, to_floor):
		print("Building ", self.building_number, "Elevator number:", number_of_elevator)
		self.elevator_object[number_of_elevator].go_to_floor(to_floor)


lift = Elevator(0, 7)
building = Building(3, 0, 10)  # creating a building object
building.run_elevator(2, 4)  # ask third elevator to go fourth floor
building.run_elevator(0, 9)  # ask first elevator to go ninth floor
building.run_elevator(0, 5)  # ask first elevator to go fifth floor
building1 = Building(5, 3, 7)  # creating second building object
building1.run_elevator(4, 7)  # ask second building elevator to go fourth floor