import re

file = open('/Users/kmh_swimgirl/PythonOne/MeetData/102724FullResults.txt', 'r')
lines = file.readlines()
file.close()

print_next_lines = 0

choice = input("Name (n) or Event (e)?: ")

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
    isRelay = input("Relay? (y/n): ")

    def filterStroke(eventType):
        if(eventType == "Freestyle" or "FR" or "Free" or "fr" or "free" or "freestyle"):
            return("Freestyle")
        if(eventType == "Breaststroke" or "BR" or "Breast" or "br" or "breast" or "breaststroke"):
            return("Breaststroke")
        if(eventType == "Butterfly" or "FL" or "Fly" or "fl" or "fly" or "butterfly"):
            return("Butterfly")
        if(eventType == "Backstroke" or "BK" or "Back" or "bk" or "back" or "backstroke"):
            return("Butterfly")
        if(eventType == "Individual Medley" or "IM" or "Ind Med" or "im" or "ind med" or "individual medley"):
            return("Individual Medley")

    event = dist + " Yard " + filterStroke(stroke) #combines entries to form event name

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
