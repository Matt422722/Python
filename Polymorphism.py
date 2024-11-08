
#parent class
class Animal:
    species = "Unknown"
    diet = "Unknown"

    def information(self):
        msg = "\nSpecies: {}\nDiet: {}".format(self.species, self.diet)
        return msg

#Child class instance
class Horse(Animal):
    species = "Shire horse"
    diet = "Herbivore"

    def information(self):
        msg = "\nSpecies: {}\nDiet: {}".format(self.species, self.diet)
        return msg
    

#Another child class
class Scorpion(Animal):
    species = "Emperor scorpion"
    diet = "Carnivore"
    exoskeleton = "Yes"

    def information(self):
        msg = "\nSpecies: {}\nDiet: {}\nExoskeleton: {}".format(self.species, self.diet, self.exoskeleton)
        return msg



if __name__ == "__main__":
    horse = Horse()
    print(horse.information())

    scorpion = Scorpion()
    print(scorpion.information())

