class Worker:
    def __init__(self, name, employee_id, job_title, experience, department, salary):
        self.name = name
        self.employee_id = employee_id
        self.job_title = job_title
        self.experience = experience
        self.department = department
        self.salary = salary

# A string representation of the worker
    def __str__(self):
        return f"Name: {self.name}\nEmployee ID: {self.employee_id}\nJob Title: {self.job_title}\n\
        Experience: {self.experience}\nDepartment: {self.department}\nSalary: ${self.salary:.2f}"

