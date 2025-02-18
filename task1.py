class Car:
    def __init__(car, brand, model, year):
        car.brand = brand
        car.model = model
        car.year = year
    
    def display_info(car):
        print(f"Brand: {car.brand}")
        print(f"Model: {car.model}")
        print(f"Year: {car.year}")

car1 = Car("Toyota", "Vios", 2022)
car2 = Car("Ford", "Ranger", 2024)

print("Car 1 Details:")
car1.display_info()
print("\nCar 2 Details:")
car2.display_info()
