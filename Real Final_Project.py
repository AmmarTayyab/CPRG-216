#Group_Assignment- Project: Classes
# Group Members-(Ammar Tayyab, Nischal Pandit, Misson Rana)



#Defining 'Appointment' class which represents an appointment in a barbershop. The class defines to store about the client, the appointment type, and the time of the appointment.
import os
class Appointment:
    def __init__(self, day_of_week=None, start_time_hour=None):
        self.client_name = ""
        self.client_phone = ""
        self.appt_type = 0  # 0 represents an available appointment
        self.day_of_week = day_of_week
        self.start_time_hour = start_time_hour
 
    @property
    def client_name(self):
        return self._client_name
 
    @client_name.setter
    def client_name(self, value):
        self._client_name = value
 
    @property
    def client_phone(self):
        return self._client_phone
 
    @client_phone.setter
    def client_phone(self, value):
        self._client_phone = value
 
    @property
    def appt_type(self):
        return self._appt_type
 
    @appt_type.setter
    def appt_type(self, value):
        self._appt_type = value
 
    # The 'schedule' method schedules an appointment with the provided client name, phone number, and appointment type.
    def schedule(self, client_name, client_phone, appt_type):
        self.client_name = client_name
        self.client_phone = client_phone
        self.appt_type = appt_type
 
    #The 'cancel' method cancels an appointment by resetting all its properties to their default values. 
    def cancel(self):
        self._client_name = ""
        self._client_phone = ""
        self._appt_type = 0
    
    #The 'format_record' method returns a string representation of the appointment
    def format_record(self):
        return f"{self.client_name} , {self.client_phone}, {self.appt_type} , {self.day_of_week} , {self.start_time_hour:02d}"
 
    #The 'get_appt_type_desc' method  returns a description of the appointment type.
    def get_appt_type_desc(self):
        types = {
            0: "Available",
            1: "Mens Cut",
            2: "Ladies Cut",
            3: "Mens Colouring",
            4: "Ladies Colouring"
        }
        return types.get(self._appt_type, "Unknown")
 
    #The 'get_end_time_hour' determines and returns the appointment's end time by adding 1 to the start time hour.
    def get_end_time_hour(self):
        return self.start_time_hour + 1
 
    #The __str__method modifies the object class's default __str__method. It returns a string representation of the appointment, formatted for user display.
    def __str__(self):
        type_descriptions = {
            0: "Available",
            1: "Mens cut",
            # ... Add descriptions for other appointment types as needed
        }
        type_description = type_descriptions.get(self._appt_type, "Unknown")
        start_time = f"{self.start_time_hour:02d}:00"
        end_time = f"{self.start_time_hour + 1:02d}:00"
        return f"{self._client_name.ljust(20)} {self._client_phone.ljust(15)} {self.day_of_week.ljust(9)} {start_time} - {end_time} {type_description}"
 
 
class AppointmentManager:
    #Creating AppointmentManager instance with an empty appointment list.
    def __init__(self):
        self.appointments = []
 
    #Creating a weekly calender with time slots which are available.
    def create_weekly_calendar(self):
        self.days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.available_hours = list(range(9, 17))  # 9 AM to 4 PM
        available_hours = self.available_hours
        existing_appointments = set()
        for day in self.days_of_week:
            for hour in available_hours:
                existing_appointment = self.find_appointment_by_time(day, hour)
                if existing_appointment is None and (day, hour) not in existing_appointments:
                    appointment = Appointment(day, hour)
                    self.appointments.append(appointment)
                    existing_appointments.add((day, hour))
                elif existing_appointment and not existing_appointment.client_name:
                    # Remove the conflicting appointment without a client name
                    self.appointments.remove(existing_appointment)
                    existing_appointments.remove((day, hour))
 

 
    #Checking to find out if the appointment file the user would like to load exists. If it does exist it loads the file.
    def load_scheduled_appointments(self, fileName):
        isExist = os.path.exists(fileName)
        if isExist == True:
                with open(fileName, 'r') as file:
                    appointmentNumber = 0
                    for line in file:
                        client_name, client_phone, appt_type, day, start_time_hour = map(str.strip, line.split(','))
                        start_time_hour = int(float(start_time_hour))
                        appt_type = int(appt_type)
                        appointment = Appointment(day, start_time_hour)
                        appointment.schedule(client_name, client_phone, appt_type)
                        self.appointments.append(appointment)
                        appointmentNumber += 1
                    print(f"{appointmentNumber} scheduled appointments have been loaded.")
        while isExist != True:
                if isExist != True:
                    fileName = input("File not found. Re-enter appointment filename: ")
                    isExist = os.path.exists(fileName)
                    if isExist == True:
                        with open(fileName, 'r') as file:
                            appointmentNumber = 0
                            for line in file:
                                client_name, client_phone, appt_type, day, start_time_hour = map(str.strip, line.split(','))
                                start_time_hour = int(float(start_time_hour))
                                appt_type = int(appt_type)
                                appointmentNumber += 1
                            print(f"{appointmentNumber} scheduled appointments have been loaded.")
    
                                
 
    #Saving all the scheduled appointments to a file before exiting using 'save_scheduled_appointments' function.
    def save_scheduled_appointments(self, fileName):
        isExist = os.path.exists(fileName)
        if isExist == True:
            with open(fileName, 'r') as openFile:
                overWrite = input("File already exists. Do you want to overwrite it (Y/N)? ")
                if overWrite.lower() != "y":
                    return  # Exit the method if the user chooses not to overwrite
                else:
                    openFile = open(fileName, 'w')
                    apptCount = 0
                    for appointment in self.appointments:
                        if appointment.appt_type != 0:
                            openFile.write(f"{appointment.format_record()}\n")
                            apptCount += 1
                    print(f"{apptCount} scheduled appointments have been successfully saved.")
                    openFile.close()
                    openFile = open(fileName, 'r')
                    print(openFile.read())

        else:  
            with open(fileName, 'w') as openFile:
                apptCount = 0
                for appointment in self.appointments:
                    if appointment.appt_type != 0:
                        openFile.write(f"{appointment.format_record()}\n")
                        apptCount += 1
            print(f"{apptCount} scheduled appointments have been successfully saved.")
            openFile = open(fileName, 'r')  
 
   
    #Using 'show_appointments_by_name' method that takes two parameters: 'self' and 'client name' to display a list of appointments for a specified client.
    def show_appointments_by_name(self, client_name):
        found_appointments = [appointment for appointment in self.appointments if
                          client_name.lower() in appointment.client_name.lower()]
        print(f"Appointments for {client_name}\n")
        print("{:<20} {:<15} {:<9} {:<5} {:<5} {:<10}".format(
            "Client Name", "Phone", "Day", "Start", "End", "Type"))
        print("--------------------------------------------------------------------------------")
        if found_appointments:
            for appointment in found_appointments:
                print(appointment)
        else:
            print(f"No appointments found for {client_name}.")

 
    #Using 'show_appointments_by_day' method that also takes in two parameters: 'self' and 'day' to display a lsit of appointments for a specified day.
    def show_appointments_by_day(self, day):
        print(f"Appointments for {day.capitalize()}\n")
        print("{:<20} {:<15} {:<9} {:<5} {:<5} {:<10}".format(
            "Client Name", "Phone", "Day", "Start", "End", "Type"))       
        print ("--------------------------------------------------------------------------------")
        appointments_for_day = [appointment for appointment in self.appointments if appointment.day_of_week.lower() == day.lower()]
        sorted_appointments = sorted(appointments_for_day, key=lambda x: (x.start_time_hour, x.client_name.lower() if x.client_name else ''))
        for appointment in sorted_appointments:
            print("{:<20} {:<15} {:<9} {:<5} {:<5} {:<10}".format(
                appointment.client_name if appointment.client_name else '',
                appointment.client_phone if appointment.client_name else '',
                appointment.day_of_week,
                (str(appointment.start_time_hour) + ":00"),
                (str(appointment.get_end_time_hour())+":00"),
                appointment.get_appt_type_desc()))
 
    
    #Using 'display_menu' method to provide option for the users to plan an appointment,search for an appointment by name,print the calender for certain day,cancel the appointment anf exit the system.
    def display_menu(self):
        print ("\n\nJojo's Hair Salon Appointment Manager\n=====================================")
        print ("1) Schedule an appointment\n2) Find appointment by name\n3) Print calendar for a specific day\n4) Cancel an appointment\n9) Exit the system")
 
    #Using 'schedule_appointment' method to schedule an appointment. It replaces empty appointment time slots with appointments that have client information.
    def schedule_appointment(self, day, start_hour, client_name, client_phone, appt_type):
        existing_appointment = self.find_appointment_by_time(day, start_hour)
        existing_appointment = self.find_appointment_by_time(day, start_hour)
        if existing_appointment and existing_appointment.client_name:
            print(f"Appointment conflict: An appointment already exists at {day} {start_hour}:00 with {existing_appointment.client_name}.")
        else:
            if existing_appointment:
                self.appointments.remove(existing_appointment)
            appointment = Appointment(day, start_hour)
            appointment.schedule(client_name, client_phone, appt_type)
            print(f"OK, {client_name}'s appointment is scheduled!")
            self.appointments.append(appointment)
 
    #Using 'find_appointment_by_time' method for arranging an appointment on a certain day and time.
    def find_appointment_by_time(self, day, start_hour):
        for appointment in self.appointments:
            if appointment.day_of_week.lower() == day.lower() and appointment.start_time_hour == start_hour and not appointment.client_name:
                return appointment
        return None
 
    #Using 'cancel_appointment' method to cancel an appointment.
    def cancel_appointment(self):
         print("\n** Cancel an appointment **")
         day = input("Enter the day of the week: ")
         start_hour = int(input("Enter the start hour (24-hour clock): "))
         canceled_appointments = 0
         for appointment in self.appointments:
             if appointment.day_of_week.lower() == day.lower() and appointment.start_time_hour == start_hour:
                 if appointment.client_name:
                     canceled_appointments += 1
                     print(f"Appointment: {day} {start_hour}:00 - {start_hour+1}:00 for {appointment.client_name} has been cancelled!")
                     appointment.cancel()
         if canceled_appointments == 0:
             print(f"No appointments found for {day} {start_hour}:00.")
 
    #Using 'main' method for starting and running the Appointment Manager system.
    def main(self):
        print ("Starting the Appointment Manager System\nWeekly calendar created")
        #Creating a weekly calendar.
        self.create_weekly_calendar()
        loadFile = input("Would you like to load previously scheduled appointments from a file (Y/N)? ") #Asks the user if theyd like to load appointments from a previous file
        if  loadFile == "y" or loadFile == "Y":    #If the user says it allows them to enter a filename
                fileName = input("Enter appointment filename:  ")
                self.load_scheduled_appointments(fileName)
        while True:
            self.display_menu()             #Prints the menu and asks for an input from the user
            selection = input("Enter your selection: ")
            if selection == '1':              
                print ("\n** Schedule an appointment **")
                day = input("What day: ")
                if day.title() not in self.days_of_week:   #If the user tries to input a day that isnt a day of the week, the program will not schedule the appointment
                    print("Sorry that time slot is not in the weekly calendar!") 
                else:
                    start_hour = int(input("Enter start hour (24-hour clock): "))
                    conflicting_appointments = [appointment for appointment in self.appointments if  #Checks if there are already other appointments in the timeslot
                                                appointment.day_of_week.lower() == day.lower() and
                                                appointment.start_time_hour == start_hour and
                                                appointment.client_name]
                    if conflicting_appointments:       #If there are other appointments in the timeslot it tells the user and does not schedule an appointment
                        print("Sorry that timeslot is booked already!")
                    elif start_hour not in self.available_hours:
                        print("Sorry that time slot is not in the weekly calendar!")                  
                    else:
                        client_name = input("Client Name: ")
                        client_phone = input("Client Phone: ")
                        print("Appointment types\n1: Mens Cut $50, 2: Ladies Cut $80, 3: Mens Colouring $50, 4: Ladies Colouring $120")
                        appt_type = int(input("Type of Appointment: "))
                        self.schedule_appointment(day, start_hour, client_name, client_phone, appt_type)
            elif selection == '2':
                print ("\n**Find appointment by name**") #Asks user to input name and then searches for and prints appointments with partial or full matches to that name
                client_name = input("Enter Client Name: ")
                self.show_appointments_by_name(client_name)
            elif selection == '3':   #Asks user to input a day of the week and then prints the schedule of that day's appointments for the week
                day = input("Enter the day of week : ")
                self.show_appointments_by_day(day)
            elif selection == '4':
                self.cancel_appointment()
            elif selection == '9':  #Exits the system and asks user if they'd like to save all the scheduled appointments to a file
                print("** Exit the system **")
                saveFile = input("Would you like to save all scheduled appointments to a file? (Y/N)? ")
                if  saveFile == "y" or saveFile == "Y":
                    fileName = input("Enter appointment filename:  ")
                    self.save_scheduled_appointments(fileName)
                break
 
 
if __name__ == "__main__":
    salon_manager = AppointmentManager()
    salon_manager.main()