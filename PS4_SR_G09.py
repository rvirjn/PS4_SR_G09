# Description: Data Structure Assignment-1
# ASSIGNMENT1_BLR_B2_G09

import re
import datetime

def initializeHash():
    """
    This function creates an empty hash table and points to null

    :return:
    """
    from hashtable import HashTable
    StudentHashRecords = HashTable()
    return StudentHashRecords


def insertStudentRec(StudentHashRecords, studentId, CGPA):
    """
    This  function  inserts  the student id and corresponding CPGA into the
    hash table. The inputs need to be read from a file inputPS4.txt which
    contains the student ID and overall graduating CGPA (decimal value
    with a maximum of 5.0 points). The file read can happen outside the
    function and only the information in every individual row needs to be
    passed to the function

    :param StudentHashRecords:
    :param studentId:
    :param CGPA:
    :return:
    """
    StudentHashRecords.put(studentId, CGPA)
    return StudentHashRecords


def hallOfFame(StudentHashRecords, CGPA):
    """
    This function prints the list of all students who have a CGPA greater
    than the CGPA passed to the function. The input CGPA can be read from
    the file promptsPS4.txt. The input can be identified with the tag
    mentioned below

    hallOfFame: 4.5

    This hall of fame list should be output in a file outputPS4.txt
    and should contain the studentid and CGPA.

    Output format:
    ----------
    hall of fame
    ----------
    Input: 4.5
    Total eligible students: 2
    Qualified students:
    2008CSE1225 / 4.5
    2008CSE1226 / 4.8
    -------------------------------------
    :param StudentHashRecords:
    :param CGPA:
    :return: Output
    """
    temp = {}
    count = 0
    output_format = "---------hall of fame-----------------------\n" \
                    "Input: {CGPA}\n" \
                    "Total eligible students: {count}\n" \
                    "Qualified students:\n" \
                    "{Qualified_students}" \
                    "-------------------------------------------------\n"

    student_format = """{key} / {value}"""
    Qualified_students = ''
    for key in StudentHashRecords.keys():
        value = StudentHashRecords.get(key)
        if value >= CGPA:
            count = count + 1
            temp[key] = value
    for key in temp.keys():
        value = StudentHashRecords.get(key)
        Qualified_students = Qualified_students + ((student_format.format(key=key, value=value))).strip() + '\n'
    output = output_format.format(CGPA=CGPA, count=count, Qualified_students=Qualified_students)
    print(output)
    temp.clear()
    return output


def newCourseList(StudentHashRecords, CGPAFrom, CPGATo):
    """
    This function prints the list of all students who have a CGPA within
    the given range and have graduated in the last 5 years. The input
    CGPAs can be read from the file promptsPS4.txt. The input can be
    identified with the tag mentioned below

    courseOffer: 3.5 : 4.0

    This list should be output to outputPS4.txt that contains the student id and CGPA.

    Output format:
    ---------- new course candidates ----------
    Input: 3.5 to 4.0
    Total eligible students: 2
    Qualified students:
    2008CSE1223 / 3.5
    2008CSE1224 / 3.9
    ------------------------------------
    :param StudentHashRecords
    :param CGPAFrom:
    :param CPGATo:
    :return: Output
    """
    temp = {}
    count = 0
    output_format = "---------new course candidates-----------------------\n" \
                    "Input: {CGPAFrom} to {CPGATo}\n" \
                    "Total eligible students: {count}\n" \
                    "Qualified students:\n" \
                    "{Qualified_students}" \
                    "-------------------------------------------------\n"
    student_format = """{key} / {value}"""
    Qualified_students = ''
    for key in StudentHashRecords.keys():
        value = StudentHashRecords.get(key)
        if CGPAFrom <= value <= CPGATo:
            count = count + 1
            temp[key] = value
    for key in temp.keys():
        value = StudentHashRecords.get(key)
        Qualified_students = Qualified_students + ((student_format.format(key=key, value=value))).strip() + '\n'

    output = output_format.format(CPGATo=CPGATo, CGPAFrom=CGPAFrom, count=count, Qualified_students=Qualified_students)
    print(output)
    temp.clear()
    return output


def depAvg(StudentHashRecords):
    """
    This function prints the list of all departments followed by the
    maximum CGPA and average CGPA of all students in that department.
    The output should be captured in outputps4.txt following format

    Output format:
    ---------- department CGPA ----------
    CSE: max: 3.5, avg: 3.4
    MEC: max: 3.5, avg: 3.4
    ECE: max: 3.5, avg: 3.4
    ARC: max: 3.5, avg: 3.4
    -------------------------------------

    (Note: the above output numbers are indicative and not actuals.)

    :param StudentHashRecords:
    :return:
    """
    CSE_max, CSE_total, CSE_numberOfRec = 0, 0, 0
    MEC_max, MEC_total, MEC_numberOfRec = 0, 0, 0
    ECE_max, ECE_total, ECE_numberOfRec = 0, 0, 0
    ARC_max, ARC_total, ARC_numberOfRec = 0, 0, 0

    output_format = "---------- department CGPA -------------\n" \
                    "{students}\n" \
                    "-----------------------------------------\n"
    student_format = """{dept}: max: {dept_max}, avg: {dept_avg}"""
    students = ''
    for key in StudentHashRecords.keys():
        value = StudentHashRecords.get(key)
        dept = re.split('(\d+)', key)[2]
        if dept == 'CSE':
            CSE_numberOfRec = CSE_numberOfRec + 1
            CSE_total = CSE_total + value
            if value > CSE_max:
                CSE_max = value
        if dept == 'MEC':
            MEC_numberOfRec = MEC_numberOfRec + 1
            MEC_total = MEC_total + value
            if value > MEC_max:
                MEC_max = value
        if dept == 'ECE':
            ECE_numberOfRec = ECE_numberOfRec + 1
            ECE_total = ECE_total + value
            if value > ECE_max:
                ECE_max = value
        if dept == 'ARC':
            ARC_numberOfRec = ARC_numberOfRec + 1
            ARC_total = ARC_total + value
            if value > ARC_max:
                ARC_max = value
    if CSE_numberOfRec:
        CSE_avg = float(CSE_total / CSE_numberOfRec)
        students = students + ((student_format.format(dept='CSE', dept_max=CSE_max,
                                                      dept_avg=round(CSE_avg, 1)))).strip() + '\n'
    if MEC_numberOfRec:
        MEC_avg = float(MEC_total / MEC_numberOfRec)
        students = students + ((student_format.format(dept='MEC', dept_max=MEC_max,
                                                      dept_avg=round(MEC_avg, 1)))).strip() + '\n'
    if ECE_numberOfRec:
        ECE_avg = float(ECE_total / ECE_numberOfRec)
        students = students + ((student_format.format(dept='ECE', dept_max=ECE_max,
                                                      dept_avg=round(ECE_avg, 1)))).strip() + '\n'
    if ARC_numberOfRec:
        ARC_avg = float(ARC_total / ARC_numberOfRec)
        students = students + ((student_format.format(dept='ARC', dept_max=ARC_max,
                                                      dept_avg=round(ARC_avg, 1)))).strip() + '\n'

    output = output_format.format(students=students)
    print(output)
    return output


def destroyHash(StudentHashRecords):
    """
    This function destroys all the entries inside hashtable.
    This is a clean-up code

    :param StudentHashRecords:
    :return:
    """
    StudentHashRecords.clear()
    return StudentHashRecords


def validate_inputPS4_txt(line):
    if '/' in line:
        arr = line.split('/')
        if len(arr) == 2:
            studentId = arr[0].strip()
            y_d_r = re.split('(\d+)', studentId)
            if len(y_d_r) != 5:
                print('Student ID is not proper hence skiping that rc %s\n' % studentId)
                raise
            dept = y_d_r[2]
            if dept not in ['CSE', 'ECE', 'ARC', 'MEC']:
                print('Student ID had not proper dept %s\n' % studentId)
                raise
            cgpa = arr[1].strip()
            try:
                cgpa = float(cgpa)
            except Exception:
                print("Enter proper cgpa value in inputPS4.txt %s\n" % line)
                raise
            return studentId, cgpa
        else:
            print('Record is not in proper format %s \n' % line)
            raise
    else:
        print('/ in missing in line %s' % line)
        raise


def validate_hallOfFame_txt():
    CGPA = None
    with open('promptsPS4.txt') as f:
        lines = f.readlines()
        for line in lines:
            if 'hallOfFame' in line:
                arrs = line.split('hallOfFame:')
                if not arrs:
                    print('Enter proper format for hallOfFame %s \n' % line)
                    raise
                if len(arrs) != 2:
                    print('Enter proper format for hallOfFame %s \n' % line)
                    raise
                CGPA = arrs[1].strip()
                try:
                    CGPA = float(CGPA)
                except Exception:
                    print("Enter proper value in promptsPS4.txt %s \n" % line)
                    raise

    if CGPA is None and not isinstance(CGPA, float):
        print("Enter proper CGPA value \n")
        raise
    return CGPA


def validate_courseOffer_txt():
    CGPAFrom, CPGATo = None, None
    with open('promptsPS4.txt') as f:
        lines = f.readlines()
        for line in lines:
            if 'courseOffer' in line:
                arrss = line.split('courseOffer:')
                if len(arrss) > 1:
                    rng = arrss[1].strip()
                else:
                    print('Enter proper format for courseOffer %s \n' % line)
                    raise
                ars = rng.split(':')
                if len(ars) != 2:
                    print('Enter proper format for courseOffer range %s \n' % line)
                    raise
                CGPAFrom = ars[0].strip()
                CPGATo = ars[1].strip()
                try:
                    CGPAFrom = float(CGPAFrom)
                    CPGATo = float(CPGATo)
                except Exception:
                    print("Enter proper value for courseOffer %s \n" % line)
                    raise

    if CGPAFrom is None and CPGATo is None and not isinstance(CGPAFrom, float) and not isinstance(CPGATo, float):
        print("Enter proper CGPAFrom, CGPATO value \n")
        raise
    return CGPAFrom, CPGATo


def writeTofile(output, file="outputPS4.txt"):
    f = open(file, "a")
    f.write(output)
    f.close()


if __name__ == "__main__":
    start_time = datetime.datetime.now()
    StudentHashRecords = initializeHash()

    # create outputPS4.txt
    open("outputPS4.txt", "w").close()

    # input for function insertStudentRec()
    with open('inputPS4.txt') as f:
        lines = f.readlines()
        for line in lines:
            studentId, cgpa = validate_inputPS4_txt(line)
            insertStudentRec(StudentHashRecords, studentId, cgpa)

    # input for function hallOfFame()
    CGPA = validate_hallOfFame_txt()
    hallOfFame_output = hallOfFame(StudentHashRecords, CGPA)
    writeTofile(hallOfFame_output)

    # input for function newCourseList()
    CGPAFrom, CPGATo = validate_courseOffer_txt()
    newCourseList_output = newCourseList(StudentHashRecords, CGPAFrom, CPGATo)
    writeTofile(newCourseList_output)

    # department CGPA
    depAvg_output = depAvg(StudentHashRecords)
    writeTofile(depAvg_output)

    # print(StudentHashRecords)

    # clean-up code
    StudentHashRecords = destroyHash(StudentHashRecords)

    # update time in Analysis
    end_time = datetime.datetime.now()
    open("analysisPS4.txt", "w").close()
    writeTofile('Hour:Min:Sec.MicroSec\n', "analysisPS4.txt")
    writeTofile(str(end_time-start_time), "analysisPS4.txt")

