def run_matching(verbose = True):
    import math

    hospitals = {}
    hospitalsCheck = {}
    students = {}
    lineIndex = 1
    hospitalIndex = 1
    studentIndex = 1
    fileLinesIndex = 1
    pairs = []
    n = 0
    currentHospital = 1 #current hospital index

    numLines = sum(1 for line in open("test-files/example1.in")) #read in number of lines
    halfLines = math.ceil((numLines-2) / 2)

    #handle a number that has more than single digit
    def multipleDigits(index, line):
        number = ""

        while index < len(line) and line[index] != " ":
            number += line[index]
            index += 1
    
        return [number, index]


    #get and store each number from the current preference line
    def getLineValues(currentLine):
        values = []
        i = 0
    
        while i < len(currentLine):
            if (currentLine[i] != " " and i + 1 < len(currentLine) and currentLine[i + 1] != " "):
                numberVal = multipleDigits(i, currentLine)
                values.append(int(numberVal[0]))
    
                i = numberVal[1]
    
            elif (currentLine[i] != " "):
                values.append(int(currentLine[i]))
                i += 1
    
            i += 1

        return values


    #set and update the hospital dictionary
    def setHospitals(currentLine, hospitalIndex):
        hospitalPreferenceList = getLineValues(currentLine)

        #store preference list for each hospital
        hospitals[hospitalIndex] = hospitalPreferenceList
        hospitalsCheck[hospitalIndex] = list(hospitalPreferenceList)


    #set and update student dictionary
    def setStudents(currentLine, studentIndex):

        # store preference list for each student
        studentPreferenceList = getLineValues(currentLine)
        students[studentIndex] = studentPreferenceList


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


        #current hospital has higher preference than hospital student is paired with
        if(currentHospitalIndex < pairedHospitalIndex):
            pairedIndex = getPairIndex(pariedHosptial, student)
            pairs.pop(pairedIndex) #remove previously paired hospital from list
            return True

        else:
            return False


    #check number of pairs in list
    def checkPairSize(pairs):

        if(len(pairs) < int(n)):
            return True

        else:
            return False


    #get values of student and hospital preference lists
    with open("test-files/example1.in") as file:
        for line in file:

            if lineIndex == 1:
                n = line.rstrip()

            #get individual values from current line and place in a dictionary
            else:
                strippedLine  = line.rstrip()

                #check line index
                if fileLinesIndex <= halfLines:
                    setHospitals(strippedLine, hospitalIndex)
                    fileLinesIndex += 1
                    hospitalIndex += 1

                else:
                    setStudents(strippedLine, studentIndex)
                    fileLinesIndex += 1
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

        #student paired and hospital rejected: remove student from preference list
        else:
            preferenceList.pop(0)

        currentHospital += 1

        #reset hospital index counter for next iteration
        if currentHospital > int(n):
            currentHospital = 1


    def printSolution(pairs):

        for pair in pairs:
            print(pair[0], "", pair[1])

    if verbose:
        printSolution(pairs)
    return pairs, hospitalsCheck, students, int(n)


run_matching()
