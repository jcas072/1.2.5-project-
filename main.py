
#-----import statements--------------------------
import turtle as trtl
import random
import time
import sys
import os
from termcolor import cprint  

#-----text animation-------------------------------
def text_ani(str): 
  choice=input()
  if choice == '': 
    os.system('cls' if os.name == 'nt' else 'clear')
    for char in str:
      sys.stdout.write(char)
      sys.stdout.flush()
      time.sleep(0.05)
    cprint("\n\nPRESS ENTER TO CONTINUE", attrs=['reverse', 'bold'])
    time.sleep(1) 
    
def text_ani_input(str): 
  for char in str:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)
  time.sleep(1)

  
def text_ani_slow(str):
  choice=input()
  if choice == '': 
    os.system('cls' if os.name == 'nt' else 'clear')
    for char in str:
      sys.stdout.write(char)
      sys.stdout.flush()
      time.sleep(1)
    print 
    cprint("\n\nPRESS ENTER TO CONTINUE", attrs=['reverse', 'bold'])

#-----prints character name-------------------------------
def charctersName():
  choice = input()
  if choice == '':
    os.system('cls' if os.name == 'nt' else 'clear')
    cprint('You', attrs=['bold'])

def elfname():
  choice = input()
  if choice == '':
    os.system('cls' if os.name == 'nt' else 'clear')
    cprint('Rocky', attrs=['bold'])

def helpername():
  choice = input()
  if choice == '':
    os.system('cls' if os.name == 'nt' else 'clear')
    cprint('Helper', attrs=['bold'])

def evil():
  choice = input()
  if choice == '':
    os.system('cls' if os.name == 'nt' else 'clear')
    cprint('Evil Guy', attrs=['bold'])

def santa():
  choice = input()
  if choice == '':
    os.system('cls' if os.name == 'nt' else 'clear')
    cprint('Santa', attrs=['bold'])

#-----prints endings-------------------------
def good_ending():
  cprint('\n\nGOOD ENDING', 'green', attrs=['reverse','bold']) 

  exit()

def bad_ending():
  cprint('\n\nBAD ENDING', 'red', attrs=['reverse','bold']) 

  exit()

#-----title screen-------------------------------

wn = trtl.Screen()
wn.setup(700, 350) # size of window
wn.bgpic("pic.gif")
wn.bgcolor('antiquewhite')


print('          ')
print('               ____')
print('            .-\" +\' \"-.    __,  ,___,')
print('           /.\'.\'A_\'*`.\  (--|__| _,,_ ,_')
print('          |:.*\'/\-\. \':|   _|  |(_||_)|_)\/')
print('          |:.\'.||\"|.\'*:|  (        |  | _/')
print('           \:~^~^~^~^:/          __,  ,___,')
print('            /`-....-\'\          (--|__| _ |\' _| _,   ,')
print('       jgs /          \           _|  |(_)||(_|(_|\//_)')
print('           `-.,____,.-\'          (               _/')
#https://asciiart.website/index.php?art=holiday/christmas/other

#-----introduction to game-------------------------

def prologue():
  cprint("\n\nPRESS ENTER TO CONTINUE", attrs=['reverse', 'bold'])
  text_ani('That time of year has come again. \nThe Holiday\'s are right around the corner.')
  smallTown = trtl.Screen()
  smallTown.bgpic('town.gif')
  text_ani('In your small town everyone is rushing to get their loved ones gifts!\nYou are one of those people.')
  print('                 _  _')
  print('                /_\/_\ ')
  print('        .=======\_\/_/=======.')
  print('        |        //\\\______ |')
  print('        |       //  ||to you||')
  print('        |        |  |`\"\"\"\"\"\"`|')
  print('        |        |  |        |')
  print('    jg  |        |  |        |')
  print('        \'====================\'')
#https://asciiart.website/index.php?art=holiday/christmas/other

  text_ani('Today was like any ordinary day and you head to work greeting people on your way.')
  work = trtl.Screen()
  work.bgpic('work.gif')
  text_ani('All is going good at work and you work hard. \nA couple hours into work you start to doze off due to the lack of sleep since you have been staying late at work. \nYou just want the kids in your town to have a memorable Chirstmas this year due to the pandemic.')
  text_ani('Next thing you know everything is black.')

  black = trtl.Screen()
  black.bgcolor('black')
  black.bgpic('black.gif')
  text_ani_slow('...')
  text_ani_slow('...')
  text_ani_slow('...')

  work = trtl.Screen()
  work.bgpic('work.gif')
  text_ani('You are awaken by an angry boss')
  print('   ')
  print('(╬ ಠ益ಠ)')
  text_ani('He yells at you and fires you on the spot.\nYou realize this is the worst time to get fired because you need the money for necessities, bills and gifts.')

  house = trtl.Screen()
  house.bgpic('house.gif')
  text_ani_slow('~ 1 week later ~')
  text_ani('After a week of searching for jobs no luck has presented itself. \nBills have been piling on your counter and you haven\'t had a proper meal in a week.\nYou have lose all hope.\nYou go check the mail to see what bills have piled.')

  mail = trtl.Screen()
  mail.bgpic('mail.gif')

  text_ani('There are no bills piled up!')
  print('    ')
  print('         __________________')
  print('        |             .__. |')
  print('        |  ._-..      |  | |') 
  print('        |             \'\"\"\' |') 
  print('        |           -.,-_  |') 
  print('        |__________________|') 

  text_ani('Instead there is a letter, but you don\'t recognize where its from.')

  print('    ')
  print('       __________________')
  print('      |\                /|')
  print('      | \              / |') 
  print('      | /\____________/\ |') 
  print('      |/                \|') 
  print('      |__________________|') 

  text_ani("You open the letter.")

  print('      ')
  print('          ____________')
  print('         /     _.\'\   ')
  print('        /   _.\'    \   \=')
  print('       /_.-\'        \___')
  print('      |\_\ ``   .-   \ _/|')
  print('      |  _\___________.  |') 
  print('      | /              \ |') 
  print('      |/                \|') 
  print('      |__________________|') 

  letter = trtl.Screen()
  letter.bgpic('letter.gif')
  charctersName()
  text_ani_input("OMG!")
  text_ani('You quickly write a letter back and explain your situaion.')
  text_ani('The next day there is an elf outside wating to interview you!')

  hope = trtl.Screen()
  hope.bgpic('hope.gif')
  prologue()

#-----endings-------------------------
def game_over1():
  santahouse = trtl.Screen()
  santahouse.bgpic('santahouse.gif')

  text_ani('You head to Santa\'s house.')
  text_ani('An Elf spots and you quickly runs to you.')
  text_ani('The elf explains that you are not supposed to be here and starts dragging you away from the house.')
  text_ani('You try to explain that you are here for a job, but the Elf does not listen to you.')
  text_ani('The elf brings you to the plane and tells the jet to send you home.')
  text_ani('You get sent home.')
  bad_ending()

def game_over2():
  text_ani('You are at the Coal Mine.')
  coal = trtl.Screen()
  coal.bgpic('coal.gif')

  text_ani('You enter the mine and quickly find how easy it is to get lost')
  text_ani('Instead of going back, you keep going in thinking that you will remember your way out.')
  text_ani('Soon you realize your mistake! You are lost and do not know your way out.')  
  bad_ending()

def gameover3():
  text_ani('You are right in front of Santa\'s sleigh')
  sleigh = trtl.Screen()
  sleigh.bgpic('sleigh.gif')
  text_ani('You notice how big the sleigh is! You ignore the fact that it is unstable and get on the sleigh.')
  text_ani('Right as you get on it the sliegh starts to make noises.') 
  text_ani('The sleight starts to move and you start to head downhill.')
  text_ani('Soon you realize how dangerous it is, but it is too late.')
  text_ani('You come crashing to a tree.')
  bad_ending()

def gameover4():
  text_ani('You are inside of the Labs.')
  text_ani('The Labs is a huge place. You realize its because there are 4 different types of labs here. Fabric, Metal, Coal, and Wrapping paper.')
  labs = trtl.Screen()
  labs.bgpic('labs.gif')
  text_ani('Once you are inside you realize how busy it is inside. It is loud. You regret your choice because you realize that Santa will not be here.')
  text_ani('An elf sees you and goes up to you. They tell you that you have to get to work now and drags you to one of the 4 labs.')
  text_ani('You are stuck working and can not leave.')
  bad_ending()


def gameover5():
  text_ani('You are in the mailroom.')
  mailroom = trtl.Screen()
  mailroom.bgpic('mailroom.gif')

  text_ani('You look around and admire the view. You realize that this whole workshop is amazing. Every room has its own surprise.')
  text_ani('Here in the mailroom you see all the mail from kids all over the world. It is crazy how much mail the kids send.')
  text_ani('Soon you notice in the corner that there already elves here.')
  text_ani('You also see SANTA!!')
  
  charctersName()
  text_ani_input('Dang I came too late!')
  text_ani('As you walk closer you notice that something is not right. Everyone looks terrified.')
  text_ani('Something is off here.')

  evil()
  text_ani_input('HEY YOU!')
  evil()
  text_ani_input('Get in the corner with the rest of them.')

  text_ani('You are afraid and go to the corner.')
  evil()
  text_ani_input('Now I will end all of you and the workshop today!')
  evil()
  text_ani_input('I always recvied coal for chirstmas while all the other kids got presents')
  evil()
  text_ani_input('Do you know how that makes me feel? NO! So I am taking revenge I have planned this for years.')
  evil()
  text_ani_input('Now the day has finally come ! HAHAHA')

  text_ani('This is not how you want to die!')

  charctersName()
  text_ani_input('I must do something!')
  charctersName()
  text_ani_input('HEY YOU! LET\'S BATTLE')
        

def gameover6():
  workshop = trtl.Screen()
  workshop.bgpic('workshop.gif')

  text_ani('In the end the creature ends up leaving.')
  text_ani('Eveyone is cheering and is happy that you were able to make the evil creature leave.')
  santa()
  text_ani_input('Thank you for saving Christmas this year! You are welcome here anytime. ')
  santa()
  text_ani_input('I know of your struggles, so this Christmas there will be a little surprise for you under the tree!')

  text_ani('Everyone ends up having a great Christmas and so do you!')
  good_ending()

#-----branches-------------------------
def branch1():
  text_ani('You head to the Elf Dorm')
  dorm = trtl.Screen()
  dorm.bgpic('dorm.gif')

  text_ani('Once you are at the Dorm you see your name at a door and enter the room.')
  text_ani('On the bed you notice your uniform and put it on. After you head to Santa\'s house')

  santahouse = trtl.Screen()
  santahouse.bgpic('santahouse.gif')

  text_ani('Once you arrive there is a a huge group of elves and one is talking in front of everyone.')

  helpername()
  text_ani_input('Hello everyone!')
  helpername()
  text_ani_input('There is an emergency! Christmas is in a couple of days and Santa is missing! There is a lot of work to do so we have to find him ASAP!')
  text_ani('Whoever can find him will get a huge reward!')

  text_ani('Now that sounds interesting! You decide that you will be the first one to find him!')

  text_ani('You hear all the elves talking amoung themelves. One conversation catchs your attention.')

  helpername()
  text_ani_input('He could be in the coal mine. But it\'s so dangerous no elf dares to go in.')

  charctersName()
  text_ani_input('Hmm interetsing!')

  map = trtl.Screen()
  map.bgpic('map.gif')

  text_ani('You use the map and to go to the front of the workshop! ')
  text_ani("you are determined to find Santa first at all costs and get that reward. Where should you head first? the Coal Mine or the Entrance of the workshop?")

  charctersName()
  text_ani_input('If I go to the coal mine it would be the least expected place that anyone would find him. But also the Coal Mines are known to be super dangerous.')
  charctersName()
  text_ani_input('If I go the Entrance it woul be a safer option and he could be somewhere in the workshop.')

  cprint("\n\n\nTYPE A LETTER AND HIT ENTER", attrs=['reverse', 'bold'])
  choice=input("A) Coal Mine     B) Entrance").upper()

  if choice == 'A':
    game_over2()
  elif choice == 'B':
    branch2()

def branch2():
  text_ani('You are in the entrance of the workshop and your realize how big it is.')
  workshop = trtl.Screen()
  workshop.bgpic('workshop.gif')

  charctersName()
  text_ani_input('Santa could be anywhere!')
  
  text_ani('You look around Entrance to see if you find anything useful. ')

  text_ani('But there is not much at the Entrance. There really is not anything here for you to do, so you look at the map to see where you can go next.')
  text_ani('You conclude two places you can go to. Which are the Workshop and the Stable.')

  map = trtl.Screen()
  map.bgpic('map.gif')

  charctersName()
  text_ani_input('Where should I go the stables or the workshop.')
  
  cprint("\n\n\nTYPE A LETTER AND HIT ENTER", attrs=['reverse', 'bold'])
  choice=input("A) Stable    B) Workshop").upper()

  if choice == 'A':
    branch3()
  elif choice == 'B':
    branch4()

def branch3():
  text_ani('You are in the stables right now.')
  stable = trtl.Screen()
  stable.bgpic('stable.gif')

  text_ani('There you find youself with a bunch of reindeer.')
  text_ani('Sadly there is no sign of Santa here. So you end up looking around to see what the place has to offer.')

  charctersName()
  text_ani_input('Woah! This is CRAZY! I get to see reindeers close up.')

  text_ani('The door to the stables close and you try yo go out, but it won\'t budge. You\'re stuck.')

  text_ani('You notice a sign and read it.')

  stable = trtl.Screen()
  stable.bgpic('stable.gif')

  text_ani('You find the carrots in the bucket and start feeding the reindeer.')
  text_ani('It seems like he likes you now.')
  text_ani('You behind the reindeer and fetch the key. You go to unlock the door.')

  text_ani('Now that the door has opened you look at the map to see where to go next.')

  map = trtl.Screen()
  map.bgpic('map.gif')

  text_ani('As you look atthe map you look outside to see Santa\'s sleigh. There is also the workshop.')
  text_ani('It looks very unstable.')
  charctersName()
  text_ani_input('I can go check out the sleigh or go the workshop. Where should I go?')
  charctersName()
  text_ani_input('The sleigh could be dangerous, but he could be hiding there since no one goes there.')
  charctersName()
  text_ani_input('There is always the workshop that is inside and looks huge in the map which has potential hidding places.')

  cprint("\n\n\nTYPE A LETTER AND HIT ENTER", attrs=['reverse', 'bold'])
  choice=input("A) Santa\'s Sleigh    B) Workshop").upper()

  if choice == 'A':
    gameover3()
  elif choice == 'B':
    branch4()


def branch4():
  text_ani('You are now in the workshop.')
  workshop2 = trtl.Screen()
  workshop2.bgpic('workshop2.gif')

  text_ani('The place is so huge that it takes you 30 minutes to explore the whole place.')
  text_ani('It doesnt look like he is here. So you decide to search elsewhere. But right as you are about to leave an elf spots you.')

  helpername()
  text_ani_input('Hey you! Go fetch me 3 toys now I need them.')

  text_ani('You just stare at him. Why is this dude ordering me around.')

  helpername()
  text_ani_input('HELLO! I SAID NOW. Or you can not leave. SO HURRY')

  text_ani('You frantically seach for the three gifts that he showed you.')

  text_ani('It takes you about 30 minutes to find the three gifts. ')
  text_ani('You walk towards the elf.')

  charctersName()
  text_ani_input('Here are your three toys you asked for.')

  text_ani('Annoyed you stomp out before the elf could say anything. In the hallway you look at the map again.')
  text_ani('You can go the labs or the mailroon')
  charctersName()
  text_ani_input('If I go to the mailroom then that would be the last place he could be at.') 
  charctersName()
  text_ani_input('If I go to the labs he could be there, but I could be put to do work.') 

  cprint("\n\n\nTYPE A LETTER AND HIT ENTER", attrs=['reverse', 'bold'])
  choice=input("A) Mailroom    B) Labs").upper()

  if choice == 'A':
    gameover5()
  elif choice == 'B':
    gameover4()



#-----starting game-------------------------
def startgame1():
  text_ani('A couple days have passed and the day has finally come.')

  northpole = trtl.Screen()
  northpole.bgpic('northpole.gif')

  text_ani('You go to the North Pole and are greeted by Rocky the Elf from before.')

  elfname()
  text_ani_input('Hello! Welcome to the North Pole! I will be your personal guide today!')
  elfname()
  text_ani_input('Today we will go over the Workshop, sign all the necessary documents and explain the work you\'ll be doing.')

  text_ani('Rocky Hands you a paper.')

  map = trtl.Screen()
  map.bgpic('map.gif')

  elfname()
  text_ani_input('Here is a map of the place. Made by Rocky himself! This map contains all the places at the workshop.')
  elfname()
  text_ani_input('Alright! so first we will hea-')

  northpole = trtl.Screen()
  northpole.bgpic('northpole.gif')

  helpername()
  text_ani_slow('HELP!')
  helpername()
  text_ani_input('SANTA IS MISSING! ALL ELVES TO SANTA\'s HOUSE NOW!')

  elfname()
  text_ani_input('Sorry! I have to go!!')
  elfname()
  text_ani_input('Use the map and head to the Elf Dorm. There will be a uniform on your bed waiting for you.')
  elfname()
  text_ani_input('Oh YEAH! I forgot to tell you!! You MUST wear the uniform, since none of the other elves know you. They may think you are an imposter and kick you out!! BYE!!')

  text_ani('You are so confused right now of what just happened. You look at your map to find the dorm')

  map = trtl.Screen()
  map.bgpic('map.gif')

  charctersName()
  text_ani_input('Alri-')

  helpername()
  text_ani_input('HEY YOU!! TO SANTAS HOUSE NOW!')

  charctersName()
  text_ani_input('Sor-')

  text_ani('Before you could finish your sentence the elf leaves.')

  charctersName()
  text_ani_input('Phew! That was scary! Now should I go to the dorm or to Santa\'s house?')

  charctersName()
  text_ani_input('If I go to the dorm I can get my uniform and not get kicked out. But I could encounter that elf and get yelled at again.')
  charctersName()
  text_ani_input('If I go to the house I could help out quicker and not get yelled at. I do run the possibilty of getting kicked out for not having my uniform.')

  cprint("\n\n\nTYPE A LETTER AND HIT ENTER", attrs=['reverse', 'bold'])
  choice=input("A) Elf Dorm     B) Santa\'s House ").upper()

  if choice == 'A':
    branch1()
  elif choice == 'B':
    game_over1()


startGame = input('You have been hired to be Santa\'s helper! Will you accept the job? y/n')
cprint("\n\nPRESS ENTER TO CONTINUE", attrs=['reverse', 'bold'])
if startGame == 'n' or startGame == 'N':
  elfname()
  text_ani_input('That\'s though you missed out on a great opportunity!')
  
elif startGame == 'y' or startGame == 'Y':
  elfname()
  text_ani_input('I\'m glad that you accepted this amazing opportunity! We will get started right away. What did you say your name was again?')
Response_1 = input("") 
Response_1 = Response_1.title()
elfname()
text_ani_input('AH yes! {} what a nice name you have!'.format(Response_1))

startgame1()


#-----creating hero classes-------------------------
class elfwarrior (object):
    health = 50
    strength = 10
    defence = 10
    magic = 1

class elfwizard (object):
    health = 125
    strength = 7
    defence = 7
    magic = 10

class elf (object):
    health = 100
    strength = 5
    defence = 10
    magic = 7

#-----creating enemy classes------------------------
class halfling (object):
    name = "Little Drummer Boy"
    health = 20
    strength = 2
    defence = 2

class krampus (object):
    name = "Krampus"
    health = 10
    strength = 1
    defence = 3


class human (object):
    name = "Slient Knight"
    health = 30
    strength = 5
    defence = 1.5

#-----selecting the hero-------------------------
def gamedone(character, score):
    if character.health < 1:
        print("You have no health left")
        print("Thanks for playing...")
        print("You have scored...", score)
        
        writeScore(score)

        file=open("score.txt","r")

        for line in file:
            xline = line.split(",")
            print(xline[0], xline[1])
        gameover6()
        

def writeScore(score):
    file = open('score.txt','a')
    file.write(str(score))
    file.write(",")
    file.write("\n")
    file.close()


def heroselect():
    print ("Select your hero!")
    selection = input("1. elfwarrior \n2. elfwizard \n3. elf \n")
    if selection == "1":
        character = elfwarrior
        print ("You have selected the mighty Elfwarrior!... These are their stats...")
        print ("Health =  ", character.health)
        print ("Strength = ", character.strength)
        print ("Defence = ", character.defence)
        print ("Magic = ", character.magic)
        return character

    elif selection == "2":
        character = elfwizard
        print ("You have selected the wizard...These are their stats...")
        print ("Health = ", character.health)
        print ("Strength = ", character.strength)
        print ("Defence = ", character.defence)
        print ("Magic = ", character.magic)
        return character

    elif selection == "3":
        character = elf
        print ("You have selected the elf...These are their stats...")
        print ("Health = ", character.health)
        print ("Strength = ", character.strength)
        print ("Defence = ", character.defence)
        print ("Magic = ", character.magic)
        return character

    else:
        print("Only press 1, 2 or 3")
        heroselect()

def enemyselect(krampus,human,halfling):
    enemyList = [krampus,human,halfling]
    chance = random.randint(0,2)
    enemy = enemyList[chance]
    return enemy

      
def battlestate(score):
    enemy = enemyselect(krampus,human,halfling)
    text_ani('The creature turns around and is angry. ')
    evil()
    text_ani_input('You asked for this. You will die today! I will now transfrom into one of my three creatures.')
    print("I am now", enemy.name, "Time for you to die!!!")
    print ("you have 2 options...")

    while enemy.health > 0 :
        choice = input("1. Fists\n2. Magic")

        if choice == "1":
            print ("You get your fists ready, punching", enemy.name)
            hitchance = random.randint(0,10)
            if hitchance > 3:
                enemy.health = enemy.health - character.strength
                print ("You hit the enemy, their health is now....", enemy.health)

                if enemy.health > 1:
                    character.health = character.health - (enemy.strength / character.defence)
                    print ("The", enemy.name, "takes a swing, it hits you leaving", character.health)
                    gamedone(character, score)
                    

                else:
                    if enemy.name == "Little Drummer Boy":
                        enemy.health = 20
                        score = score + 10
                        

                    elif enemy.name == "Krampus":
                        enemy.health = 10
                        score = score + 5
                        

                    elif enemy.name == "Slient Knight":
                        enemy.health = 30
                        score = score + 15
                        

                    print ("You have defeated the", enemy.name)
                    return score
                    break
            else:
                print("You stumble on your feet and miss the creaure!")
                print("The", enemy.name, "hits you for full damage")
                character.health = character.health - enemy.strength
                print("You now only have", character.health, "remaining")
                gamedone(character, score)


        elif choice == "2":
            print ("You cast a spell, attacking the", enemy.name)
            hitchance = random.randint(0,10)
            if hitchance > 3:
                enemy.health = enemy.health - character.magic
                print ("You hit the enemy, their health is now....", enemy.health)

                if enemy.health > 0:
                    character.health = character.health - (enemy.strength / character.defence)
                    print ("The", enemy.name, "takes a swing, it hits you leaving", character.health)
                    gamedone(character, score)

                else:
                    if enemy.name == "Little Drummer Boy":
                        enemy.health = 20
                        score = score + 10
                        

                    elif enemy.name == "Krampus":
                        enemy.health = 10
                        score = score + 5
                        

                    elif enemy.name == "Slient Knight":
                        enemy.health = 30
                        score = score + 15
                        

                    print ("You have defeated the", enemy.name)
                    return score
                    break
            else:
                print("You overthink your spell, and miss!")
                print("The", enemy.name, "hits you for full damage")
                character.health = character.health - enemy.strength
                print("You now only have", character.health, "remaining")
                gamedone(character, score)
        else:
            print ("number not allowed, please only type 1, 2 or 3...")
        

score = 0
character = heroselect()
score = battlestate(score)
print(score)
score = battlestate(score)
print(score)
score = battlestate(score)
print (score)
score = battlestate(score)
print(score)
score = battlestate(score)
print(score)
score = battlestate(score)
writeScore(score)




#-----events----------------



wn.mainloop()
