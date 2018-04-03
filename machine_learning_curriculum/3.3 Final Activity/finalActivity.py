#!/usr/bin/env python3

################################################################################
# DO NOT MODIFY THIS PART OF THE FILE
#
# (Unless you are sure of what you are doing :P )
################################################################################

import decisionTreeSolutions
import knnSolutions
import csv

class Person(object):
    def __init__(self, age, workclass, education, maritalStatus, occupation,
                 race, sex, capitalIncome, hoursPerWeek,
                 nativeCountry, incomeOver50K):
        self.age = age
        self.workclass = workclass
        self.education = education
        self.maritalStatus = maritalStatus
        self.occupation = occupation
        self.race = race
        self.sex = sex
        self.capitalIncome = capitalIncome
        self.hoursPerWeek = hoursPerWeek
        self.nativeCountry = nativeCountry
        self.__incomeOver50K__ = incomeOver50K

    def __str__(self):
        return ("Person(age: "+str(self.age) + ", " + repr(self.workclass) + ", " + repr(self.education) +
                ", " + repr(self.maritalStatus) + ", occupation: " + repr(self.occupation) + ", " +
                repr(self.race) + ", " + repr(self.sex) + ", capitalIncome: " + str(self.capitalIncome) + ", hoursPerWeek: " +
                str(self.hoursPerWeek) + ", " + repr(self.nativeCountry) + ", " + ">=50K: " + 
                str(self.__incomeOver50K__) + ")")

    def __repr__(self):
        return ("Person("+str(self.age) + ", " + repr(self.workclass) + ", " + repr(self.education) +
                ", " + repr(self.maritalStatus) + ", " + repr(self.occupation) + ", " +
                repr(self.race) + ", " + repr(self.sex) + ", " + str(self.capitalIncome) + ", " +
                str(self.hoursPerWeek) + ", " + repr(self.nativeCountry) + ", " +
                str(self.__incomeOver50K__) + ")")

class Database(object):
    def __init__(self, src):
        self.database = []
        filepath = "adult" + src + "Data.csv"
        with open(filepath, 'rt') as csvfile:
            fileReader = csv.reader(csvfile)
            for row in fileReader:
                if len(row) < 14: break
                # Eliminate all data points with missing values from the dataset
                foundUnknown = False
                for data in row:
                    if '?' in data:
                        foundUnknown = True
                        continue
                if foundUnknown: continue
                # Convert the entries to standard python data types
                age = int(row[0])
                workclass = row[1].strip()
                education = row[3].strip()
                maritalStatus = row[5].strip()
                occupation = row[6].strip()
                race = row[8].strip()
                sex = row[9].strip()
                capitalGain = int(row[10].strip())
                capitalLoss = int(row[11].strip())
                capitalIncome = capitalGain - capitalLoss
                hoursPerWeek = int(row[12].strip())
                nativeCountry = row[13].strip()
                incomeOver50K = True if ">50K" in row[14] else False
                self.database.append(Person(age, workclass, education,
                    maritalStatus, occupation, race, sex, capitalIncome,
                    hoursPerWeek, nativeCountry, incomeOver50K))

    def __iter__(self):
        return iter(self.database)

    def __getitem__(self, key):
        return self.database[key]

    def __len__(self):
        return len(self.database)

################################################################################
# WRITE YOUR CODE BELOW THIS
################################################################################

database = Database("Training")

# We'll use the loadDataForModel function to take a database instance and turn 
# it into a data list, which is the format that our KNN and DT algorithms use.
def loadDataForModel(database):
    data = []
    for person in database:
        feature1 = person.age
        feature2 = person.capitalIncome
        data.append([feature1, feature2, person.__incomeOver50K__])
    return data


# This function will take in a person (an instance of the Person class) and
# should return a boolean that indicates whether you predict that person has
# an income >50K (True) or <=50K (False). Use any data analysis or machine
# learning techniques that you would like. Feel free to write helper functions
# or to write separate code to get parameters that are then hardcoded into
# this function (like you did with decision trees)
#
# Note that for any global variables you use, including function names, please
# add your name at the end of the variable so it won't conflict with other
# student's variable names. For example, if my name is "Amal", my main function
# should be called "predictIncomeAmal".
#
# This function should also not use "database". Rather, database should be used
# to calculate parameters that you then use in the "predictIncome" function.
def predictIncomeMyName(person):
    ################################################################################
    # Include any global variables you want to use here:


    ################################################################################


    # If you want to use a KNN or DT, change the features to be the same features
    # that you used to train your model.
    feature1 = person.age
    feature2 = person.capitalIncome
    testInstance = [feature1, feature2]

    # Finally, return your prediction
    # Here, knnSolutions.getPrediction or decisionTreeSolutions.getPrediction may be
    # useful. Make sure you give them the correct arguments.
    return False


def testModel(expertFunctionName, database):
    numCorrect = 0
    for person in database:
        prediction = expertFunctionName(person)
        if prediction == person.__incomeOver50K__:
            numCorrect += 1
    print ("Accuracy:", numCorrect / len(database))


########################################################################################
# Uncomment these lines to test your model on the training and dev sets:
########################################################################################

# testModel(predictIncomeMyName, Database("Training"))
# testModel(predictIncomeMyName, Database("Dev"))
