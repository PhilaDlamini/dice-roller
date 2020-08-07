from player import Player;

def main():
    
    print('Welcome to Dice Roller Inc. The first player to get to 10 wins!')
    players = [];
    playerCount = int(input('Number of players in game: '));
    
    while playerCount <= 1:
        print('Cannot have', playerCount, 'players in the game');
        playerCount = int(input('Enter valid number of players in game: '));
    
    for i in range(playerCount):
        name = input('Name of player ' + str(i + 1) + ': ');
        players.append(Player(name));
    
    while True:
        for player in players:
            player.roll();
        
        
main();
        
    