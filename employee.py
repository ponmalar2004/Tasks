#write 
with open('employee.csv', 'w') as file:
    file.write('Name, Age , Role , College PassedOut\n')
    file.write('Ponmalar , 21 , Full Stack Trainee , 2026 \n')
    file.write('Dinesh , 22 , Data Engineering , 2025\n')
    file.write('Dhanush , 21, Gen AI Engineer , 2025 \n')

# Add a new employee
with open('employee.csv', 'a') as file:
    file.write('Dhanushiya , 21 , Full Stack Developer , 2025\n')

# Read
with open('employee.csv', 'r') as file:
    for line in file:
        print(line.strip())

# Delete a specific employee
employee_name = 'Ponmalar'

with open('employee.csv', 'r') as file:
    lines = file.readlines()

with open('employee.csv', 'w') as file:
    for line in lines:
        if not line.startswith(employee_name + ' , '):
            file.write(line)

# Delete a full employee table
with open('employee.csv', 'w') as file:
    pass

# Read specific employee
employee_name = 'Dinesh'

with open('employee.csv', 'r') as file:
    for line in file:
        if line.startswith(employee_name + ' , '):
            print(line.strip())


# Update a specific employee data
employee_name = 'Dhanush'
new_age = '22'

with open('employee.csv', 'r') as file:
    lines = file.readlines()

with open('employee.csv', 'w') as file:
    for line in lines:
        if line.startswith(employee_name + ' , '):
            parts = line.strip().split(',')
            parts[1] = new_age
            line = ' , '.join(parts) + '\n'

        file.write(line)