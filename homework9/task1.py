class Company:
    def __init__(self, name, industry, founder, founded_year, head_office, employees, revenue):
        self.name = name
        self.industry = industry
        self._founder = founder  # Protected attribute
        self.founded_year = founded_year
        self.head_office = head_office
        self.employees = employees
        self.__revenue = revenue  # Private attribute

    # A string representation of the company
    def describe_company(self):  # Public method
        return f"Company: {self.name}\nIndustry: {self.industry}\nFounded by: {self.founder}\n\
        Founded: {self.founded_year}\nHead office: {self.head_office}\nEmployees: {self.employees}\nIt generates {self.__revenue} in revenue"


    # Getter method for revenue (property)
    @property
    def revenue(self):
        return self.__revenue

    # Setter method for revenue (property)
    @revenue.setter
    def revenue(self, new_revenue):
        if new_revenue > 0:
            self.__revenue = new_revenue
        else:
            print("Revenue must be a positive value.")

    # Public static method
    @staticmethod
    def is_profitable(revenue, expenses):
        return revenue > expenses

    # Class method
    @classmethod
    def create_startup(cls, name, founder, founded_year, head_office):
        industry = "Startup"
        employees = 0
        revenue = 0  # Initialize with zero revenue for startups
        return cls(name, industry, founder, founded_year, head_office, employees, revenue)

    @property
    def founder(self):
        return self._founder


# Create instances of the Company class
apple = Company("Apple Inc.", "Technology", "Steve Jobs", 1976, "Cupertino, California", 164000, 274.5e9)

print(apple.name)  # Public attribute
print(apple._founder)  # Protected attribute
# print(apple.__revenue) # gonna call the error since its private

# Calling public methods
print(apple.describe_company())

# Using properties (getters and setters)
print(f"Current revenue of {apple.name}: {apple.revenue}")
apple.revenue = 300e9  # Using setter method
print(f"Updated revenue of {apple.name}: {apple.revenue}")

# Calling a static method
profitable = Company.is_profitable(apple.revenue, 250e9)
print(f"Is {apple.name} profitable? {profitable}")

# Using a class method to create a startup company
startup = Company.create_startup("NewCo", "Jane Doe", 2023, "Lviv")
print(f"{startup.name} is a startup with a revenue of {startup.revenue}")
