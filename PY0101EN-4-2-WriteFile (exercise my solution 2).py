# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 20:33:55 2022

@author: Wilson Wei
"""

#Run this prior to starting the exercise
from random import randint as rnd

memReg = 'members.txt'
exReg = 'inactive.txt'
fee =('yes','no')

def genFiles(current,old):
    with open(current,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(20):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[rnd(0,1)]))


    with open(old,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[1]))


genFiles(memReg,exReg)


# The below was my solution 2

def cleanFiles(currentMem,exMem):
    '''
    currentMem: File containing list of current members
    exMem: File containing list of old members
    
    Removes all rows from currentMem containing 'no' and appends them to exMem
    '''
    
    with open(currentMem, 'r+') as currentMemfile:
        with open(exMem, 'a+') as exMemfile:
            cList = currentMemfile.readlines()
            print(cList)
            activeMem = [] # The list for storing data of active member # At the end of the code cList = activeMem
            inactiveMem = [] # The list for storing data of inactive member
            
            activeMem.append(cList[0]) # Append the header as later i will need to overwrite the currentMem
            # No need to add the header for inactiveMem as later i will just need to append the data to exMemfile
            for i in range(len(cList)):
                if 'yes' in cList[i]:
                    activeMem.append(cList[i])
                elif 'no' in cList[i]:
                    inactiveMem.append(cList[i])
            # Start to overwrite the currentMem
            # Firstly, need to move the cursor back to the beginning
            currentMemfile.seek(0)
            # Secondly, use for loop
            for member in activeMem:
                currentMemfile.write(member)
            # Thirdly, need to cut/remove the redundant pre-existing data
            currentMemfile.truncate()
            
            # Start to append the data to the exMem
            for member in inactiveMem:
                exMemfile.write(member)
                    
                
                
                


# Code to help you see the files
# Leave as is
memReg = 'members.txt'
exReg = 'inactive.txt'
cleanFiles(memReg,exReg)


headers = "Membership No  Date Joined  Active  \n"
with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())
    
with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())
                
# The below verifies my defined cleanFiles function
def testMsg(passed):
    if passed:
       return 'Test Passed'
    else :
       return 'Test Failed'

testWrite = "testWrite.txt"
testAppend = "testAppend.txt" 
passed = True

genFiles(testWrite,testAppend)

with open(testWrite,'r') as file:
    ogWrite = file.readlines()

with open(testAppend,'r') as file:
    ogAppend = file.readlines()

try:
    cleanFiles(testWrite,testAppend)
except:
    print('Error')

with open(testWrite,'r') as file:
    clWrite = file.readlines()

with open(testAppend,'r') as file:
    clAppend = file.readlines()
        
# checking if total no of rows is same, including headers

if (len(ogWrite) + len(ogAppend) != len(clWrite) + len(clAppend)):
    print("The number of rows do not add up. Make sure your final files have the same header and format.")
    passed = False
    
for line in clWrite:
    if  'no' in line:
        passed = False
        print("Inactive members in file")
        break
    else:
        if line not in ogWrite:
            print("Data in file does not match original file")
            passed = False
print ("{}".format(testMsg(passed)))
    
