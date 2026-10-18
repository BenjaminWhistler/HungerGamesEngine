import HungerGamesClasses

"""
Here is a custom playground where you can create your own Hunger Games story,
and test out different any functions, classes or methods included in the package.
"""
def compile_events():
    story = HungerGamesClasses.BinaryTree()
    user = HungerGamesClasses.Tribute()
    start = story.set_root("")


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