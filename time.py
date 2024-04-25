import time
print("              this programme is for you.")
print()

# timestamp = time.strftime('%H:%M:%S')
newtime = int(time.strftime('%H'))
#newtime = 22
# print(newtime)
if (newtime >=0 and newtime < 12 ):
    print("         \"(:hello sir very good morning , i hope you have a nice day-:)\"")
    print()
    print("but i want to know that you go for exercise daily in the morning..?")
    print()
    answer = input("please give me your answer \"yes and no\":-")
    if( answer == "yes"):
        print()
        print("-------------------what you can call me tommorow for exersice with you...?")
        print()
        again_answer = input("please give me your answer in \"yes and no\" :-")
        if again_answer == "yes" :
          print()
          print("ok this is my home address h.n= 123(jaipur,rajasthan)") 
          print()
          print("please call me tommorow , brother.!")
        else:      
           again_answer = "no"
           print()
           print('is\'s ohk enjoy your day:)')
    else :
        answer =="no"
        print("is\'s ohk have a nice day.")      
######################################################################################################################

elif (newtime >=12 and newtime < 18):
    print("\"(:-hello sir good afternoon-:) \n \n can we go for tea together...?")
    print()
    answer = input("                  please give me your answer in \"yes and no\":-")
    print()
    if (answer == "yes") :
        print("please give me your mobile number:-")
        mobile_number = input()
        print()
        print("please confirm that this is your mobile number:-",mobile_number)
        print()
        print("give me your confirmation in \"yes and no\" :-")
        confirmation = input()
        print()

        if(confirmation == "yes"):
           print("ok , i will call you after office close.")
           exit()
        else :
           (confirmation == "no" )
           print("type again your mobile number:-")
           again_mobile_number = input()
           print()
           print("ok check again:-",  again_mobile_number)
           print("what this is your mobile number..?")
           print()
        second_confirmation = input("please give me your again confirmation in \"yes and no\" :-")
        print()
        
        if second_confirmation == "yes" :
              print("ok thanks , i will call you after office close.")
              exit()
        else:
              second_confirmation == "no"
              print("sorry try again lator..!")
    else:
        (answer == "no")
        print("its ohk, thank you so much but nice to meet you.")
#######################################################################################################################


elif (newtime >=18 and newtime <= 20):
    print("\"(:-hello sir good evening-:)\"")
    print()
    print("Will you go out with me after the office is over..?")
    print()
    print("             please give me your answer in \"yes and no\":-")
    answer = input()
    if answer == "yes" :
        print("ohk tell me what is great location for enjoy in this city:-")
        city = input("type the location name:-")
        print()
        print("are your sure for this location..? - ", city ,"\ngive me your answer in \"yes and no\":-")
        new_answer = input()
        if new_answer == "yes" :
            print("ok i will come at 7 o'clock")
        elif new_answer =="no" :
            print()
            print("type again your desired location:-")
            again_answer = input()
            print()
            print("tell me again what are you sure for this location..? -" , again_answer , "\n\nplease give me your confirmation  in \"yes and no:-")
            confirmation = input()
            if confirmation == "yes" :
             print("ok i will come at 7 o'clock")
            elif confirmation == "no" :
             print("its ok we will go other time")
        else :
             exit()
    else :
        answer == "no"
        print("ohk, I will go with my another friend:)")    
####################################################################################################################


elif (newtime > 20 and newtime <= 24) :
    print("\"(:-hello sir good night take care-:)\"")
    print()
    print("but tell me:-")
    print()
    print("You will go to the garden tomorrow for morning exercise :-" )
    print()
    print("please give me your answer in \"yes and no\"..?")
    answer = input()
    if answer == "yes" :
        print()
        print("please call me in the morning for exercise with you..!")
    elif answer == "no" :
        print("its ohk good night.")
        print()
        print("But May I know that you will come to office tomorrow?..?")
        print()
        print("please give me your answer in \"yes and no\"..?")
        
        confirmation = input()
        if confirmation == "yes" :
          print()
          print("that nice, let's meet tomorrow in the office")
        elif confirmation == "no" :
            print()
            print("May I know why you are not coming to office tomorrow..?")
            print()
            print("if your are comfortable so you can give me your conformation in \"yes and no\":-")
            again_conformation = input()
            if again_conformation == "yes" :
                print()
                print("what is reason that you are not coming office tomorror:-")
                reason = input()
            else :
                again_conformation == "no"
                print()
                print("it's ohk , i can understand your feeling..)")
else :
    exit()

