print('''   ,=====,---.
   /=====/=====\
   |=====|\=====;
   _j---j_|=====|
  /,-"0"-.\=====|
 //   |   \\====|
||9   o   3|D===|
 \\    `. //====|
  \`-.6.-'/=====|
   `j---j'|=====|
   |=====|/=====;
   \=====\=====/
    `-----`---'  ''')
print("Welcome to The Watch")
a = input("What time is it(12,3,6,9)?")
if a != '12':
    print("The clock does:")
    for i in range(int(a)):
        print("BONG")
    print("You are sitting in the sofa and there is knife on the counter, do you stand up and pick up the knife? Y/N")
    if input() == 'Y':
        'Now you have the knife, you can defend yourself in need'
        if input("Do you go back to sitting? Y/N") == 'Y':
            print("*The Creeper* shows up and kills you while you sit. The end.")
        else:
            print("You are standing with knife in your hand.")
        if input("The Creeper shows up. Attack or Defend?") == 'Attack':
            print("\nCreeper is shocked that you attack. You kill The Creeper. You survived. The end")
        else:
            print("\nThe Creeoer jumps to you. You try to swing at him but he is faster. You are dead. The end.")
    else:
        print("*The Creeper* shows up and kills you. The end.")
else:
    print("\n*The Creeper* shows up and kills you. The end.")
