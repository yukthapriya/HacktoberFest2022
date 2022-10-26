from random import choice

cave_numbers = range(1,17)
w_l = choice(cave_numbers)
p_l = choice(cave_numbers)
G_l = choice(cave_numbers)
while p_l == w_l:
    p_l = choice(cave_numbers)
while G_l == w_l:
    G_l = choice(cave_numbers)
print("welcome to hunt the wumpus")
print("you can see", len(cave_numbers),"caves")
print("to play ,just type the number")
print("of the cave you wish to enter next")
while True:
    print("you are in cave",p_l)
    if(p_l == w_l -1 or
       p_l == w_l +1):
        print("i smell the wumpus!!")
    print("which cave next?")
    p_input = input(">")
    if(not p_input.isdigit() or int(p_input) not in cave_numbers):
           print(p_input,"not in a cave")
    else:
              p_location = int(p_input)
              if p_l == w_l:
                print("argh!! you have got eaten by wumpus")
              
              elif p_l == G_l:
                    print("you grabbed the gold")
                    print("Do you want to play again y or n")
                    p_input2 = input(">")
                    if(p_input2 == "n" or p_input2 == "N"):
                        break
              
              
