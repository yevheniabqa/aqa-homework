class Company:
    def __init__(self, name, industry, founder, founded_year, head_office, employees):
        self.name = name
        self.industry = industry
        self.founder = founder
        self.founded_year = founded_year
        self.head_office = head_office
        self.employees = employees

# A string representation of the company
    def __str__(self):
        return f"Company: {self.name}\nIndustry: {self.industry}\nFounded by: {self.founder}\n\
        Founded: {self.founded_year}\nHead office: {self.head_office}\nEmployees: {self.employees}"


