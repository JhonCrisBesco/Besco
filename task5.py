class Employee:
    def __init__(employee):
        employee.name = input("Employee name: ")
        employee.position = input("Employee position: ")
        employee.salary = float(input("Employee salary: "))
    
    def give_raise(employee, amount):
        if amount > 0:
            employee.salary += amount
            print(f"Salary increased by₱{amount}\nNew salary: ₱{employee.salary}")
        else:
            print("Raise amount must be positive.")

    def display_employee(employee):
        print(f"Employee Name: {employee.name}")
        print(f"Position: {employee.position}")
        print(f"Salary: ₱{employee.salary}")

employee = Employee()

employee.display_employee()

raise_amount = float(input("Enter the raise amount: "))
employee.give_raise(raise_amount)
employee.display_employee()
