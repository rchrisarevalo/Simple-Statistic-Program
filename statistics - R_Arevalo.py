i = 1
introv_count = 0
extrov_count = 0

total_avg = 0

final_introv_percent = 0.0
final_extrov_percent = 0.0

choice = " "

print("Enter -1 to exit program. Otherwise:")

while True:
    choice = input("Enter 'i' if you are introverted or 'e' if you are extroverted:")
    
    if choice == "i":
        introv_count += 1
        total_avg += 1
        
    elif choice == "e":
        extrov_count += 1
        total_avg += 1
        
    elif choice == "-1":
        break
    
    else:
        print("Wrong input!")
        
final_introv_percent = (introv_count / total_avg) * 100
final_extrov_percent = (extrov_count / total_avg) * 100

if final_introv_percent == 0.0 and final_extrov_percent == 0.0:
    print("It's empty!")
else:
    print("Percentage of introverts:", final_introv_percent, "%")
    print("Percentage of extroverts:", final_extrov_percent, "%")