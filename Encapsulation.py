


class Password:
    def __init__(self):
        self._passwordVar = 1234 #the protected value, one underscore
        self.__privateVar = 1234 #the private value, two underscores

    #get private function
    def get_private(self):
        print("Private variable value:", self.__privateVar)

    #set private function
    def set_private(self, private):
        self.__privateVar = private
        
    #get protected function
    def get_protected(self):
        print("Protected variable value:", self._passwordVar)

    #set protected function
    def set_protected(self, password):
        self._passwordVar = password


#object of password
obj = Password()

#getting the protected value
obj.get_protected() 

#changes the protected value
obj.set_protected(34)
#prints value
obj.get_protected()  

#getting the private value, printing it
obj.get_private() 


#changing the private value
obj.set_private(5678)
#prints it
obj.get_private()

