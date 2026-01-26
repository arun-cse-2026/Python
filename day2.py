
#conditions 

 #if 
age = int(input("Enter your age: "))  

if age >= 18:
    print("You are an adult")
    
#elif
mark = int(input("Enter your mark: "))

if mark == 100:
    print("Perfect score!")
elif mark >= 50:
    print("Pass")
          
#else
a = int(input("Enter temperature: "))
if a > 30:
    print("Hot weather")
else:
    print("Not hot")

#comparison operators
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

print(a == b) 
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

#logical operators
age = int(input("Enter your age: "))
country = input("Enter your country: ")

if age >= 18 and country == "India":
    print("Eligible to vote in India")

if age < 18 or country != "India":
    print("Not eligible to vote in India")
