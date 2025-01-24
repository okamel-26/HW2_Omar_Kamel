print("Hi, welcome to the Net Salary Calculator!")

try:
    # Inputs used
    gross_salary = input("Please enter your gross salary: ")
    gross_salary = int(gross_salary)
    no_children = input("How many children do you have? ")
    no_children = int(no_children)

    tax_rate = 0

    # The base tax rate
    if gross_salary < 1000:
        tax_rate = 0.10
    elif gross_salary < 2000:
        tax_rate = 0.12
    elif gross_salary < 4000:
        tax_rate = 0.14
    else:
        tax_rate = 0.18

    # Calculating the tax cut based on the number of children
    if gross_salary < 2000:
        tax_cut = no_children * 0.01
    if gross_salary > 2000:
        tax_cut = no_children * 0.005

    # Ensuring the tax cut does not make the tax rate negative
    tax_rate -= tax_cut
    if tax_rate < 0:
        tax_rate = 0

    # Calculating the net salary
    net_salary = gross_salary * (1 - tax_rate)

    print("Your net salary is: ", round(net_salary, 2))

except ValueError:
    print("Invalid input. Please enter your gross salary numerically and the number of children you have.")