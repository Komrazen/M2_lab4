if __name__ == "__main__":
    # Write your solution here
    class Building:
        def __init__(self, name: str, address: str, floor_count: int) -> None:
            self._name = name
            self._address = address
            self._floor_count = floor_count

        def __str__(self) -> str:
            return f"{self._name} building, located at {self._address}, with {self._floor_count} floors"

        def __repr__(self) -> str:
            return f"Building(name='{self._name}', address='{self._address}', floor_count={self._floor_count})"

        def get_floors(self) -> int:
            return self._floor_count


    class Equipment:
        def __init__(self, name: str, description: str, manufacturer: str) -> None:
            self._name = name
            self._description = description
            self._manufacturer = manufacturer

        def __str__(self) -> str:
            return f"{self._name} ({self._manufacturer}) - {self._description}"

        def __repr__(self) -> str:
            return f"Equipment(name='{self._name}', description='{self._description}', manufacturer='{self._manufacturer}')"

        def get_manufacturer(self) -> str:
            return self._manufacturer


    class ResidentialBuilding(Building):
        def __init__(self, name: str, address: str, floor_count: int, apartment_count: int,
                     occupancy_rate: float) -> None:
            super().__init__(name, address, floor_count)
            self._apartment_count = apartment_count
            self._occupancy_rate = occupancy_rate

        def __str__(self) -> str:
            return f"{super().__str__()} with {self._apartment_count} apartments and an occupancy rate of {self._occupancy_rate}"

        def get_occupancy_rate(self) -> float:
            return self._occupancy_rate


    class Vehicle(Equipment):
        def __init__(self, name: str, description: str, manufacturer: str, fuel_type: str, max_speed: float) -> None:
            super().__init__(name, description, manufacturer)
            self._fuel_type = fuel_type
            self._max_speed = max_speed

        def __str__(self) -> str:
            return f"{super().__str__()}, runs on {self._fuel_type} and has a max speed of {self._max_speed} km/h"

        def get_max_speed(self) -> float:
            return self._max_speed
