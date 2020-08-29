from time import *

def startTower():
    print("\nThe tower lies before you.")
    choice = input("a) Go in the front. Boldness is favoured by fortune.  b) Search for a back entrance. Let's remain hidden. \n")

    if choice == "a":
        rating = rating + 10
        skeletonAppear()

    elif choice == "b":
        print("You search around the tower until you find a trapdoor that leads into the tower. You and your companions enter the tower through the trapdoor.")
        sewerCorridor()

    else:
        print("\n You must choose an option. Cowardice is not favoured by the King.")
        startTower()

def skeletonAppear():
    print("\nA skeleton guards the hallway before you. It looks dangerous.")
    print("What do you do?")
    choice = input("a) Fight the skeleton.  b) Run away \n")

    if choice == "a":
        rating = rating = rating + 20
        skeletonFight()

    elif choice == "b":
        startTower()

    else:
        print("Your failure to make a coherent decision quickly has cost you the lives of you and your companions.")
        print("You have died.")
        rating = 0
        score()

def skeletonFight():
    print("\nThe skeleton lunges forward!")
    choice = input("a) Swing your weapons.  b) Raise your shields. \n")
    if choice == "a":
        print("\nYou charge towards the skeleton, weapons raised at large. However, you do not realise that you ")
        print("have left your right flank wide open. You strike the skeleton down, but not before it gives you a")
        print("nasty gash along the side of your torso.")
        injury = True
        print("You continue down the hallway, taking care not to step on the skeleton's remains.")
        rating = rating + 10
        sewerCorridor()
        
    elif choice == "b":
        print("\nYou successfully block the attack. The skeleton stumbles backward, giving you enough time to ")
        print("strike and slay the foul creature.")
        print("You continue down the hallway, taking care not to step on the skeleton's remains.")
        rating = rating + 20
        sewerCorridor()
        
    else:
        print("Your failure to make a coherent decision quickly has cost you the lives of you and your companions.")
        print("You have died.")
        rating = 0
        score()

def sewerCorridor():
    print("\nYou find yourself in a sewer-like corridor. To your left, a hallway glows with a peculiar green light. To your ")
    print("right, a staircase leads up into the dark.")
    print("What do you do?")
    choice = input("a) Enter the hallway to your left.  b) Climb the stairs to your right.\n")
    if choice == "a":
        capsuleRoom()
    elif choice == "b":
        finalBattle()
    else:
        print("\n You must make a choice. We've gotten too far. There's no turning back now.")
        sewerCorridor()

def capsuleRoom():
    print("\nYou are in a room. On your left is a ladder. On your right, three prisoners are floating in strange, ")
    print("glowing capsules. They appear to be in the process of some kind of transformation.")
    print("Could this be some kind of sick experiment of the Sorcerer?")
    print("What do you do?")
    choice = input("a) Leave as quickly as possible.  b) Destroy the capsules.\n")
    if choice == "a":
        print("Highly disturbed by what you've just witnessed, you and your companions quickly climb the ladder and exit the room.")
        rating = rating - 10
        finalBattle()
    elif choice == "b":
        print("After putting these poor souls to rest, you and your companions climb the ladder.")
        rating = rating + 10
        finalBattle()
        
    
def finalBattle():
    print("\nYou've come to a door at the end of a hallway.")
    sleep(3)
    print("The time has come to face the evil Sorcerer Stryker.")
    sleep(3)
    print("Preparing yourself for the final battle, you open the door before you.")
    sleep(3)
    print("\nStryker: Intruders? How dare you tresspass in my private chambers!")
    print("\nStryker: Ah, so you've come for the Sword of Demares...")
    print("\nStryker: Hehehe... fools. You'll make a nice addition to my skeleton army!")

    print("\nThe Evil Sorcerer Stryker casts a large ball of fire at you and your companions!")
    print("What do you do?")
    choice = input("a) Launch a counterattack with your own fireball.  b) Cast a shield to protect you and your companions.\n")
    if choice == "a":
        if injury == True:
            print("You begin to cast your own fireball, but you are suddenly filled with excruitiating pain. The wound from your fight earlier ")
            print("has begun to take its toll on your body. Unfortunately, this delays you to take immediate action against Stryker, and his fireball")
            print("completely eradicates you and your companions.")
            rating = rating - 50
            score()
        else:
            print("Quick to react, you cast your own fireball and launch it at Stryker's. The two magic spells collide, creating a large explosion. While")
            print("Stryker is still stunned from the explosion, you quickly cast another fireball that hits Stryker square in the face. The sorcerer shrieks")
            print("and crumbles to dust.")
            print("\nYou pick up the Sword of Demares, restoring order and peace to the kingdom.")
            rating = rating + 20
            score()
    elif choice == "b":
        print("You quickly cast a protection spell over you and your companions. Stryker's fireball bounces off your shielding charm and hits him square in the face.")
        print("The evil sorcerer shrieks in pain before crumbling to dust.")
        print("\nYou pick up the Sword of Demares, restoring order and peace to the kingdom.")
        rating = rating + 10
        score()

    else:
        print("Your failure to make a coherent decision quickly has cost you the lives of you and your companions.")
        print("You have died.")
        rating = rating - 50
        score()        


def score():
    print("\n*********************")
    print("****** THE END ******")
    print("*********************")

    if rating >= 50:
        print("You finished the game with an 'A' rating.")

    elif 30 <= rating <= 40:
        print("You finished the game with a 'B' rating.")

    elif 0 <= rating <= 20:
        print("You finished the game with a 'C' rating.")

    else:
        print("You finished the game with a 'D' rating.")
    
    print("*********************")
    print("\n Thank you for playing The Kingdom of Demares! I hope you enjoyed this game.")
    print("By Sarah Ahmed")

    choice = input("\nWould you like to play again? (y/n)")
    if choice in ["y", "Y", "yes", "YES", "Yes"]:
        introGame()
    else:
        print("Okay then. Bye.")

def introGame():
    #title

    print("********************************")
    print("**** THE KINGDOM OF DEMARES ****")
    print("********************************")
    
    #introduction
    print()
    print("The King has entrusted you and your companions with recovering the Sword of Demares...")
    print("a task which, if completed successfully, will grant you a lifetime of glory, as well ")
    print("as a sizeable fortune of gold and silver.")
    print()
    print("After the long months of journeying across unforgiving lands, you step out of the outskirts")
    print("of a forest to see your destination looming in the distance.")
    print()
    print("There, beyond a moonlit plain, lies the Wizard's Tower... where the evil Sorcerer Stryker has")
    print("stolen the power of the Sword of Demares for his own vile purposes.")

    startTower()

rating = 0
injury = False
introGame()
