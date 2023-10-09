class Worker:
    def __init__(self, name, employee_id, job_title, experience, department, salary):
        self.name = name
        self._employee_id = employee_id  # Protected attribute
        self.job_title = job_title
        self.experience = experience
        self._department = department  # Protected attribute
        self.__salary = salary  # Private attribute

    # Public method
    def describe_worker(self):
        return f"{self.name} is a {self.job_title}, has {self.experience} years of experience in the {self._department} department."

    # Getter method for salary (property)
    @property
    def salary(self):
        return self.__salary

    # Setter method for salary (property)
    @salary.setter
    def salary(self, new_salary):
        if new_salary >= 0:
            self.__salary = new_salary
        else:
            print("Salary must be a non-negative value.")

    # Public static method
    @staticmethod
    def is_senior(experience):
        return experience >= 5

    # Class method
    @classmethod
    def create_manager(cls, name, employee_id, department):
        job_title = "Manager"
        experience = 5
        salary = 3000
        return cls(name, employee_id, job_title, experience, department, salary)

# Create an instance of the Worker class
worker = Worker("Mortimer Goth", "A12345", "AQA", 3, "IT", 3500)

# Accessing attributes
print("Name:", worker.name)
print("Employee ID:", worker._employee_id)  # Protected attribute
# The following line would raise an AttributeError since it's private:
# print("Salary:", worker.__salary)

# Calling methods
print(worker.describe_worker())

# Using properties (getters and setters)
print(f"Current salary of {worker.name}: {worker.salary}")
worker.salary = 4000  # Using setter method
print(f"Updated salary of {worker.name}: {worker.salary}")

# Calling a static method
senior = Worker.is_senior(worker.experience)
print(f"Is {worker.name} a senior worker? {senior}")

# Using a class method to create a manager
manager = Worker.create_manager("Cassandra Goth", "A67890", "PM")
print(f"{manager.name} is a {manager.job_title} in the {manager._department} department.")
