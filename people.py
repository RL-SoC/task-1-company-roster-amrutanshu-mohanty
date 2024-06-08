"""
We'll try to understand classes in python. 
Check the resources on google classroom to ensure you have gone through everything expected.

"""
###### THESE LISTS HAVE ALREADY BEEN DEFINED FOR YOU ###############
engineer_roster = [] # A list of all instantiated engineer objects
sales_roster = [] # List of all instantiated sales objects
branchmap = {  # A dictionary of dictionaries -> Maps branchcodes to cities and branch names
    0:  { "city": "NYC", "name": "Hudson Yards"},
    1:  { "city": "NYC" , "name": "Silicon Alley"},
    2:  { "city": "Mumbai", "name": "BKC"},
    3:  { "city": "Tokyo", "name": "Shibuya"},
    4:  { "city": "Mumbai", "name": "Goregaon"},
    5:  { "city": "Mumbai", "name": "Fort"}
}
####################################################################

class Employee:
    pass

class Salesman:
    pass

def employeefinder(ID: int) -> Employee:
    found_employee = None
    for employee in engineer_roster + sales_roster:
        if employee.ID == ID:
            found_employee = employee
            break
    return found_employee

def salesfinder(ID: int) -> Salesman:
    found_employee = None
    for employee in sales_roster:
        if employee.ID == ID:
            found_employee = employee
            break
    return found_employee


class Employee:
    name : str 
    age : int
    ID : int
    city : str
    branches : list[int] # This is a list of branches (as branch codes) to which the employee may report
    salary : int 

    def __init__(self, name, age, ID, city,\
                 branchcodes, salary = None):
        self.name = name
        self.age = age 
        self.ID = ID
        self.city = city
        self.branches = branchcodes
        if salary is not None: self.salary = salary
        else: self.salary = 10_000 
    
    def change_city(self, new_city:str) -> bool:
        # Change the city 
        # Return true if city change, successful, return false if city same as old city
        if self.city.lower() == new_city.lower():
            return False
        else:
            self.city = new_city
        return True

    def migrate_branch(self, new_code:int) -> bool:
        # Should work only on those employees who have a single 
        # branch to report to. Fail for others.
        # Change old branch to new if it is in the same city, else return false.
        branchcode = self.branches[0]
        if len(self.branches) != 1 or branchmap[branchcode]["name"] != branchmap[new_code]["name"]:
            # or just simply use self.city.lower() instead of branchmap[branchcode]["name"] and ofcourse .lower()
            # with branchmap[new_code]["name"] as well
            # Also we added no checks for if wrong branch and city are entered
            return False
        else:
            self.branches[0] = new_code
        return True

    def increment(self, increment_amt: int) -> None:
        # Increment salary by amount specified.
        self.salary += increment_amt
        return





class Engineer(Employee):
    position : str # Position in organization Hierarchy

    def __init__(self, name, age, ID, city,\
                 branchcodes, position= "Junior", salary = None):
        # Call the parent's constructor
        super().__init__(name, age, ID, city, branchcodes, salary)
        
        # Check if position is one of  "Junior", "Senior", "Team Lead", or "Director" 
        # Only then set the position. 
        if position.lower() in ["junior", "senior", "team lead", "director"]:
            self.position = position

    
    def increment(self, amt:int) -> None:
        # While other functions are the same for employee and engineer,
        # an increment to an engineer's salary should add a 10% bonus on to "amt"
        self.salary += int(1.1*amt)
        return
    
    def promote(self, position:str) -> bool:
        # Return false for a demotion or an invalid promotion
        # Promotion can only be to a higher position and
        # it should call the increment function with 30% of the present salary
        # as "amt". Thereafter return True.
        positions_dict = {"junior" : 0, "senior" : 1, "team lead" : 2, "director" : 3}
        if position.lower() not in positions_dict.keys():
            return False
        # don't want to implement both the ifs together as in the second if
        # we will run into the issue of invalid key if position provided is
        # not in the list
        if positions_dict[position.lower()] <= positions_dict[self.position.lower()]:
            return False
        else:
            self.position = position
            self.increment(0.3*self.salary)      
        return True


class Salesman(Employee):
    """ 
    This class is to be entirely designed by you.

    Add increment (this time only a 5% bonus) and a promotion function
    This time the positions are: Rep -> Manager -> Head.

    Add an argument in init which tracks who is the superior
    that the employee reports to. This argument should be the ID of the superior
    It should be None for a "Head" and so, the argument should be optional in init.
    """
    
    # An extra member variable!
    superior : int # EMPLOYEE ID of the superior this guy reports to

    def __init__(self, name, age, ID, city, branchcodes, position="Rep", salary=None, superior=None): # Complete all this! Add arguments
        super().__init__(self, name, age, ID, city, branchcodes, salary)
        self.position = position
        if position.lower() != "head": self.superior = superior
        else: self.superior = None
    
    
    # def increment 
    def increment(self, increment_amt: int) -> None:
        return super().increment(int(1.05*increment_amt)) # alternate way to increment, this time by calling parent function
    
    # def promote
    def promote(self, position:str, superior:int) -> bool:
        # Return false for a demotion or an invalid promotion
        # Promotion can only be to a higher position and
        # it should call the increment function with 30% of the present salary
        # as "amt". Thereafter return True.
        positions_dict = {"rep" : 0, "manager" : 1, "head" : 2}
        if position.lower() not in positions_dict.keys():
            return False
        # don't want to implement both the ifs together as in the second if
        # we will run into the issue of invalid key if position provided is
        # not in the list
        if positions_dict[position.lower()] <= positions_dict[self.position.lower()]:
            return False
        else:
            self.position = position
            self.increment(0.3*self.salary)
            self.superior = superior # add some check for this?      
        return True

    def find_superior(self) -> tuple[int, str]:
        # Return the employee ID and name of the superior
        # Report a tuple of None, None if no superior.
        if self.superior == None:
            return None, None
        for salesperson in sales_roster:
            if salesperson.ID == self.superior:
                return salesperson.ID, salesperson.name
        return None, None

    def add_superior(self, ID: int) -> bool:
        # Add superior of immediately higher rank.
        # If superior doesn't exist return false,
        positions_dict = {"rep" : 0, "manager" : 1, "head" : 2}
        found = False
        for salesperson in sales_roster:
            if salesperson.ID == ID and positions_dict[salesperson.position.lower()] == positions_dict[self.position.lower()] + 1:
                self.superior = ID
                return True
        return False


    def migrate_branch(self, new_code: int) -> bool:
        # This should simply add a branch to the list; even different cities are fine
        for citycode in self.branches:
            if citycode == new_code:
                return False
        self.branches.apppend(citycode)
        return True

# Have to check .lower() and other such cases
# Issues of nonsensical input, for example when city doesn't match branch
# Superior thing in salesperson and how exactly I want to implement it and handle exceptions
# Maybe use add superior and find superior in defining promotion
