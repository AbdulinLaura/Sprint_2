class EmployeeSalary():
    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, hours, rest_days, email):
        if hours is None:
            hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name, hours, rest_days, email):
        if email is None:
            email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment

    def salary(self):
        return self.hours * self.hourly_payment


emp1 = EmployeeSalary.get_hours("ivan", None, 2, "ivan@email.com")
print(emp1.hours)       # 40
print(emp1.email)       # ivan@email.com
print(emp1.salary())    # 16000

emp2 = EmployeeSalary.get_email("olga", 35, 1, None)
print(emp2.hours)       # 35
print(emp2.email)       # olga@email.com
print(emp2.salary())    # 14000

# изменим ставку
EmployeeSalary.set_hourly_payment(500)
print(emp2.salary())    # 17500