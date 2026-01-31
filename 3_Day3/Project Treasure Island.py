treasure = """
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-   -'  o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
"""
print(treasure)
print("Welcome to Treasure Island.\n")
print("Your mission is to find the treasure.")
choose = input("You're at a cross road. Where do you want to go? Type 'left' ot 'right' \n").lower()
if choose == "left":
    choose = input("You're at a cross road. Where do you want to go? Type 'swim' or 'wait'\n").lower()
    if choose == 'wait':
        choose = input("Which door? Choose 'Red' or 'Yellow' or 'Blue'\n").lower()
        if choose == 'Red':
            print("You burned by fire. Game Over")
        elif choose == 'Yellow':
            print("You Win!")
        elif choose == 'Blue':
            print("You eaten by beasts. Game Over.")
        else:
            print("Game Over.")
    else:
        print("You attacked by trout. Game Over.")
else:
    print("You fall into a hole. Game Over.")
