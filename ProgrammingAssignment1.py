import math
hospitals = {}
students = {}
lineLengthIndex = 0
lineIndex = 1
index = 1
hospitalIndex = 1
studentIndex = 1
lineValues = []
n = 0

numLines = sum(1 for line in open("exampleData.txt")) #read in number of lines
print(numLines)

halfLines = math.ceil((numLines-2) / 2)
print("half value :", halfLines)

#set and update hospital dictionary with n hospitals and preference list of each hospital
def setHospitals(currentLine, hospitalIndex):
    values = []

    for element in currentLine:
        if (element != " "):
            values.append(int(element))
            print("current line: ", values)

    # ["hospital " + str(hospitalIndex)]
    hospitals[hospitalIndex] = values

#set and update student dictionary with n students and preference list of each hospital
def setStudents(currentLine, studentIndex):
    values = []

    for element in currentLine:
        if (element != " "):
            values.append(int(element))
            print("current line: ", values)

    students[studentIndex] = values


with open("exampleData.txt") as file:
    for line in file:

        print("line ", lineIndex," ", line)
        print(len(line.rstrip()))

        if lineIndex == 1:
            n = line.rstrip()

        #get individual values from current line and place in a dictionary
        else:
            strippedLine  = line.rstrip()

            #check line index
            if index <= halfLines:
                setHospitals(strippedLine, hospitalIndex)
                index += 1
                hospitalIndex += 1

            else:
                setStudents(strippedLine, studentIndex)
                index += 1
                studentIndex += 1

        lineIndex += 1

print(hospitals)
print(students)


