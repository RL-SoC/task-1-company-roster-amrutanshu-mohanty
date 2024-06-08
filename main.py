"""
This is where the actual working of the program will happen!
We'll be Querying stuff for testing whether your classes were defined correctly

Whenever something inappropriate happens (like a function returning false in people.py),
raise a Value Error.
"""
from people import * # import everything!

if __name__ == "__main__":  # Equivalent to int main() {} in C++.
    last_input = 99
    while last_input != 0:
        last_input = int(input("Please enter a query number:"))

        if last_input == 1:
            name = input("Name: ")
            age = input("Age: ")
            ID = input("ID: ")
            city = input("City: ")
            branchcodes = input("Branch(es): ")
            # How will you conver this to a list, given that
            # the user will always enter a comma separated list of branch codes?
            # eg>   2,5
            branchcodes = list([int(x) for x in branchcodes.split(',')])
            position = input("Position: ")
            salary = input("Salary: ")
            # Create a new Engineer with given details.
            engineer = None # Change this
            engineer = Engineer(name, int(age), int(ID), city, branchcodes, position, int(salary))
            engineer_roster.append(engineer) # Add him to the list! See people.py for definiton
            
        
        elif last_input == 2:
            # Gather input to create a Salesperson
            # Then add them to the roster
            name = input("Name: ")
            age = input("Age: ")
            ID = input("ID: ")
            city = input("City: ")
            branchcodes = list(map(int(x) for x in input("Branch(es): ").split(",")))
            position = input("Position: ")
            salary = input("Salary: ")
            superior = input("Superior ID: ")

            salesperson = Salesman(name, int(age), int(ID), city, branchcodes, position, int(salary), int(superior)) 
            sales_roster.append(salesperson) 

        elif last_input == 3:
            ID = int(input("ID: "))
            # Print employee details for the given employee ID that is given. 
            
            try:
                found_employee = employeefinder(ID)
                print(f"Name: {found_employee.name} and Age: {found_employee.age}")
                print(f"City of Work: {found_employee.city}")

                ## Write code here to list the branch names to
                ## which the employee reports as a comma separated list
                ## eg> Branches: Goregaon,Fort
                branch_names = []
                for branchcode in found_employee.branchcodes:
                    branch_names.append(branchmap[branchcode]["name"])
                ## ???? what comes here??
                # print(f"Branches: " + ???? )
                #print("Branches: ", end="")
                #[print(branch, end = ", ") for branch in branch_names]
                branches = "Branches: "
                for branch in branch_names:
                    branches = branches + branch + ", "
                print(branches.rstrip(", "))
                print(f"Position: {found_employee.position}")
                print(f"Salary: {found_employee.salary}")
            except:
                print("No such employee")

        elif last_input == 4:
            #### NO IF ELSE ZONE ######################################################
            # Change branch to new branch or add a new branch depending on class
            # Inheritance should automatically do this. 
            # There should be no IF-ELSE or ternary operators in this zone

            # one if else to check if employee exists
            ID = int(input("ID: "))
            try:
                found_employee = employeefinder(ID)
                found_employee.migrate_branch(int(input("New branch code: ")))
            except:
                print("No such employee")

            #### NO IF ELSE ZONE ENDS #################################################

        elif last_input == 5:
            ID = int(input("Enter Employee ID to promote: "))
            # promote employee to next position
            try:
                found_employee = employeefinder(ID)
                found_employee.promote(input("Enter new position: "))
            except:
                print("No such employee")

        elif last_input == 6:
            ID = int(input("Enter Employee ID to give increment: "))
            # Increment salary of employee.
            try:
                found_employee = employeefinder(ID)
                found_employee.increment(int(input("Enter increment amount: ")))
            except:
                print("No such employee")
        
        elif last_input == 7:
            ID = int(input("Enter Employee ID to find superior: "))
            # Print superior of the sales employee.
            try:
                found_employee = salesfinder(ID)
                print(found_employee.find_superior()) 
            except:
                print("No such employee")

        
        elif last_input == 8:
            ID_E = int(input("Enter Employee ID to add superior: "))
            ID_S = int(input("Enter Employee ID of superior: "))
            # Add superior of a sales employee
            try:
                found_employee = salesfinder(ID_E)
                found_employee.add_superior(ID_S) 
            except:
                print("No such employee")

        else:
            raise ValueError("No such query number defined")

            
            

            


            


        






