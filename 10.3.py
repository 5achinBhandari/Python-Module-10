class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print(f"Invalid floor. Please select a floor between {self.bottom_floor} and {self.top_floor}.")
            return

        while self.current_floor != target_floor:
            if self.current_floor < target_floor:
                self.floor_up()
            elif self.current_floor > target_floor:
                self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now at floor {self.current_floor}.")
        else:
            print("Already at the top floor.")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now at floor {self.current_floor}.")
        else:
            print("Already at the bottom floor.")


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_num, target_floor):
        if 0 <= elevator_num < len(self.elevators):
            self.elevators[elevator_num].go_to_floor(target_floor)
        else:
            print(f"Invalid elevator number. Please select an elevator between 0 and {len(self.elevators) - 1}.")

    def fire_alarm(self):
        print("Fire alarm activated!")
        for idx, elevator in enumerate(self.elevators):
            elevator.go_to_floor(self.bottom_floor)


def main():
    # Create a building with bottom floor as 1, top floor as 10, and 2 elevators
    building = Building(1, 10, 2)

    # Run elevator 0 to floor 5
    building.run_elevator(0, 5)

    # Run elevator 1 to floor 7
    building.run_elevator(1, 7)

    # Run elevator 0 back to the bottom floor
    building.run_elevator(0, 1)

    # Activate fire alarm
    building.fire_alarm()


if __name__ == "__main__":
    main()