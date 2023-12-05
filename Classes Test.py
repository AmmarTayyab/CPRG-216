class test:
        def __init__(self):
                self.first = 0
                self.second = 0

theTest = test()

theTest.first = 10
theTest.second = 17

print (theTest.first + theTest.second)


class Appointment:
        def __init__(self, day_of_week, start_time_hour):
                self._week = day_of_week
                self._hour = start_time_hour
                self.client_name = 0
                self.client_phone = 0
                self.appt_type = 0

        
        def get_client_name(self):
                return self.client_name
        
        def get_client_phone(self):
                return self.client_phone
        
        def get_appt_type(self):
                return self.appt_type
        
        def get_appt_type_desc(self):
                if self.appt_type == "0":
                        return "Available"
                elif self.appt_type == "1":
                        return "Mens cut"
                elif self.appt_type == "2":
                        return "Ladies Cut"
                elif self.appt_type == "3":
                        return "Mens Colouring"
                elif self.appt_type == "4":
                        return "Ladies Colouring"
                
                
       
        def __str__(self):
                return (f"{my_app.get_day()} {self.__week}")

day_of_week = 1
start_time_hour = 10

appt1 = 1

my_app = Appointment(day_of_week, start_time_hour)
print (my_app)



