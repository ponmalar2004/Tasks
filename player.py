# Create the player.csv file and add players
with open('player.csv', 'w') as file:
    file.write('Name,Position,Salary\n')
    file.write('Dhoni,Wicket Keeper,100000\n')
    file.write('virat kohli,Top order Batsman,90000\n')
    file.write('suresh raina,All-rounder,75000\n')

# Read and display the player
with open('player.csv', 'r') as file:
    for line in file:
        print(line.strip())

# Add a new player
with open('player.csv', 'a') as file:
    file.write('bhuvi,Bowler,70000\n')

# Delete a specific player
player_name = 'Dhoni'

with open('player.csv', 'r') as file:
    lines = file.readlines()

with open('player.csv', 'w') as file:
    for line in lines:
        if not line.startswith(player_name + ','):
            file.write(line)

# Read the specific player data
player_name = 'Dhoni'

with open('player.csv', 'r') as file:
    for line in file:
        if line.startswith(player_name + ','):
            print(line.strip())

# Delete a full player table
with open('player.csv', 'w') as file:
    pass

# Update a specific player data
player_name = 'Dhoni'
new_salary = '120000'

with open('player.csv', 'r') as file:
    lines = file.readlines()

with open('player.csv', 'w') as file:
    for line in lines:
        if line.startswith(player_name + ','):
            parts = line.strip().split(',')
            parts[2] = new_salary
            line = ','.join(parts) + '\n'

        file.write(line)