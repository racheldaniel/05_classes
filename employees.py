# Create a class that contains information about employees of a company and define methods to get/set employee name, job title, and start date.


class Employee:
    def __init__(self, name, employee_number):
        self.name = name
        self.employee_number = employee_number


    def hire_employee(self, department, job_title, start_date):
        self.department = department
        self.job_title = job_title
        self.start_date = start_date

    def get_emp_details(self):
        return f'Name: {self.name} \n Employee Number: {str(self.employee_number)} \n Dept: {self.department} \n Title: {self.job_title} \n Start Date: {self.start_date}'


class Company(object):

    def __init__(self, company_name, date_founded):
        self.company_name = company_name
        self.date_founded = date_founded
        self.employees = set()

    def get_company_name(self):
        return self.company_name

# Create a company, and three employees, and then assign the employees to the company.


nash_software = Company('Nashville Software School', '29-Feb-1601')

joe_shep = Employee('Joe Shepherd', 19238574)
joe_shep.hire_employee('Faculty', 'Full-Stack Instructor', '1-Jan-1937')


kimmie_bird = Employee('Kimmie Bird', 19238574)
kimmie_bird.hire_employee('Faculty', 'Junior Instructor', '15-Dec-1987')

nash_software.employees.add(joe_shep)
nash_software.employees.add(kimmie_bird)

for emp in nash_software.employees:
    print(f'{nash_software.company_name}, founded in {nash_software.date_founded}, employs the following instructor: \n {emp.get_emp_details()}')
