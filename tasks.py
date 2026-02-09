from abc import ABC, abstractmethod

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def login(self):
        print(f"{self.name} has logged in successfully.")

class Patient(User):  
    def __init__(self, name, email, health_id):
        super().__init__(name, email)
        self.__health_id = health_id

    def get_health_id(self):
        return self.__health_id

    def set_health_id(self, new_id):
        if isinstance(new_id, str) and len(new_id) > 5:
            self.__health_id = new_id
            print("Health ID is updated")
        else:
            print("Invalid Health ID!")

class Doctor(User):
    def __init__(self, name, email, specialization):
        super().__init__(name, email)
        self.specialization = specialization

    def __str__(self):
        return f"Dr. {self.name} - {self.specialization}"
    

class Consultation(ABC):
    @abstractmethod
    def prescribe(self):
        pass

class GeneralCheckup(Consultation):
    def prescribe(self):
        print("Take vitamins and rest ")

class Surgery(Consultation):  
    def prescribe(self):
        print("Surgery required")


print("Mediflow Healthcare System")
patient1 = Patient("Arun", "arun@gmail.com", "HID12345")
patient1.login()
print("Health ID:", patient1.get_health_id())
patient1.set_health_id("NEW67890")
print("Updated Health ID:NEW67890")
patient1.get_health_id()
print("Doctor detils")
doctor1 = Doctor("Ravi", "ravi@gmail.com", "Heart Specialist")
print(doctor1)

print("Doctor decision:")
choice = input("Enter consultation type (general/surgery): ").lower() 
if choice == "general":
    consultation = GeneralCheckup()
elif choice == "surgery":
    consultation = Surgery()
else:
    print("Invalid choice")
    consultation = None

if consultation:
    consultation.prescribe()



        
    






