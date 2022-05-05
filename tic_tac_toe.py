print('''
                TIC-TAC-TOE
        CAN YOU WIN IN THREE MOVES?

RULE : Each Player has only 3 chances to win this.
       Your Success = Luck * Presence of mind :)
    ''')


p1 = " "
p2 = " "
p3 = " "
p4 = " "
p5 = " "
p6 = " "
p7 = " "
p8 = " "
p9 = " " 

user_1_answers = [] 
user_2_answers = []

replay = True

valid = (1,2,3,4,5,6,7,8,9)

win = [[1, 2, 3], [1, 5, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [3, 5, 7], [4, 5, 6], [7, 8, 9]]


while True:
    user_1 = input("Player 1 - Choose either 'X' or 'O' : ").upper()
    if (user_1 == "") :
        print("Please make a choice\n")
    elif user_1 == "X" :
        user_2 = "O"
        break
    else:
        user_2 = "X"
        break

table = (f'''
            |       | 
        7   |   8   |   9   
            |       | 
     -----------------------
            |       | 
        4   |   5   |   6   
            |       | 
     -----------------------  
            |       | 
        1   |   2   |   3   
            |       |  
      ''')

print(table)
    
print(f"As per your choice : Player 1 is '{user_1}' and Player 2 is '{user_2}'\n")


while replay: 
    
    player_1 = int(input("Player 1 - Choose between (1-9): "))

    user_1_answers.append(player_1)
    
    if player_1 == 1 :
        p1 = user_1
    elif player_1 == 2 :
        p2 = user_1
    elif player_1 == 3 :
        p3 = user_1
    elif player_1 == 4 :
        p4 = user_1
    elif player_1 == 5 :
        p5 = user_1
    elif player_1 == 6 :
        p6 = user_1
    elif player_1 == 7 :
        p7 = user_1
    elif player_1 == 8 :
        p8 = user_1
    elif player_1 == 9 :
        p9 = user_1

    
    table = (f'''
            |       | 
        {p7}   |   {p8}   |   {p9}   
            |       | 
     -----------------------
            |       | 
        {p4}   |   {p5}   |   {p6}   
            |       | 
     -----------------------  
            |       | 
        {p1}   |   {p2}   |   {p3}   
            |       |  
      ''')

    print(f'{table}\n Player 1 Move Counter: {len(user_1_answers)}\n')
    
    
    user_1_answers.sort()
    
    if user_1_answers in win:
        print("Congratulations!! Player 1, You Won!!")
        replay = False
        break

    player_2 = int(input("Player 2 - Choose between (1-9): "))

    user_2_answers.append(player_2)
    
    if player_2 == 1 :
        p1 = user_2
    elif player_2 == 2 :
        p2 = user_2
    elif player_2 == 3 :
        p3 = user_2
    elif player_2 == 4 :
        p4 = user_2
    elif player_2 == 5 :
        p5 = user_2
    elif player_2 == 6 :
        p6 = user_2
    elif player_2 == 7 :
        p7 = user_2
    elif player_2 == 8 :
        p8 = user_2
    elif player_2 == 9 :
        p9 = user_2
        
         
    table = (f'''
            |       | 
        {p7}   |   {p8}   |   {p9}   
            |       | 
     -----------------------
            |       | 
        {p4}   |   {p5}   |   {p6}   
            |       | 
     -----------------------  
            |       | 
        {p1}   |   {p2}   |   {p3}   
            |       |  
      ''')

    print(f'{table}\n Player 2 Move Counter: {len(user_2_answers)}\n')
    
    user_2_answers.sort()
    
    if user_2_answers in win :
        print("Congratulations!! Player 2, You Won!!")
        replay = False
        break

    if len(user_2_answers) == 3 :
        print("Sorry!! You used your all chances!")
        replay = False
        break        