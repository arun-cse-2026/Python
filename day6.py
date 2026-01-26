#Errors & Files

#Error Handling – try / except
try:
    x = int(input())
    print(10 / x)
except:
    print("Error occurred")


#File Handling(r,w,a)
#read
try:
    f = open("data.txt", "r")
    print(f.read())
    f.close()
except:
    print("File read error")
    
#write
try:
    f = open("data.txt", "w")
    f.write("Hello Python")
    f.close()
except:
    print("File write error")


#append
try:
    f = open("data.txt", "a")
    f.write("\nNew line added")
    f.close()
except:
    print("File append error")
    


