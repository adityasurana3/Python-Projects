from time import *
import random

def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error+1
        except:
            error = error+1
    return error

def speed(time_s,time_e,userinput):
    time_delay = time_e -  time_s
    time_R = round(time_delay)
    speed = len(userinput)/time_R
    return round(speed)


while True:
    ck = input("ready to test: yes / no: ")
    if ck == "yes" or ck == "y":
        test = [" sequence of sentences representing an idea or explaining a topic in the most organized fashion is called a paragraph","Paragraph writing pertains to a single issue at a time. All matter relevant to the topic has to be clearly explained in a section in a proper flow", "While writing paragraphs, it is essential to care for the target audience","Students are mostly beneficial candidates of paragraphs as they look out for relevant information while crafting essays"]
        test1 = random.choice(test)
        print("*****typing speed*****")
        print(test1)
        print()
        print()
        time_1 = time()
        testinput= input("Enter: ")
        time_2 = time()

        print("Speed:", speed(time_1,time_2,testinput), "w/sec")
        print("Error:", mistake(test1,testinput))
        zero_error = mistake(test1,testinput)
        if zero_error == 0:
            print("Congratulation you have typed the sentence with Zero Error")
    elif ck == "no" or ck == "n":
        print("Thank you for using the typing speed")
        break
    else:
        print("Wrong Input")