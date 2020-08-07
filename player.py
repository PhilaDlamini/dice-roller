'''The player class'''
from random import randint;

class Player:
    
    def __init__(self, name):
        self.name = name;
        self.score = 0;
    
    def roll(self):
        
        print(self.name, "'s turn to roll! Enter 'Roll' to roll dice", sep = '');
        print(self.name, "'s current score is ",  self.score, sep = '');
        roll = input('');
        
        while roll.lower() != 'roll':
            print("Wrong input! Enter 'Roll' to roll the dice");
            roll = input('');
        
        points = randint(1, 6);
        self.score += points;
        
        print(self.name, ' rolled ', points, '!', sep = '');
        print(self.name, "'s score is now ", self.score, sep = '');
        
        if(self.score >= 10): 
            print(self.name, ' wins!!');
            print('The game ends');
            exit();
        