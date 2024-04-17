class Employee:
    def __init__(self, name, emp_id, title, department):
        self.name = name
        self.emp_id = emp_id
        self.title = title
        self.department = department

    def display_details(self):
        """Display employee details."""
        print("Name:", self.name)
        print("ID:", self.emp_id)
        print("Title:", self.title)
        print("Department:", self.department)

    def __str__(self):
        """String representation of the employee."""
        return f"{self.name} - ID: {self.emp_id}"


class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        """Add an employee to the department."""
        self.employees.append(employee)

    def remove_employee(self, emp_id):
        """Remove an employee from the department."""
        for employee in self.employees:
            if employee.emp_id == emp_id:
                self.employees.remove(employee)
                print(f"Employee {employee.name} removed.")
                return
        print("Employee not found.")

    def list_employees(self):
        """List all employees in the department."""
        print(f"Employees in {self.name} department:")
        for employee in self.employees:
            print(employee)


class Company:
    def __init__(self):
        self.departments = {}

    def add_department(self, department):
        """Add a department to the company."""
        self.departments[department.name] = department

    def remove_department(self, department_name):
        """Remove a department from the company."""
        if department_name in self.departments:
            del self.departments[department_name]
            print(f"Department {department_name} removed.")
        else:
            print("Department not found.")

    def display_departments(self):
        """Display all departments in the company."""
        print("Departments:")
        for department_name in self.departments:
            print("-", department_name)


def print_menu():
    """Print the menu for user interaction."""
    print("\nEmployee Management System Menu:")
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. List Employees in Department")
    print("4. Add Department")
    print("5. Remove Department")
    print("6. Display Departments")
    print("7. Exit")


def add_employee(company):
    """Add an employee to a department."""
    department_name = input("Enter department name: ")
    if department_name not in company.departments:
        print("Department not found.")
        return

    name = input("Enter employee name: ")
    emp_id = input("Enter employee ID: ")
    title = input("Enter employee title: ")

    employee = Employee(name, emp_id, title, department_name)
    company.departments[department_name].add_employee(employee)
    print("Employee added successfully.")


def remove_employee(company):
    """Remove an employee from a department."""
    department_name = input("Enter department name: ")
    if department_name not in company.departments:
        print("Department not found.")
        return

    department = company.departments[department_name]
    emp_id = input("Enter employee ID: ")
    department.remove_employee(emp_id)


def list_employees_in_department(company):
    """List all employees in a department."""
    department_name = input("Enter department name: ")
    if department_name not in company.departments:
        print("Department not found.")
        return

    department = company.departments[department_name]
    department.list_employees()


def add_department(company):
    """Add a new department to the company."""
    department_name = input("Enter department name: ")
    if department_name in company.departments:
        print("Department already exists.")
        return

    department = Department(department_name)
    company.add_department(department)
    print("Department added successfully.")


def remove_department(company):
    """Remove a department from the company."""
    department_name = input("Enter department name: ")
    company.remove_department(department_name)


def main():
    company = Company()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee(company)

        elif choice == "2":
            remove_employee(company)

        elif choice == "3":
            list_employees_in_department(company)

        elif choice == "4":
            add_department(company)

        elif choice == "5":
            remove_department(company)

        elif choice == "6":
            company.display_departments()

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
