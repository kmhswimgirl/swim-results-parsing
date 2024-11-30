import re

file = open('/Users/kmh_swimgirl/PythonOne/MeetData/102724FullResults.txt', 'r')
lines = file.readlines()
file.close()

print_next_lines = 0

choice = input("Name (n) or Event (e)?")

if(choice == "n"):
    name = input("Enter Name: " )
    # Swim Data Extraction by Name
    print( "----------> " + name + "'s Swim Data "+ "<----------")
    print("")
    for line in lines:
       if print_next_lines != 0:
            if re.search('[a-zA-Z]', line) and print_next_lines != 5:  # Check if the line contains any letters, without eliminating the first line with my name in it
                print_next_lines = 0
            else:
             print(line)
             print_next_lines -= 1
       if name in line:
         print(line)
         print_next_lines = 5

if (choice == "e"):
    dist = input("distance (yds): " )
    stroke = input("Stroke: ")

    event = dist + " Yard " + stroke #combines entries to form event name

    print("Swim Data for "+ event)
    print("")
    # Swim Data by event
    for line in lines:
        if print_next_lines != 0:
                if re.search('=', line) and print_next_lines < (origVal - 4) :
                    print_next_lines = 0
                else:
                 print(line)
                 print_next_lines -= 1
        if event in line:
            print(line)
            print_next_lines = 50
            origVal = 50

if (choice != "n" and choice != "e" ):
    print("ERROR: Invalid Entry!")