# 6.00 Problem Set 8
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time:
#

import time
import copy

SUBJECT_FILENAME = "subjects.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    # The following sample code reads lines from the specified file and prints
    # each one.
    Dict_subjects={}
    value, work=0, 0
    inputFile = open(filename)
    for line in inputFile:
#        print("line", line)
        stripped_line=line.strip()
#        print("stripped_line", stripped_line)
        usable_line=stripped_line.split(",")
#        print("usable_line", usable_line)
        value=int(usable_line[1])
#        print("value", value)
        work=int(usable_line[2])
#        print("Work", work)

        Dict_subjects[usable_line[0]]=value, work
#        print("usable line[0]", Dict_subjects[usable_line[0]])
#        print("usable line[1]", Dict_subjects[usable_line[1]])

#    print(Dict_subjects)
    return Dict_subjects
    # TODO: Instead of printing each line, modify the above to parse the name,
    # value, and work of each subject and create a dictionary mapping the name
    # to the (value, work).

loadSubjects(SUBJECT_FILENAME)

Global_Dict_Subjects=loadSubjects(SUBJECT_FILENAME)
#print(Global_Dict_Subjects)

def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    sorted(subNames)
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print(res)

#printSubjects(Global_Dict_Subjects)

def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return  val1 > val2

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return  work1 < work2

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return float(val1) / work1 > float(val2) / work2

#
# Problem 2: Subject Selection By Greedy Optimization
#
def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """
    # TODO...
    Study_plan={}
    WorkingHours=0
    compare_key_list=list(subjects.keys())
    compare_key=compare_key_list[0]
    compare_key_value=subjects[compare_key]
    copy_subjects={}
    Total_work=0
    numCalls=0

    start_time=time.time()

    while Total_work<=maxWork:
        for key,value in subjects.items():
            numCalls+=1
            #print("Compare_key_value", compare_key_value, "key, value", key, value)
            if comparator(value, compare_key_value):
#                print("Compare_key", compare_key)
#                print("compare_key_value", compare_key_value)
#                print("key", key)
#                print("value", value, "value[1]", value[1])
#                print("True")
                compare_key=key
                compare_key_value=value
#            else:
#                print("Compare_key", compare_key)
#                print("compare_key_value", compare_key_value)
#                print("False")

        if Total_work+compare_key_value[1]<=maxWork:
            Total_work+=compare_key_value[1]
            Study_plan[compare_key]=compare_key_value
#            print("Total_work", Total_work)
#            print("Study_plan", Study_plan)
        copy_subjects=copy.deepcopy(subjects)
        copy_subjects.pop(compare_key,None)
        subjects=copy_subjects
        compare_key_list=list(subjects.keys())
        if compare_key_list==[]:
            break
        compare_key=compare_key_list[0]
        compare_key_value=subjects[compare_key]
#    print("With comparator:", comparator)
#    print("Final Study Plan", Study_plan)
#    print("Total_work", Total_work)
    printSubjects(Study_plan)

    end_time=time.time()
    print("total time", end_time-start_time)
    print("numCalls:", numCalls)
    return Study_plan


#print(Global_Dict_Subjects)


greedyAdvisor(Global_Dict_Subjects, 15, cmpValue)

def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    nameList = subjects.keys()
    tupleList = subjects.values()
    bestSubset, bestSubsetValue = \
            bruteForceAdvisorHelper(list(tupleList), maxWork, 0, None, None, [], 0, 0)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[list(nameList)[i]] = list(tupleList)[i]
    return outputSubjects

def bruteForceAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork):
    # Hit the end of the list.
#    print("Subjects", subjects, type(subjects))
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
            return subset[:], subsetValue
        else:
            # Keep the current best.
            return bestSubset, bestSubsetValue
    else:
        s = subjects[i]
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
            subset.pop()
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork)
        return bestSubset, bestSubsetValue

#
# Problem 3: Subject Selection By Brute Force
#
def bruteForceTime():
    """
    Runs tests on bruteForceAdvisor and measures the time required to compute
    an answer.
    """
    # TODO...
    start_time=time.time()
    bruteForceAdvisor(Global_Dict_Subjects, 15)
    end_time=time.time()
    total_time=end_time-start_time
    print("Total time", total_time)

#bruteForceTime()

# Problem 3 Observations
# ======================
#
# TODO: write here your observations regarding bruteForceTime's performance

#
# Problem 4: Subject Selection By Dynamic Programming
#
def dpAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work) that contains a
    set of subjects that provides the maximum value without exceeding maxWork.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    # TODO...
    memo={}
    Study_plan={}
    WorkingHours=0
    compare_key_list=list(subjects.keys())
    compare_key=compare_key_list[0]
    compare_key_value=subjects[compare_key]
    copy_subjects={}
    Total_work=0


    start_time=time.time()
    while Total_work<=maxWork:
        for key,value in subjects.items():
            #print("Compare_key_value", compare_key_value, "key, value", key, value)
            if not (value, compare_key_value) in memo:
                if cmpValue(value, compare_key_value):
#                   print("Compare_key", compare_key)
#                   print("compare_key_value", compare_key_value)
#                   print("key", key)
#                   print("value", value, "value[1]", value[1])
#                   print("True")
                    memo[value, compare_key_value]=cmpValue(value, compare_key_value)
                    compare_key=key
                    compare_key_value=value
                else:
                    memo[value, compare_key_value]=cmpValue(value, compare_key_value)
#                   print("Compare_key", compare_key)
#                   print("compare_key_value", compare_key_value)
#                   print("False")
            elif memo[value, compare_key_value]==True:
                compare_key=key
                compare_key_value=value


        if Total_work+compare_key_value[1]<=maxWork:
            Total_work+=compare_key_value[1]
            Study_plan[compare_key]=compare_key_value
#           print("Total_work", Total_work)
#           print("Study_plan", Study_plan)
        copy_subjects=copy.deepcopy(subjects)
        copy_subjects.pop(compare_key,None)
        subjects=copy_subjects
        compare_key_list=list(subjects.keys())
        if compare_key_list==[]:
            break
        compare_key=compare_key_list[0]
        compare_key_value=subjects[compare_key]
#    print("With comparator:", comparator)
#    print("Final Study Plan", Study_plan)
#    print("Total_work", Total_work)
    #print("memo", memo)
    printSubjects(Study_plan)
    end_time=time.time()
    print("total time", end_time-start_time)



    return Study_plan

dpAdvisor(Global_Dict_Subjects, 15)

#
# Problem 5: Performance Comparison
#
def dpTime():
    """
    Runs tests on dpAdvisor and measures the time required to compute an
    answer.
    """
    # TODO...

# Problem 5 Observations
# ======================
#
# TODO: write here your observations regarding dpAdvisor's performance and
# how its performance compares to that of bruteForceAdvisor.
