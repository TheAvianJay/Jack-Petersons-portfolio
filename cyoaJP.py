#The name will make the player feel a little more immersed when he or she input their name. 
#TODO find some way to remove None when it asks for the player name.
p_name = input(print("Welcome to The hive a choose your own adventure where you will be tasked with dealing with a hive with wasps the size of a person that has poped in out of no where on the outskerts of town. What is your name?"))
print(f"your name is {p_name}")#The name adds a little bit of immersion
print("It was a bright sunny morning when you woke up. You work as an exterminator removing pests from peoples house and yards.")
print("An honest living, making peoples houses safer to live in without fear of disease or potential alergies popping up.")
print("Today is different as you waking you hear knocking at your door.")
print("What do you do? (Type in the number to select one of the choices that are avalible)")
#this variable below helps start the while loop and skip the rest of the decisions if an ending is reached
a_1 = 0
a_1c = 1 
a_1b = 1
a_1a = 1 
a_1d = 1 
a_1e = 1
a_1f = 1 
a_1g = 1 
a_1h = 1
a_1i = 1 
#start 1
while a_1 != 1 and 2:
    a_1 = int(input("1. perform your normal morning reutine 2. answer the door."))
    if a_1 == 1:
        print("")
        print("You decide to ignore the door and take your quick shower and brush your teeth")
        print("However you then heard the door knock. Hmm it apears to be someone who really needs your line of work so you finish your shower and brushing your teeth")
        print("and quickly make your breakfast and go to the door to open it.")
        a_1a = 0
        a_1 = 1
    if a_1 == 2:
        print("Deciding it would be best to open up the door and check if a new client needs some sort of pest or insect control.")
        a_1a = 0
        a_1 = 1
    else:
        print("that isn't an option. Choose one of the options presented")
print("")
#2
print("When you open the door you seek a group of people looking scared asking you for help.")
while a_1a != 1 and 2:
    print(f"One person in a fearful tone says '{p_name} there is a huge hive that appeared out in the outskirts of town with wasps that are huge and the size")
    print("of a person.' Everyone has the look of fear on their faces, but are they telling you the truth. A wasp the size of a person that can't be real, right?")
    a_1a = int(input("What do you do? 1. Listen to them.  2. Laugh and tell them that is a nice joke and close the door on them."))
    if a_1a == 1:
        print("What? Huge wasps? you asked. The person in the group then responded with 'Yes. just outside of town, we are worried about our safety and")
        print("we need you to quickly exterminate them. You have the poisons for them and likely the expertiece with these insects.")
        a_1b = 0
        a_1a = 1 
    if a_1 == 1:
        print("You tell the people that wasps the size of people arn't real and close the door. Later that day you then see huge wasps flying through town causing a havic")
        print("all over and people falling to the group it seems like it is to late as the wasps may have just taken over the town. The end.")
        print("You should have believed their story.")   
        a_1a = 1 
    else:
        print("that isn't an option. Choose one of the options presented")
print("")
# this is path A and the begining of a journey.3
while a_1b != 1 and 2:
    print("As she finshed you then see what looks like a huge wasp flying by above the group. Everyone paniced but the giant wasp flew by without interacting with anyone.")
    print("She then shouted 'THAT ONE OF THEM'. We need you to stop them now.")
    a_1a = int(input("What will you do. 1. Get your equipment and get ready 2. Ask the group a question about the giant wasps."))
    if a_1a == 1:
        #The responce is in #5
        a_1b = 1
        a_1d = 0
    if a_1a == 2:
        print("You ask the woman what she knows that the wasps can do. She then responds by telling you that she dosn't know what they can do and that they just")
        print("showed up suddenly. She then tells you that you may be able to slow them down while the people try to help you get back up from other exterminators")
        print("when they arrive.")   
        a_1c = 0
        a_1b = 1
    else:
        print("that isn't an option. Choose one of the options presented")
print("")
#4 (you asked the woman a question)
while a_1c != 1 and 2:
    a_1a = int(input("What will you do? 1.Get your equipment and get ready to confront the wasps to buy time.  2. Wait til back up comes."))
    if a_1a == 1:
        a_1d = 0#response is in 5
        a_1c = 1 
    if a_1a == 2:
        print("You tell the group that you will wait til back up arrives so you have people to help you out. Someone from the group asks you if you have a spare suit so the number of people")
        print("to stop the wasp hive will be greater. The only issue is that you only have one suit. Besides the suit may not be effective against the giant wasps. ")   
        a_1c = 1#response is in 6 
        a_1e = 0
    else:
        print("that isn't an option. Choose one of the options presented")
print("")#5 (You quickly get your gear or you get your gear once you finished talking with her.)
while a_1d != 1 and 2:
    print("You then tell the group that you will get ready. You go back inside and start getting your extermination equipment along with your protective gear.")
    print("You wonder how effective your equipment will be at dealing with the giant wasps. After all they bigger and likely are stronger and their stingers will")
    print("be more painful and potentialy leathal. You then begin to wonder how should you approach the hive")
    a_1a = int(input("What will you do? 1. you approach the hive by foot   2. you take your car and drive to the hive"))
    if a_1a == 1:
        print("you exit your house from your grauge with your equipment and as you are exiting the people cheer you on and then one person in the crowd then says")
        print("Wait you still have chemicals and poisons that can harm the giants wasps. You should give them to the people who are willing to help you.")
        a_1f = 0# response is in 7
        a_1d = 1
    if a_1a == 2:
        print("Get a good amount of your chemicals and poisons (more than useual) and begin to exit your driveway to people cheering you on as you go try to stop and rid")
        print("the town of the hive of giant wasps.")   
        a_1d = 1 # response is in 8
        a_1g = 0
    else:
        print("that isn't an option. Choose one of the options presented")
print("")#6 (from 4: You tell the people to hide until back up comes)
while a_1e != 1 and 2:
    print("The man then makes a theory. The wasps are bigger but they don't appear to be as fast as a normal wasp so it is likely that it would be easier to hit them")
    print("and land blows onto them and further states that the hive may have notas much giant wasps inside them compared to a normal wasp hive. So he then suggest then")
    print("suggests that you should to take one down yourself away from the hive so that way you can understand how to take them one.")
    a_1a = int(input("What will you do? 1. Follow his suggeston  2. suggest that you wait til you get more exterminators."))
    if a_1a == 1:
        print("You respond saying 'You make a good point'. as you say that another giant wasp appear to fly and land into one of your neighbors front lawns to do something")
        print("with the flowers. It seems busy looking around while the people are looking at it with caution.")
        a_1e = 1#response is in 9
        a_1h = 0
    if a_1a == 2:
        print("You decide to wait but the back up didn't have enough time before you and the town got over ran. The end")   
        a_1e = 1 
    else:
        print("that isn't an option. Choose one of the options presented")
print("")#7 (from 5: You get asked if people can help you deal with the wasps if they can use your chemicals and poisons)
while a_1f != 1 and 2:
    print()
    a_1a = int(input("What will you do? 1.grant the people access to your resources to help you  2.decline telling people it is to risky for them to have themselves put into danger."))
    if a_1a == 1:
        print("Knowing that the giant wasps out number you. You decide it is best to have people help you out so you let people grab your chemicals, sprays, and pesticde")
        print(f"to help you in combatting the giant wasps. One man then talks to you and says'Thanks {p_name}. You may not remember me but I remember you when you helped desposed")
        print("my rat infestation. Instead of us watching you risking your self to the swarm. We will help cover you in the directions that they may be coming from. To be continued")
        a_1f = 1
    if a_1a == 2:
        print("You tell the people that they shouldn't risk themselves trying to kill the giant wasps. Because the poison may not kill or incapasitate them fast enough.")
        print("'I will try to help them back as much as I can before the back up arrives. Stay but and hunker up in your houses this will be bummpy.' You say. To be continued")   
        a_1f = 1 
    else:
        print("that isn't an option. Choose one of the options presented")
print("")#8
while a_1g != 1 and 2:
    print("The people tell you the directions of where the hive is and as you start to drive your way to it. There are lots of cars driving the oposite direction away from")
    print("the hive and you are starting to see giant wasps in a increasing number. They don't appear to be attacking anyone yet but you know the danger will only get bigger.")
    print("after driving for a while you can see the hive in the distance and you are getting closer while you see like hundreds of giant wasps flying arround. You hesitate a mement before making a descion.")
    a_1a = int(input("What will you do? 1. Drive your truck into the hive at full speed 2. Step out of the car and get your chemicals ready."))
    if a_1a == 1:
        print("You decide the best course of action to buy time and maybe cause as much damage as possible you decide to crash your truck right into the side of the hive.")
        print("As you hit the gas to start going full speed thats when you see the giants wasps start to fly twards you likely to stop you but the first crashed right into the")
        print("front of your hood with a splat as its corpse then gets ran over by your truck. luckly for you the wasps didn't have enough time to reach you as you plowed right")
        print("through the hive wall. before then coming to a complete stop. You then see the wasps starting to climb all over your truck. To be continued")
        a_1g = 1
    if a_1a == 2:
        print("Believing they haven't seen you yet you decide to get your chemicals ready to start the purge of giant wasps. As you are getting the chemicals ready.")
        print("You realize that some of the chemicals you have are flamible. This is a great opportunity to despose of the hive in one easy strike.  To be continued")   
        a_1g = 1 
    else:
        print("that isn't an option. Choose one of the options presented")
print("")#9
while a_1h != 1 and 2:
    print("")
    a_1a = print(input("What will you do? 1. Get everyone to be ready to charge the giant wasp 2.You rush it yourself and dump the cheicals onto it."))
    if a_1a == 1:
        int("To be continued")
        a_1b = 1
    if a_1a == 2:
        print("To be continued")   
        a_1c = 1 
    if a_1a == 3:# go to 10
        print("(Secret found) A very stupid though came to your head and it is to talk to the wasp")
        a_1h = 1
        a_1i = 0
    else:
        print("that isn't an option. Choose one of the options presented")
print("")#10 from 9 hidden path
while a_1i != 1 and 2:
    print("")
    a_1a = int(input("What will you do? 1. To be continued 2.To be continued"))
    if a_1a == 1:
        print("To be continued")
        a_1i = 1
    if a_1a == 2:
        print("To be Continued")   
        a_1i = 1 
    else:
        print("that isn't an option. Choose one of the options presented")