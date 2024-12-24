class Car:
    def __init__(self, fuel_capacity, fuel_conbustion, average_speed):
        self.fuel_capacity = fuel_capacity
        self.fuel_conbustion = fuel_conbustion
        self.average_speed = average_speed

    def calculate_distance(self):
        return (self.fuel_capacity / self.fuel_conbustion) * 100

    def __add__(self, other):

        if isinstance(other, Car):
            return Car(
                self.fuel_capacity + other.fuel_capacity,
                (self.fuel_conbustion + other.fuel_conbustion) / 2,
                (self.average_speed + other.average_speed) / 2
            )
        return NotImplemented

    def __str__(self):
        return (f"Автомобиль: емкость бака = {self.fuel_capacity} л, "
                f"расход топлива = {self.fuel_conbustion} л/100 км, "
                f"средняя скорость = {self.average_speed} км/ч")

class Truck(Car):
    def __init__(self, fuel_capacity, fuel_consumption, average_speed, max_cargo_weight):
        super().__init__(fuel_capacity, fuel_consumption, average_speed)
        self.max_cargo_weight = max_cargo_weight

    def cargo_to_fuel_ratio(self, distance=250):
        fuel_needed = (self.fuel_conbustion / 100) * distance
        return self.max_cargo_weight / fuel_needed

    def __str__(self):
        return (super().__str__() +
                f", максимальный вес груза = {self.max_cargo_weight} кг")

class Bus(Car):
    def __init__(self, fuel_capacity, fuel_consumption, average_speed, passenger_capacity):
        super().__init__(fuel_capacity, fuel_consumption, average_speed)
        self.passenger_capacity = passenger_capacity

    def passenger_to_fuel_ratio(self, distance=250):
        fuel_needed = (self.fuel_conbustion / 100) * distance
        return self.passenger_capacity / fuel_needed

    def __str__(self):
        return (super().__str__() +
                f", вместимость пассажиров = {self.passenger_capacity}")


if __name__ == "__main__":
    car = Car(50, 8, 120)
    print(car)
    print(f"Расстояние до полного опустошения бака: {car.calculate_distance()} км\n")

    truck = Truck(100, 15, 80, 500)
    print(truck)
    print(f"Соотношение веса груза к топливу (250 км): {truck.cargo_to_fuel_ratio()} кг/л\n")

    bus = Bus(70, 12, 100, 50)
    print(bus)
    print(f"Соотношение пассажиров к топливу (250 км): {bus.passenger_to_fuel_ratio()} чел/л\n")

    combined_vehicle = truck + bus
    print("Объединенный автомобиль (грузовик + автобус):")
    print(combined_vehicle)
    print(f"Расстояние до полного опустошения бака объединенного автомобиля: {combined_vehicle.calculate_distance()} км")
