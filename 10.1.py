class Elevator:
    def __init__(self, bottom_floor, top_floor, current_floor=0):
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
            """if self.current_floor != self.bottom_floor:
                for i in range(self.current_floor, self.bottom_floor):
                    self.floor_down()"""  # i want to take the elevator back to bottom floor after use it every time.
        if self.current_floor > to_floor:
            for i in range(self.current_floor, to_floor, -1):
                self.floor_down()
        print(f"Thank you for using the elevator. The current floor is {self.current_floor}")


lift = Elevator(0, 7)
lift.go_to_floor(1)
