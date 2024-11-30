import re

file = open('/Users/kmh_swimgirl/PythonOne/MeetData/102724FullResults.txt', 'r') # opens up the meet data file
lines = file.readlines() # reads lines one at a time
file.close() # closes the file

print_next_lines = 0 # initializes the line counter

choice = input("Name (n) or Event (e)?: ") # input filed for Name vs Event sorting

# process for sorting time data by name 
if(choice == "n"): 
    name = input("Enter Name: " ) # name search/input field

    # Swim Data Extraction by Name
    print( "----------> " + name + "'s Swim Data "+ "<----------") # makes data easier to read visually
    print("")
    for line in lines:
       if print_next_lines != 0:
            if re.search('[a-zA-Z]', line) and print_next_lines != 5:  # Check if the line contains any letters, without eliminating the first line
                print_next_lines = 0
            else:
             print(line)
             print_next_lines -= 1
       if name in line:
         print(line)
         print_next_lines = 5

if (choice == "e"): # sorting meet data by event

    # Constants & Inputs
    dist = input("distance (yds): " )
    stroke = input("Stroke: ")
    gender = input("men's or women's results? (m/w): ")

    def filterStroke(stType): # filter events by stroke, accounting for different abbreviations.
        if stType in ["Freestyle", "FR", "Free", "fr", "free", "freestyle"]:
            return "Freestyle"
        if stType in ["Breaststroke", "BR", "Breast", "br", "breast", "breaststroke"]:
            return "Breaststroke"
        if stType in ["Butterfly", "FL", "Fly", "fl", "fly", "butterfly"]:
            return "Butterfly"
        if stType in ["Backstroke", "BK", "Back", "bk", "back", "backstroke"]:
            return "Backstroke"
        if stType in ["Individual Medley", "IM", "Ind Med", "im", "ind med", "individual medley"]:
            return "Individual Medley"
        
    def filterGender(genInput): # filter events by gender
        if(genInput == "m"):
            return("Men")
        if(genInput == "w"):
            return("Women")

    event = filterGender(gender)+ " " + dist + " Yard " + filterStroke(stroke) # combines entries to form event name

    print("=============== " + "Swim Data for "+ event + " ===============")
    print("")
   
    for line in lines:  # Swim Data by event
        if print_next_lines != 0:
                if re.search('<b>', line) and print_next_lines < (origVal - 4) :
                    print_next_lines = 0
                else:
                 print(line)
                 print_next_lines -= 1
        if event in line:
            print(line)
            print_next_lines = 50
            origVal = 50

if (choice != "n" and choice != "e" ): # Error messages
    print("ERROR: Invalid Entry!")
