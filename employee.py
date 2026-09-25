# Create the employee.csv file and add employees
with open('employee.csv', 'w') as file:
    file.write('Name,Position,Salary\n')
    file.write('John Doe,Software Engineer,80000\n')
    file.write('Jane Smith,Project Manager,90000\n')
    file.write('Emily Johnson,Data Analyst,75000\n')

# Read and display the employees
with open('employee.csv', 'r') as file:
    for line in file:
        print(line.strip())

# Add a new employee
with open('employee.csv', 'a') as file:
    file.write('Michael Brown,UX Designer,70000\n')

# Delete a specific employee
employee_name = 'John Doe'

with open('employee.csv', 'r') as file:
    lines = file.readlines()

with open('employee.csv', 'w') as file:
    for line in lines:
        if not line.startswith(employee_name + ','):
            file.write(line)

# Read the specific employee
employee_name = 'John Doe'

with open('employee.csv', 'r') as file:
    for line in file:
        if line.startswith(employee_name + ','):
            print(line.strip())

# Delete a full employee table
with open('employee.csv', 'w') as file:
    pass

# Update a specific employee data
employee_name = 'John Doe'
new_salary = '85000'

with open('employee.csv', 'r') as file:
    lines = file.readlines()

with open('employee.csv', 'w') as file:
    for line in lines:
        if line.startswith(employee_name + ','):
            parts = line.strip().split(',')
            parts[2] = new_salary
            line = ','.join(parts) + '\n'

        file.write(line)
