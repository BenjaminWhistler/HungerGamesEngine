import HungerGamesClasses

def compile_events():
    story = HungerGamesClasses.BinaryTree()
    user = HungerGamesClasses.Tribute()
    start = story.set_root("You are a tribute who has been selected to compete in the annual Hunger Games."
                           "\n\nAfter much preparation, the day has finally come."
                           "\n\nYou step onto the platform, and upon reaching the top you see 23 other Tributes preparing to race toward either the Cornucopia or the jungle-like woods. " 
                           "\n\nWill you go toward the Cornucopia [1], or run into the woods? [2]")
    cornucopia = story.add_left(start, "\nYou rush toward the Cornucopia as fast as you can. Your adrenaline is pumping like never before."
                                       "\n\nYou begin to start making your way toward the closest weapon, a sword, when you "
                                       "notice another tribute running at your pace. \n\nDo you run over and strike with your fists first [1], or try to beat her to the sword? [2]")
    woods = story.add_right(start, "You quickly flee towards the woods, but in your rush you accidentally bump into a tracker jacker nest. \nThey all rush out of the nest and quickly eliminate you.")
    cornucopia_strike = story.add_left(cornucopia, "\nAs you and the other tribute begin getting closer to the sword, you run over and quickly strike her with your right fist, which completely catches\n"
                                                   "her off guard, knocking her off her feet."
                                                   "\n\nYou use the window to quickly dash toward the sword and managed to reach it before anybody else."
                                                   "\n\nDo you want to grab the sword [1], or leave it? [2]", event_type="Loot", loot="Sword", loot_type="Weapon",
                                       post_loot_string="The rest of the tributes have quickly made their way toward the Cornucopia, and are frantically rushing toward and fighting over\n"
                                                        "the available weapons. One tribute is beginning to advance toward you, wielding an axe.\n\n"
                                                        "Do you wish to fight [1], or flee? [2]")
    cornucopia_strike_fight = story.add_left(cornucopia_strike, "You engage the tribute.", event_type="Combat", hp=100, weapon=90)
    cornucopia_strike_fight_lose = story.add_right(cornucopia_strike_fight, "You are overpowered and eliminated.")
    cornucopia_strike_fight_win = story.add_left(cornucopia_strike_fight, "Incredibly, you manage to survive and defeat the axe-wielding tribute."
                                                                          "\n\nDo you want to grab the axe [1], or leave it? [2]",
                                                 post_loot_string="There is only one tribute left in the entire arena, standing right across from you wielding a dagger. Fight [1], or flee? [2]", event_type="Loot", loot="Axe", loot_type="Weapon")
    cornucopia_strike_fight_win_fight = story.add_left(cornucopia_strike_fight_win, "You charge and start swinging!", event_type="Combat", hp=100, weapon=35)
    cornucopia_strike_fight_win_fight_win = story.add_left(cornucopia_strike_fight_win_fight, "You manage to overpower and eliminate the final tribute. \n\nYou are victorious! You have survived and your name will be passed down for generations.")
    cornucopia_strike_fight_win_fight_lose = story.add_right(cornucopia_strike_fight_win_fight, "You sustain too many injuries, and are eliminated.")
    cornucopia_strike_fight_win_run = story.add_right(cornucopia_strike_fight_win, "You attempt to run away, but are quickly hawked down by the tribute who begins attacking.", event_type="Combat", hp=100, weapon=35, user_first=False)
    cornucopia_strike_fight_win_run_win = story.add_left(cornucopia_strike_fight_win_run, "Despite being unable to escape at first, you manage to overpower and defeat the final tribute."
                                                                                          "\n\nYou are victorious! You have survived and your name will be passed down for generations.")
    cornucopia_strike_fight_win_run_lose = story.add_right(cornucopia_strike_fight_win_run, "You sustain too many injuries, and are eliminated.")

    cornucopia_dash = story.add_right(cornucopia, "As you rush toward the sword, you and the other tribute reach it at the same time. Both of you grab it at the same time and struggle to win the tug of war."
                                                  "\n\nDo you attempt to keep struggling in order to get the sword [1], or do you let go of it and attempt to flee to the woods? [2]")
    cornucopia_fight = story.add_left(cornucopia_dash, "During the struggle, the sword slips out of both of your hands and clatters to the ground. The Tribute quickly starts striking with her fists.", event_type="Combat", hp=50, weapon=10, user_first=False)
    cornucopia_fight_win = story.add_left(cornucopia_fight, "You manage to win the fist fight between you and the other tribute, but before you have any time to react you are struck from behind."
                                                            "\nThe blow is too powerful, resulting in your elimination.")
    cornucopia_fight_lose = story.add_right(cornucopia_fight, "You are overpowered during the fist fight. You have been eliminated.")
    cornucopia_give_up = story.add_right(cornucopia_dash, "You let go of the sword, pushing her back in order to give yourself a window to escape, and quickly start running to escape the Cornucopia and enter the woods. \nIn your rush you accidentally bump into a tracker jacker nest. They all rush out of the nest and quickly eliminate you.")
    cornucopia_loot_and_escape_attempt = story.add_right(cornucopia_strike, "While attempting to escape, you find yourself running head-first into a knife-armed tribute, who starts attacking you first.", event_type="Combat", hp=50, weapon=35, user_first=False)
    cornucopia_escape_win = story.add_left(cornucopia_loot_and_escape_attempt, "\n\nYou managed to eliminate her, but have no time to loot. You quickly run and escape to the woods. You continue walking for a couple hours. As time passes, you hear cannon shots begin ringing out in the distance.\n"
                                                                               "The forest is quite large, filled with lakes and hilly terrain, but you haven't found any additional resources yet. \nThen, all of a sudden you hear some leaves rustling, which quickly puts you on alert to turn around and see it's another tribute hiding in the bush next to you.\n"
                                                                               "'Please don't attack! I'm unarmed, and if you don't eliminate me, we can both work together and increase both our chances of winning!' The Tribute shouts. You notice he has bandages sticking out in his right pocket. \n"
                                                                               "\n\nDo you tell him that you agree to align with him [1], or do you attack him [2]?")
    cornucopia_escape_lose = story.add_right(cornucopia_loot_and_escape_attempt, "You are overpowered, and eliminated.")
    woods_trick = story.add_left(cornucopia_escape_win, "'Okay, okay.' The Tribute mutters, breathing a sigh of relief. He turns around to give himself a moment to collect himself. "
                                                         "\nYou take advantage of his foolish naivety, striking him in the back before he has any chance to react or fight back, eliminating him."
                                                         "\nYou grab his leftover bandages. Do you wish to use them [1], or leave them [2]?", event_type="Loot", post_loot_string="\nYou hear a cannon shot ring out right away, and upon traveling further into the woods, you realize that there is only one other tribute left. "
                                                                                                                                                      "\nYou make your way back toward the Cornucopia, and you see the final tribute, wielding a battle axe, who is very visibly injured from previous fights."
                                                                                                                                                                                  "\n\nDo you attempt to attack him head-on [1], or try to sneak attack him? [2]", loot="Bandages", loot_type="Healing")
    woods_attack = story.add_right(cornucopia_escape_win, "'No!' The tribute yells in panic as you begin to lunge toward him, and he quickly starts running away before you can attack, and escapes successfully.\n"
                                                          "Upon traveling further into the woods, you realize that there is only one other tribute left. "
                                                        "\nYou make your way back toward the Cornucopia, and you see the final tribute, wielding a battle axe, who is very visibly injured from previous fights." "\n\nDo you attempt to attack him head-on [1], or try to sneak attack him? [2]")
    cornucopia_head_on = story.add_left(woods_trick, "You charge at him head on, ready to strike first.", event_type="Combat", hp=1, weapon=90)
    cornucopia_sneak_attack = story.add_right(woods_trick, "You start sneaking up behind him in an attempt to attack him off-guard. However, he hears your footsteps and turns around, swinging at you first, catching you off guard.", event_type="Combat", hp=1, weapon=90, user_first=False)
    cornucopia_sneak_attack_win = story.add_left(cornucopia_sneak_attack,
                                                 "Despite being caught off guard, you survive the blow and manage to eliminate him."
                                                 "\n\nYou are victorious! You have survived and your name will be passed down for generations.")
    cornucopia_sneak_attack_lose = story.add_right(cornucopia_sneak_attack,
                                                   "\n\nA single axe blow is enough to completely overpower you. You have been eliminated.")
    cornucopia_head_on_win = story.add_left(cornucopia_head_on, "You managed to get the first hit in, which was enough to eliminate him before he could fight back."
                                                                "\n\nYou are victorious! You have survived and your name will be passed down for generations.")
    cornucopia_head_on_lose = story.add_right(cornucopia_head_on, "\n\nA single axe blow is enough to completely overpower you. You have been eliminated.")
    alt_cornucopia_head_on = story.add_left(woods_attack, "You charge at him head on, ready to strike first.",
                                        event_type="Combat", hp=1, weapon=90)
    alt_cornucopia_sneak_attack = story.add_right(woods_attack,
                                              "You start sneaking up behind him in an attempt to attack him off-guard. However, he hears your footsteps and turns around, swinging at you first, catching you off guard.",
                                              event_type="Combat", hp=1, weapon=90, user_first=False)
    alt_cornucopia_sneak_attack_win = story.add_left(alt_cornucopia_sneak_attack, "You manage to miraculously survive and eliminate him. However, immediately, you get attacked from the back with a stone from the tribute you attempted to eliminate earlier.", event_type="Combat", hp=50, weapon=20, user_first=False)
    alt_cornucopia_sneak_attack_win_win = story.add_left(alt_cornucopia_sneak_attack_win, "You manage to also eliminate the last tribute. \n\nYou are victorious! You have survived and your name will be passed down for generations.")
    alt_cornucopia_sneak_attack_lose = story.add_right(alt_cornucopia_sneak_attack, "A single axe blow is enough to completely overpower you. You have been eliminated.")
    alt_cornucopia_sneak_attack_win_lose = story.add_right(alt_cornucopia_sneak_attack_win, "You are unable to win against the final tribute. You have been eliminated.")
    alt_cornucopia_head_on_win = story.add_left(alt_cornucopia_head_on,
                                            "You managed to get the first hit in, which was enough to eliminate him before he could fight back."
                                            "\n\nHowever, immediately, you get attacked from the back with a stone from the tribute you attempted to eliminate earlier.", event_type="Combat", hp=50, weapon=20, user_first=False)
    alt_cornucopia_head_on_win_win = story.add_left(alt_cornucopia_head_on_win, "Although he caught you off guard, you manage to win the fight. \n\nYou are victorious! You have survived and your name will be passed down for generations.")
    alt_cornucopia_head_on_win_lose = story.add_right(alt_cornucopia_head_on_win, "You are unable to win against the final tribute. You have been eliminated.")
    alt_cornucopia_head_on_lose = story.add_right(alt_cornucopia_head_on,
                                              "\n\nA single axe blow is enough to completely overpower you. You have been eliminated.")


    current = start
    # while current.left and current.right:
    #     print(current.event_string)
    #     choice = input("Select Choice [1, 2] or view stats with [3]: ")
    #     current = story.navigate(current, user, choice)
    # if current:
    #     print(current.event_string)
    # story.preorder()
    # story.inorder()
    # story.postorder()
    story.find_path(1)
    print(story.height())
    print(story.count_leaves())

begin = input("Welcome to the Hunger Games Simulator. Do you wish to begin [1], or exit? [2]: ")
while begin != "1" and begin != "2":
    print("Invalid choice, try again.")
    begin = input("Welcome to the Hunger Games Simulator. Do you wish to begin [1], or exit? [2]: ")
while begin == "1":
    compile_events()
    begin = input("Do you want to restart [1], or exit? [2]: ")
    while begin != "1" and begin != "2":
        print("Invalid choice, try again.")
        begin = input("Do you want to restart [1], or exit? [2]: ")
