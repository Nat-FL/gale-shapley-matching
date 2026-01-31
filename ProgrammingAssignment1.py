def run_matching():
    import math
    import validity_check
    hospitals = {}
    hospitalsCheck = {}
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
    halfLines = math.ceil((numLines-2) / 2)


    #set and update hospital dictionary with n hospitals and preference list of each hospital
    def setHospitals(currentLine, hospitalIndex):
        values = []

        for element in currentLine:
            if (element != " "):
                values.append(int(element))

        hospitals[hospitalIndex] = values
        hospitalsCheck[hospitalIndex] = list(values)

    #set and update student dictionary with n students and preference list of each student
    def setStudents(currentLine, studentIndex):
        values = []

        for element in currentLine:
            if (element != " "):
                values.append(int(element))

        students[studentIndex] = values


    #check if hospital already paired
    def checkHospitalPairs(hospital_index):

        if not pairs:
            return False

        for pair in pairs:
            if (pair[0] == hospital_index):
                return True

        return False

    def checkHospitalPreferenceList(preferenceList):

        #check if preference list empty --> no more possible candidates
        if not preferenceList:
            return False
        return True

    #check if student already paired
    def checkStudentPaired(student):

        for pair in pairs:
            if (pair[1] == student):
                return True

        return False

    #get paired hospital value from pairs list
    def getPairedHospital(student):

        for pair in pairs:
            if (pair[1] == student):
                # print("paired hospital value: " , pair[0])
                return pair[0]

    #get the index of a hospital in a student preference list
    def getHospitalIndex(hospital, student):
        index = 0
        studentPreferenceList = students.get(student)

        for preference in studentPreferenceList:
            if (preference == hospital):
                return index
            index += 1

    def getPairIndex(hospital, student):
        index = 0
        for pair in pairs:
            if (pair[0] == hospital) and (pair[1] == student):
                return index
            index += 1

    #check if student prefers hospital it is paired with or current hospital
    def changeHospital(student, currentHospital):
        pariedHosptial = getPairedHospital(student)
        pairedHospitalIndex = getHospitalIndex(pariedHosptial, student)
        currentHospitalIndex = getHospitalIndex(currentHospital, student)

        # print("paired hospital index val: " , pairedHospitalIndex)
        # print("current hospital index val: ", currentHospitalIndex)

        #current hospital has higher preference than hospital student is paired with
        if(currentHospitalIndex < pairedHospitalIndex):
            pairedIndex = getPairIndex(pariedHosptial, student)
            # print("paired hospital index val: ", pairedIndex)
            # print("PAIR REMOVED")
            pairs.pop(pairedIndex) #remove previously paired hospital from list
            # print("pairs after removal: ", pairs)
            return True

        else:
            return False

    #check number of pairs in list
    def checkPairSize(pairs):

        if(len(pairs) < int(n)):
            return True

        else:
            return False

    #get indices of student and hospital sets
    with open("exampleData.txt") as file:
        for line in file:

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

    #gale-shapley implementation
    while checkPairSize(pairs) and checkHospitalPreferenceList(hospitals.get(currentHospital)):

        #if hospital already paired skip over it
        if checkHospitalPairs(currentHospital):
            currentHospital += 1
            continue


        #get hospital preference list and set student value
        preferenceList = hospitals.get(currentHospital)
        student = preferenceList[0]


        #student is not paired
        if not(checkStudentPaired(student)):
            pairs.append([currentHospital, student])
            preferenceList.pop(0)

        #student is paired, so check if student prefers current hospital
        elif changeHospital(student, currentHospital):

            pairs.append([currentHospital, student])
            preferenceList.pop(0)


        #student paired but hospital rejected: remove student from hospital preference list
        else:

            preferenceList.pop(0)

        currentHospital += 1

        #reset hospital index counter for next iteration
        if currentHospital > int(n):
            currentHospital = 1

    def printSolution(pairs):

        for pair in pairs:
            print(pair[0], "", pair[1])

        # stability = check_validity(int(n), pairs)
        stability = validity_check.check_stability(int(n),pairs,hospitalsCheck, students)
        print("stability status: ", stability[1])

    # print("HOSPITALS", hospitals)
    printSolution(pairs)

run_matching()