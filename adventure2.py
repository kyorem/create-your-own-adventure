game_start = "yes"

while game_start == "yes":
    print("you wake up from a drugged sleep in a strange bare room")
    print("you can't seems to remember anything")
    print("you look around and see many others lying on the floor and a giant monitor on the wall")
    print("then you begin to realise there seems to be no entrance or exit to the room")
    print("do you... ")
    print("1.wake everyone up")
    print("2.go explore the room first")
    choice = input("Enter choice(1/2): ")

    if choice == '1':
        print("you go around and wake everyone up. Everyone seems just as confused and clueless as you too")
        print("the monitor turns on")
        print("a masked figure then reveal that everyone have signed up to be a participant of a survival game")
        print("and whoever survives the longest will earn their freedom and 10 million in cash.")
        print("he also reveals that there are weapons hidden in the room in secret compartments that is now unlocked")
        print("you...")
        print("1.discuss with the others on what to do")
        print("2.sneak away to find a weapon")
        choice_1 = input("Enter choice(1/2): ")
        if choice_1 == "1":
            print("you talk with the others and worked together to find a way out")
            print("you and the other look around and you find a vent, you then call out to the others about the vent")
            print("you then volunteer to climb the vent. The others carry you up there and you climb into the vent")
            print("you are also given a dagger for defence")
            print("once inside you crawl till you see something that seems like a control room with a guard sleeping")
            print("you...")
            print("1.you break the vent gate and jump into the room")
            print("2.you continue on")
            choice_2 = input("Enter choice(1/2): ")

            if choice_2 == "1":
                print("you break the vent gate and jump down, however this alerted the guard and attack you")
                print("you managed to stab the guard in his sides.")
                print("however you still get shot by the guard's pistol fatally wounding you.")
                print("you manage to open the exit to the room with your dying breath before succumbing to your wounds")
                print("you and the guard were found later dead by the rest who went to find you")
            elif choice_2 == "2":
                print("after a while,you find a vent gate leading to the outside.you took your chances and escape")
                print("you jump out of the vent and make your way home, leaving the rest to die")
        elif choice_1 == "2":
            print("you sneak away and soon find a weapon in a hidden compartment")
            print("however you are found with a weapon which cause the rest to fear you and go look for weapons too")
            print("soon the room turn to a battlefield as people disagreed with each other")
            print("this lead to you surviving as you fought people just to survive. The room soon opens up an exit")
            print("you exit thinking if you did the right thing of sneaking off")
    elif choice == "2":
        print("you walk around and find a vent and a locked compartment.")
        print("however it is too high to reach, the monitor soon turn on abruptly")
        print("a masked figure then reveals that all have signed on to be a participant of battle to the death")
        print("and whoever survives the longest will earn their freedom and 10 million in cash.")
        print("the figure also reveals that there weapons hidden in the room in secret compartments and is now unlock")
        print("slowly people start to wake up.")
        print("you...")
        print("1.discuss with the others on what you have found")
        print("2.sneak away to find a weapon")
        choice_3 = input("Enter choice(1/2): ")

        if choice_3 == "1":
            print("you explain to the others about the vent and explain how you need their help to reach it")
            print("you and the other go to vent to figure out on how to reach it while the other go look for weapons.")
            print("you then volunteer to climb the vent. The others carry you up there and you climb into the vent")
            print("you are also given a dagger from the other group for defence")
            print("once inside you crawl till you see a what seems like a control room with a guard sleeping")
            print("you...")
            print("1.you break the vent gates and jump into the room")
            print("2.you continue on")
            choice_4 = input("Enter choice(1/2): ")
            if choice_4 == "1":
                print("you break the vent gate and jump down, however the sound alerted the guard and attack you")
                print("you managed to stab the guard in his sides.")
                print("however you still get shot by the guard's pistol fatally wounding you.")
                print("you manage to open the exit to the room with your dying breath before succumbing to your wounds")
                print("you and the guard were found later dead by the rest who went to find you")
            elif choice_4 == "2":
                print("after a while,you find a vent gate leading to the outside.you took your chances and escape")
                print("you jump out of the vent and make your way home.leaving the rest to die")
        elif choice_3 == "2":
            print("you sneak away and soon find a weapon in a hidden compartment")
            print("however you are found with a weapon which cause the rest to fear you and go look for weapons too")
            print("soon the rooms turn to a battlefield as people disagreed with each other which led to fights")
            print("this lead to you surviving as you fought people just to survive.the room soon opens up a exit")
            print("you exit thinking if you did the right thing of finding a weapon first")

    game_start = input("do you want to start over?")