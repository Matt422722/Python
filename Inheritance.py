
#creates User class and parameters
class = User:
    name = 'no Name Provided'
    email = ' '
    passowrd = '1234567890'
    account_number = 0
    

#creates the Supplier class and what they supply
class = Supplier:
    item = Pasta
    catagory = Food

    
#creates the Customer class based on User
class = Customer(User):
    mailing_address = ' '
    mailing_list = True
    
