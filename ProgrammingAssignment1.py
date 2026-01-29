import math

hospitals = {}
students = {}
lineLengthIndex = 0
lineIndex = 1
index = 1
hospitalIndex = 1
studentIndex = 1
lineValues = []
pairs = []
n = 0
currentHospital = 1 #current hospital index

numLines = sum(1 for line in open("exampleData.txt")) #read in number of lines
print(numLines)

halfLines = math.ceil((numLines-2) / 2)
# print("half value :", halfLines)

#set and update hospital dictionary with n hospitals and preference list of each hospital
def setHospitals(currentLine, hospitalIndex):
    values = []

    for element in currentLine:
        if (element != " "):
            values.append(int(element))
            # print("current line: ", values)

    # ["hospital " + str(hospitalIndex)]
    hospitals[hospitalIndex] = values

#set and update student dictionary with n students and preference list of each hospital
def setStudents(currentLine, studentIndex):
    values = []

    for element in currentLine:
        if (element != " "):
            values.append(int(element))
            # print("current line: ", values)

    students[studentIndex] = values


def checkHospitalPairs(hospital_index):
    index = 0
    # print("hospital index: ", hospital_index)
    if not pairs:
        # print("False, hospital is not in a pair")
        return False

    for pair in pairs:
        # print("pair value: ", pair[0])
        if (pair[0] == hospital_index):
            print("true")
            return True

    return False

def checkHospitalPreferenceList(preferenceList):

    #check if preference list empty --> no more possible candidates
    if not preferenceList:
        # print("false list empty")
        return False
    return True

#check if student already paired
def checkStudentPairs(student):
    # index = 0
    # print("student index: ", student)

    # if not pairs:
    #     print("False, hospital is not in a pair")
    #     return False

    for pair in pairs:
        if (pair[1] == student):
            # print("true")
            return True

    return False

def getPairedHospital(student):
    # print("student")
    for pair in pairs:
        if (pair[1] == student):
            print("paired hospital value: " , pair[0])
            return pair[0]


def getHospitalIndex(hospital, student):
    index = 0
    studentPreferenceList = students.get(student)

    for preference in studentPreferenceList:
        if (preference == hospital):
            return index
        index += 1

def getPairIndex(hospital, student):
    # print("pair")
    index = 0
    for pair in pairs:
        if (pair[0] == hospital) and (pair[1] == student):
            return index
        index += 1

def changeHospital(student, currentHospital):
    pariedHosptial = getPairedHospital(student)
    pairedHospitalIndex = getHospitalIndex(pariedHosptial, student)
    currentHospitalIndex = getHospitalIndex(currentHospital, student)

    print("paired hospital index val: " , pairedHospitalIndex)
    print("current hospital index val: ", currentHospitalIndex)

    #current hospital has higher preference than hospital student is paired with
    if(currentHospitalIndex < pairedHospitalIndex):
        pairedIndex = getPairIndex(pariedHosptial, student)
        print("paired hospital index val: ", pairedIndex)
        print("PAIR REMOVED")
        pairs.pop(pairedIndex)
        print("pairs after removal: ", pairs)
        return True

    else:
        return False

def checkPairSize(pairs):

    print("pair size: ", len(pairs))
    print("n value: ", int(n))
    if(len(pairs) < int(n)):
        return True

    else:
        return False

#get indices of both hospitals
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

#checkHospitalPairs(currentHospital)
while checkPairSize(pairs) & checkHospitalPreferenceList(hospitals.get(currentHospital)):

    if checkHospitalPairs(currentHospital):
        currentHospital += 1
        continue

    print("current hospital: ", currentHospital)
    preferenceList = hospitals.get(currentHospital)
   # print("preference list value: ",preferenceList[0])
    student = preferenceList[0]
    print("top student value: ", student)

    if not(checkStudentPairs(student)):
        pairs.append([currentHospital, student])
        preferenceList.pop(0)
        # print("pairs: ", pairs)
        # currentHospital += 1

    elif changeHospital(student, currentHospital):
        #add function to remove current pair in hospital
        print("change hospital true, updated pair")
        pairs.append([currentHospital, student])
        preferenceList.pop(0)
        # pairs.insert(0,[currentHospital, student])
        # currentHospital += 1

    else:
        print("REMOVED TOP PREFERENCE")
        # removePairIndex = getPairIndex(currentHospital, student)
        preferenceList.pop(0) #student rejected hospital so remove from list
        # currentHospital += 1

    currentHospital += 1


    #reset hospital index counter for next iteration
    if currentHospital > int(n):
        currentHospital = 1

    # break



print(hospitals)
print(students)
print("pairs: ", pairs)
