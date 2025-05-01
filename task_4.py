class EmployeeSalary():
    hourly_payment = 400

    def __init__(self, name, hours=None, rest_days=0, email=None):
        self.name = name
        self.rest_days = rest_days
        self.hours = self.get_hours(hours, rest_days)
        self.email = self.get_email(email, name)

    @classmethod
    def get_hours(cls, hours, rest_days):
        if hours is None:
            return (7 - rest_days) * 8
        return hours
    @classmethod
    def get_email(cls, email, name):
        if email is None:
            return f"{name}@email.com"
        return email

    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment

    def salary(self):
        return self.hours * self.hourly_payment


emp1 = EmployeeSalary("ivan", None, 2)  # часы не заданы, выходных 2
print(emp1.hours)       # 40
print(emp1.email)       # ivan@email.com
print(emp1.salary())    # 16000

emp2 = EmployeeSalary("olga", 35, 1, "olga@mail.ru")
print(emp2.salary())    # 14000

EmployeeSalary.set_hourly_payment(500)  # изменим ставку
print(emp2.salary())    # 17500 (35 * 500)