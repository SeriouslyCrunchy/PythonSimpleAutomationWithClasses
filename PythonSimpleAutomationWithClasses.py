#List of main commands that can be added to the command list and so require classes : click, drag, text, runTask, closeTask, wait 
#Other commands that cannot be added to the command list : printHelp, showPoint, viewList, executeCommands, finish
import pyautogui, subprocess, time, sys, subprocess #imports the python automation module

class Command():    #base class that defines a command
    def __init__(self,commandID,commandName):   #initialises basic command values, all commands will have commandID and name
        self.commandName=commandName
        self.commandID=commandID
    def executeCommand(self):  #all Commands will have an execute command, but child commands with the execute method will override this
        print('executing...')
    def showCommand(self):  #all Commands will have an show command, but child commands with the execute method will override this
        print('printing...')

class ClickCommand(Command):      #derived class 1, handles a standard click
    def __init__(self,commandID, commandName, xLocation,yLocation):  #child init overrides parent
        super().__init__(commandID, commandName)    #can use super to inherit some aspects of parent class
        self.xLocation=xLocation  #takes passed in values when initalised
        self.yLocation=yLocation  
    def executeCommand(self):
        pyautogui.click(x=int(self.xLocation),y=int(self.yLocation))
    def showCommand(self):
        print('Command number ' + str(self.commandID) + ' : ' + self.commandName + ' at ' + str(self.xLocation) +', ' + str(self.yLocation))

class DragCommand(Command):      #derived class 2, handles a drag from one point to another
    def __init__(self,commandID, commandName, xLocationStart,yLocationStart,xLocationEnd,yLocationEnd):  #child init overrides parent
        super().__init__(commandID, commandName)    #can use super to inherit some aspects of parent class
        self.xLocationStart=xLocationStart  #takes passed in values when initalised
        self.yLocationStart=yLocationStart  
        self.xLocationEnd=xLocationEnd
        self.yLocationEnd=yLocationEnd
    def executeCommand(self):
        pyautogui.moveTo(x=int(self.xLocationStart),y=int(self.yLocationStart))
        pyautogui.dragTo(x=int(self.xLocationEnd),y=int(self.yLocationEnd))
    def showCommand(self):
        print('Command number ' + str(self.commandID) + ' : ' + self.commandName + ' at ' +str(self.xLocationEnd)+', ' +str(self.yLocationEnd))

class TextCommand(Command):      #derived class 3, allows entering of text
    def __init__(self,commandID, commandName, textInput):  #child init overrides parent
        super().__init__(commandID, commandName)    #can use super to inherit some aspects of parent class
        self.textInput=textInput  #takes passed in values when initalised  
    def executeCommand(self):
        pyautogui.typewrite(self.textInput)
    def showCommand(self):
        print('Command number ' + str(self.commandID) + ' : ' + self.commandName + ' with value ' +self.textInput)

class OpenFileCommand(Command):      #derived class 4, opens a specific file
    def __init__(self,commandID, commandName, fileName):  #child init overrides parent
        super().__init__(commandID, commandName)    #can use super to inherit some aspects of parent class
        self.fileName=fileName  #takes passed in values when initalised  
    def executeCommand(self):
        subprocess.Popen(self.fileName)
    def showCommand(self):
        print('Command number ' + str(self.commandID) + ' : ' + self.commandName + ' with value ' +self.fileName)

class KillProcessCommand(Command):      #derived class 5, terminates a process
    def __init__(self,commandID, commandName, processName):  #child init overrides parent
        super().__init__(commandID, commandName)    #can use super to inherit some aspects of parent class
        self.processName=processName  #takes passed in values when initalised  
    def executeCommand(self):
        subprocess.run(['taskkill.exe', '/im', self.processName])
    def showCommand(self):
        print('Command number ' + str(self.commandID) + ' : ' + self.commandName + ' with value ' +self.processName)

class WaitCommand(Command):      #derived class 6, wait
    def __init__(self,commandID, commandName, waitTime):  #child init overrides parent
        super().__init__(commandID, commandName)    #can use super to inherit some aspects of parent class
        self.waitTime=waitTime  #takes passed in values when initalised  
    def executeCommand(self):
        time.sleep(int(self.waitTime))
    def showCommand(self):
        print('Command number ' + str(self.commandID) + ' : ' + self.commandName + ' with value ' +str(self.waitTime))

#The following commands are run instantly when requested and do not require classes to be made : printHelp, showPoint, viewList, executeCommands, finish

def printHelp() :
    print('Command list :')
    print('Automation commands :')
    print('clickPoint, dragBetweenPoints, enterText, openFile, endProcess, wait')
    print('Other commands :')
    print('printHelp, viewList, showPoint, runCommands, finish')

def showPoint() :   #shows the mouse location at the moment the user completes the input line
    print('Place mouse pointer and then hit enter to show the co-ordinate')
    acceptAnyInput = input()
    mouseLocation = pyautogui.position()
    print(mouseLocation)

def runCommands() :
    print('Running command list...')
    for i in range(len(commandList)) : 
        time.sleep(1)
        commandList[i].showCommand()
        time.sleep(1)
        commandList[i].executeCommand()
    
def viewList() :
    print('Printing current command list...')
    for i in range(len(commandList)) : 
        commandList[i].showCommand()

def finish() :
    print('Shutting down...')
    sys.exit()

def addCommand(commandID,commandName,values) :
    global currentCommandID
    print('Adding command ' + commandName)
    if commandName=='clickPoint':
        xLocation=values[0]
        yLocation=values[1]
        newCommand=ClickCommand(commandID,commandName,xLocation,yLocation)
        commandList.append(newCommand)
        currentCommandID+=1
    if commandName=='dragBetweenPoints':
        xLocationStart=values[0]
        yLocationStart=values[1]
        xLocationEnd=values[2]
        yLocationEnd=values[3]
        newCommand=DragCommand(commandID,commandName,xLocationStart,yLocationStart,xLocationEnd,yLocationEnd)
        commandList.append(newCommand)
        currentCommandID+=1
    if commandName=='enterText':
        textInput=values
        newCommand=TextCommand(commandID,commandName,textInput)
        commandList.append(newCommand)
        currentCommandID+=1
    if commandName=='openFile':
        textInput=values
        newCommand=OpenFileCommand(commandID,commandName,textInput)
        commandList.append(newCommand)
        currentCommandID+=1
    if commandName=='endProcess':
        textInput=values
        newCommand=KillProcessCommand(commandID,commandName,textInput)
        commandList.append(newCommand)
        currentCommandID+=1
    if commandName=='wait':
        waitInput=values
        newCommand=WaitCommand(commandID,commandName,waitInput)
        commandList.append(newCommand)
        currentCommandID+=1

#Startup and welcome
print('Welcome to Crunch Simple Automation! Now with classes and inheritance!')
print('Command list :')
print('Automation commands :')
print('clickPoint, dragBetweenPoints, enterText, openFile, endProcess, wait')
print('Other commands :')
print('printHelp, viewList, showPoint, runCommands, finish')
currentCommandID = 0   #tracks command number in the list
commandList : list[Command] = [] #creates an empty list of command classes
while True :    #this loop is always on until the program is closed
    print('')
    print('Current command : ' + str(currentCommandID))
    print('Enter a command')
    userInput=input()
    match userInput: #basic match case
        case 'clickPoint':
            print('Click at what point? Enter X coordinate followed by a "," and then the Y coordinate')
            values = input().split(",")
            commandName = userInput
            addCommand(currentCommandID, commandName, values)
        case 'dragBetweenPoints':
            print('Drag between what points? Enter start X coordinate, start Y coordinate, end X coordinate, and end Y coordinates, separated by ","')
            values = input().split(",")
            commandName = userInput
            addCommand(currentCommandID, commandName, values)
        case 'enterText':
            print('Enter the text you wish to enter')
            values = input()
            commandName = userInput
            addCommand(currentCommandID, commandName, values)
        case 'openFile':
            print('Enter in full file path to what you would like to open, including extension')
            values = input()
            commandName = userInput
            addCommand(currentCommandID, commandName, values)
        case 'endProcess':
            print('Enter in process name that you would like to close')
            values = input()
            commandName = userInput
            addCommand(currentCommandID, commandName, values)
        case 'wait':
            print('Enter in how long you would like to wait in seconds')
            values = input()
            commandName = userInput
            addCommand(currentCommandID, commandName, values)
        case 'printHelp':
            printHelp()
        case 'viewList':
            viewList()
        case 'showPoint':
            showPoint()
        case 'runCommands':
            runCommands()
        case 'finish':
            finish()
        # default pattern
        case _:
            print("Input not recognised")
    