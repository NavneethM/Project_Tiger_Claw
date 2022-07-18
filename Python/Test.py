#Test version 3.0
import sys
import random
import json
import os
import time
sys.path.append(".")
from Question_Bank import QuestionBank, Question
from Art import *

class Quiz:
    def __init__(self):
        self.score = 0
        self.questionPool = []
        self.currentQuestion = 0 
        self.length = 0 #user selected lenght
        self.hardMode = False
        self.currentChance = 1
        self.retries = 3
        self.testVersion = ""
        self.infinityTries = False

    def __dir__(self):
        return [
            "score",
            "questionPool",
            "currentQuestion",
            "length",
            "hardMode",
            "currentChance",
            "retries",
            "testVersion",
            "infinityTries",
        ]

#Asks the user to select a quiz and returns a list of questions. returns false if nonvalid input is given
def quizSelection():
    "Asks the user to select a quiz and returns a tuple with a list of questions and then the test choice. returns ValueError if nonvalid input is given"
    #init prompt
    startPrompt = ""
    userChoice = ""
    numTotalQuestions = 0
    output = []
    testSelection = ""
    onlyOne = ""
    seen = set()
    dupliList = set()
    dupli = ""

    #loop forever until they get it together
    while True:
        #loop through all of the available tests and give # of questions
        i = 0
        startPrompt = """
╔═══════════════════════╗
║ Please select a test: ║
╚═══════════════════════╝ 

"""
        while i < len(QuestionBank.quiz_choices):
            startPrompt += str(i + 1) + ". " + QuestionBank.quiz_choices[i][0] 
            startPrompt += " (" + str(len(getattr(QuestionBank, (QuestionBank.quiz_choices[i][1] + "_questions")))) + " questions)\n"
            #keep track of total # of questions for the all option at the end
            numTotalQuestions += len(getattr(QuestionBank, (QuestionBank.quiz_choices[i][1] + "_questions")))
            i += 1
        #add the all option at the end
        startPrompt += str(i + 1) + ". All (" + str(numTotalQuestions) + " questions)\n"

        #multiselect option
        startPrompt += str(i + 2) + ". Multiselect\n"
        
        #let user decide
        userChoice = input(startPrompt)

        #if user quits give false
        if userChoice.lower() == "q":
            return False

        #validate int was input
        try:
            numSelect = int(userChoice)
        except ValueError:
            print("Please pick a number or q to quit")
            time.sleep(3)
            continue
        
        #if an int is selected, but not a valid choice
        if (numSelect < 1) or (numSelect > (len(QuestionBank.quiz_choices) + 2)):
            print("Please make a valid selection next time doofus or q to quit")
            time.sleep(3)
            continue

        #All option is selected
        elif numSelect == (len(QuestionBank.quiz_choices) + 1): 
            #Loop through every quiz
            for quiz in QuestionBank.quiz_choices:
                #loop through every question to add to output
                for question in getattr(QuestionBank, (quiz[1] + "_questions")):
                    output.append(question)
                testSelection = "All"
            return (output, testSelection)

        #Multiselect option is selected
        elif numSelect == (len(QuestionBank.quiz_choices) + 2):
            while True:
                multi = input("Enter the number of the quizes you would like to do seperated by a space:\n")

                if multi.lower() == "q":
                    break

                multiList = multi.split()
                

                for num in set(multiList):
                    try:
                        quizNum = int(num)
                    except ValueError:
                        print("Please follow directions or q to quit")
                        multiGood = False
                        break

                    if quizNum == (len(QuestionBank.quiz_choices) + 1):
                        print("All is not an option. Try again or q to quit")
                        multiGood = False
                        break
                    elif (quizNum < 1) or (quizNum > (len(QuestionBank.quiz_choices))):
                        print("Pick valid choices next time")
                        multiGood = False
                        break
                    elif len(multiList) == 1:
                        onlyOne = input("you selected only one quiz, is that what you wanted? (<enter> or y)")
                        if onlyOne.lower() != "y":
                            print("Do it right next time then")
                            multiGood = False
                            break
                    
                    for question in getattr(QuestionBank, (QuestionBank.quiz_choices[quizNum - 1][1] + "_questions")):
                        output.append(question)
                    testSelection += QuestionBank.quiz_choices[quizNum - 1][0] + ", "
                    multiGood = True 
                
                if multiGood != False:
                    #get rid of last comma in test selection
                    testSelection = testSelection[0:-1]

                    if len(multiList) != len(set(multiList)):
                        for qz in multiList:
                            if qz in seen:
                                dupliList.add(qz)
                            
                            seen.add(qz)

                        for dup in dupliList:
                            dupli += QuestionBank.quiz_choices[int(dup) - 1][0] + ", "

                        print("You selected " + dupli[0:-2] + " multiple times. Each was only added once.")
                    print("You selected test(s): " + testSelection)

                    if len(multiList) != 1:
                        testSelection = "MutliTest: " + testSelection

                    return (output, testSelection)

                continue


        #any other choice
        else:
            for question in getattr(QuestionBank, (QuestionBank.quiz_choices[numSelect - 1][1] + "_questions")):
                output.append(question)
            testSelection = QuestionBank.quiz_choices[numSelect - 1][0]
            return (output, testSelection)

def saveQuiz(Qz):
    "Takes a quiz object input and saves into a JSON txt file. Returns True on a success and False on a fail"

    #convert the questionPools Questions objects into a list that JSON can encode
    for i in range(len(Qz.questionPool)):
        Qz.questionPool[i] = [Qz.questionPool[i].prompt, Qz.questionPool[i].answer]

    #create a dictionary for JSON
    savedQz = {
        "score": Qz.score,
        "questionPool": Qz.questionPool,
        "currentQuestion": Qz.currentQuestion,
        "length": Qz.length,
        "hardMode": Qz.hardMode,
        "currentChance": Qz.currentChance,
        "retries": Qz.retries,
        "testVersion": Qz.testVersion,
        "infinityTries": Qz.infinityTries,
    }

    while True:
        #let user exit
        myBad = input("Press enter to input save name or q to quit: ")
        if myBad.lower() == "q":
            return False

        #get filename from user
        fName = input("Input save name: ")

        #complete filename in current working directory
        f = os.getcwd() + "/" + fName + ".txt"

        if os.path.exists(f):
            retry = input("The file already exists, would you like to overwrite? (<enter> or n):  ")
            if retry.lower() == "n":
                noMore = input("Then would you like to quit? (<enter> or y):  ")
                if noMore.lower() == "y":
                    return False
                else:
                    continue

        try:
            #open file created by user and put in JSON information
            with open(f, 'w') as json_file:
                json.dump(savedQz, json_file)
                return True
        
        except:
            tryAgain = input("Something went wrong, would you like to try again? (<enter> or n) ")
            if tryAgain == "n":
                return False
            continue

def findAnswer(quest):
    "input a Question type and returns a tuple of multi choice possibilities or the answer if not a multi choice"
    multChoice = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    #alphAns and numAns only change if it is multiple choice and it mathces
    alphAns = quest.answer
    numAns = quest.answer

    #Test if question is multichoice
    if "A - " in quest.prompt:
        strChoices = quest.prompt[quest.prompt.find("A - "):quest.prompt.find("\n[+]")]
        choiceList = strChoices.split("\n ")

        for choice in choiceList:
            choiceSplit = choice.split(" - ")
            if choiceSplit[1].lower() == quest.answer.lower():
                alphAns = choiceSplit[0]
                numAns = str(multChoice.index(alphAns) + 1)
                break

    return (alphAns, numAns)

#The moneymaker
def run_quiz():
    #initialize variables
    qNum = ""
    redoPrompt = ""
    eq84 = "\n" + 84*("=") + "\n"
    qz1 = Quiz()
    sessionPool = []
    quizLoaded = False
    restart = False
    
    print(Art.introArt)
    toolbar_width = 86

    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1))

    for i in range(1,toolbar_width):
        time.sleep(.02)
        sys.stdout.write("-")
        sys.stdout.flush()

    sys.stdout.write("-\n")
    Art.ranArt()

    userLoad = input("[+]> ")
    if userLoad.lower() == "y":
        #loop forever until they get it together
        while True:
            #ask user for file to load from current working directory
            fName = input("please give file name to load(only .txt and do not add .txt): ")

            #correct filepath for successful load
            f = os.getcwd() + "/" + fName + ".txt"

            #attempt to open file
            try:
                #use with in order to close file once complete
                with open(f, "r") as f1:
                    data = json.load(f1)

                #Check to see if file loaded is a Quiz object
                if set(dir(Quiz())) != set(list(data.keys())):
                    raise TypeError

                loadOK = True #set to true in order to load
                #break to FULLY LOADED
                break

            except FileNotFoundError:
                #if file does not exist, ask if user wants to try another file
                tryAgain = input("File does not exist, would you like to select another? ")

                if (tryAgain.lower() == "n") or (tryAgain.lower() == "no"):
                    loadOK = False
                    break
                #Try while loop again if yes
                continue

            except TypeError:
                #file successfully exists/opens, but is not a quiz
                tryAgain = input("The Quiz is corrupt, would you like to select another? ")

                if (tryAgain.lower() == "n") or (tryAgain.lower() == "no"):
                    loadOK = False
                    #break to FULLY LOADED
                    break
                #try the while loop again if yes
                continue

            except:
                #something else went wrong
                tryAgain = input("Something went wrong, would you like to select another? ")

                if (tryAgain.lower() == "n") or (tryAgain.lower() == "no"):
                    loadOK = False
                    #break to FULLY LOADED
                    break
                #try the while loop again if yes
                continue

        #FULLY LOADED    
        if loadOK == True:
            #delete the save file
            os.remove(f)

            #load quiz data from file
            qz1.score = data.get("score")
            qz1.questionPool = data.get("questionPool")
            qz1.currentQuestion = data.get("currentQuestion")
            qz1.length = data.get("length")
            qz1.hardMode = data.get("hardMode")
            qz1.currentChance = data.get("currentChance")
            qz1.retries = data.get("retries")
            qz1.testVersion = data.get("testVersion")
            qz1.infinityTries = data.get("infinityTries")

            #convert questionPool from JSON readable lists back into Question objects
            for i in range(len(qz1.questionPool)):
                qz1.questionPool[i] = Question(qz1.questionPool[i][0], qz1.questionPool[i][1])

            #inform user of success and loaded quiz settings
            if qz1.hardMode == True:
                loadResult = "\nQuiz Loaded. You are in test mode on "
            else:
                loadResult = "\nQuiz loaded. You are in practice mode with " + str(qz1.retries) + " per question on "
            loadResult += "question " + str(qz1.currentQuestion + 1) + " out of " + str(qz1.length)
            loadResult += " in the " + qz1.testVersion + " quiz."

            print(loadResult)
            quizLoaded = True

        #Quiz failed to load ask user if they would like start a new quiz    
        else:
            loadResult = "Quiz loading failed, would you like to start a new quiz? "
            tryAgain = input(loadResult)
            if (tryAgain.lower() == "n") or (tryAgain.lower() == "no"):
                #quit quiz if user decides not to
                return print(finishIt())
            
            else:
                #new quiz setup
                output = "starting new Quiz"
                print(output)
                quizLoaded = False
    else:
        quizLoaded = False

    while True:
        #init quiz if user wants to start new or load fails
        if (quizLoaded == False) and (restart == False): #
            #Let a user pick a quiz, should be pretty obvious
            #QUESTION BANK HAS TO BE SAVED IN SAME FOLDER TO WORK
            initQuiz = quizSelection()

            #user makes invalid selection
            if initQuiz == False:
                return print(finishIt())

            #set options to correct quiz attribute
            qz1.questionPool = initQuiz[0]
            qz1.testVersion = initQuiz[1]

            #Let user input how many questions they want and test for valid input
            while True:
                numQuestions = input("How many questions would you like to answer? ")
                #if the user wants to quit
                if numQuestions.lower() == "q":
                    return print(finishIt())
                elif numQuestions.lower() == ".":
                    numQuestions = str(len(qz1.questionPool))

                try:
                    qz1.length = int(numQuestions)
                    break
                except ValueError:
                    print("Please input a number or press q to quit")
                    continue
            
            #If user selects a number larger than the quiz size, give all questions
            if qz1.length > len(qz1.questionPool):
                qz1.length = len(qz1.questionPool)
                tooMuch = "Appreciate your enthusiasm, but there are only " + str(qz1.length)
                tooMuch += " questions so that's how many you'll do."
                print(tooMuch)
            #exit (with sass) if negative or 0
            elif qz1.length <= 0:
                return print("Then why are you here?" + finishIt())

            #Test mode or quiz mode
            testVersion = input("Do you want test mode (no retries)? <enter> or y: ")
            if (testVersion.lower() == "y") or (testVersion.lower() == "yes") or (testVersion.lower() == "."):
                qz1.hardMode = True
                print("Hard mode activated, you poor fool")
            else:
                qz1.hardMode = False
                
                while True:
                    retries = input("How many tries do you want per question? Pick a number less then 5 or i if you want to sit here until you get it right: ")

                    #if the user hates themselves and wants infinite retries
                    if retries.lower() == "i":
                            qz1.infinityTries = True
                            print("That's a bold strategy, Cotton. Let's see if it pays off for 'em")
                            break

                    #test for valid intput (that was a typo but its a pun that makes me giggle now)
                    try:
                        bleh = int(retries)

                        #They do it right
                        if bleh <= 5 and bleh > 1:
                            qz1.retries = bleh
                            print("Starting practice mode ("+ str(qz1.retries - 1) + " retries). Good luck!")
                            break

                        #The user really just wants Hard mode
                        elif bleh == 1:
                            qz1.hardMode = True
                            print("You know this is just Hard mode right, suit yourself.")
                            break

                        #User picks something less than 0 or greather than 5
                        else:
                            raise Exception

                    #not a valid choice
                    except:
                        beingDifficult = input("Stop wasting my time, I'm not even supposed to be here today! press q to quit: ")
                        #user no longer wants to play this game
                        if beingDifficult.lower() == "q":
                            return print(finishIt())
                        
                        #or do it until they get it together
                        else:
                            continue

            #Shuffles selection order of ENTIRE quiz
            random.shuffle(qz1.questionPool)

            #set other quiz attributes to correct starting position
            qz1.score = 0
            qz1.currentQuestion = 0
            qz1.currentChance = 1

        #reset session pool for restarts
        sessionPool = []

        #set the current iterable question list
        for i in range(qz1.currentQuestion, qz1.length):
            sessionPool.append(qz1.questionPool[i])

        #The actual quiz
        for question in sessionPool:
            qz1.currentQuestion += 1
            qz1.currentChance = 1 #reset the number of chances for each question

            #get multichoice answer
            multAns = findAnswer(question)

            while qz1.currentChance <= qz1.retries:
                qNum = "Question " + str(qz1.currentQuestion) + " of " + str(qz1.length) + "\n"
                answer = input(eq84 + qNum + question.prompt) #get the user's answer

                if (answer.lower() == question.answer.lower()) or (answer.lower() == multAns[0].lower()) or (answer.lower() == multAns[1].lower()):
                    print("Correct (" + multAns[0] + ")")
                    qz1.score += 1
                    #Breaks to #KEEP GOING (outside of the while loop)
                    break
                
                #user got it wrong and has no retries or test mode is on
                if (qz1.hardMode == True) or (qz1.currentChance == qz1.retries):
                    print("Incorrect, the correct answer is " + question.answer + " (" + multAns[0] + ")")
                    #Breaks to #KEEP GOING (outside of the while loop)
                    break
                
                #set the remaining retries correctly
                if qz1.infinityTries == True:
                    qz1.currentChance -= 1 #so we can do this forever
                    remaining = "infinite"
                else:
                    remaining = str(qz1.retries - qz1.currentChance)

                #user got it wrong and has retries, ask if they want to try again
                userRetry = input("Incorrect, you have " + remaining + " attempt(s) remaining. Would you like to retry the question?  ")

                #user does not want to try question again
                if (userRetry.lower() == "n") or (userRetry.lower() == "no"):
                    print("The correct answer is " + question.answer + " (" + multAns[0] + ")")
                    #Breaks to #KEEP GOING (outside of the while loop)
                    break

                #user gets incorrect and wishes to try again
                qz1.currentChance += 1
            
            #KEEP GOING
            #Asks if the user wants to keep going if there are questions left
            if qz1.currentQuestion != qz1.length:
                userCont = input("Do you want to continue? (<enter> or n)  ")
                #user does not want to continue
                if ((userCont.lower() == "n") or (userCont.lower() == "no")):
                    userSave = input("Would you like to save your progress? (<enter> or y)  ")
                    #user wants to save
                    if userSave.lower() == "y":
                        saveOK = saveQuiz(qz1)
                        if saveOK == True:
                            return print("File saved\n\n" + finishIt())

                        #shenanigans happen with the saving (this is just in case for now)
                        else:
                            whoops = input("Sorry about that, do you wanna finish the quiz? (<enter> or y):  ")
                            if whoops == "y":
                                #on with the quiz
                                continue

                            #Break out to #RAGEQUIT (outside of for loop) to get score
                            break

                    #user does not want to save
                    else:
                        #Break out to #RAGEQUIT (outside of for loop)
                        break

        #RAGEQUIT
        #Calculate the results and give final screen
        final = qz1.score/(qz1.length)*100
        result = str("You got a " + str(round(final, 2)) + "% ")
        result += "\nYou missed " + str(qz1.length-qz1.score) + " question(s) out of " + str(qz1.length)
        result += ".\nYou correctly answered " + str(qz1.score) + " question(s)"
        print("\n\n" + boxThis(result, 1))
        time.sleep(1)

        redoPrompt = "\n\nWould you like to keep going?"
        redoPrompt += "\n\t>enter r to restart the same quiz"
        redoPrompt += "\n\t>enter n to start a new quiz"
        redoPrompt += "\n\t>press any other key to quit"
        print(redoPrompt)

        redo = input("\n[+]> ")

        if redo.lower() == "r":
			#reset required quiz attributes
            qz1.score = 0
            qz1.currentQuestion = 0
            restart = True
            continue
			
        elif redo.lower() == "n":
            restart = False
            continue
        else:
            return print(finishIt())

#So it runs when file is opened    
run_quiz()