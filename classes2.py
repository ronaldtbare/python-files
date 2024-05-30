# This progam averages test scores
class Student:
    scores = [69, 38, 76, 54, 87, 100, 98]
    total = 0
    average = 0
    def average_score(self): # all methods in a class must have self passed in
                             # as self means 'the instance/object of a class
      
        for score in self.scores:
            self.total += score
        print("Total of test scores: ", self.total)
        num_tests = len(self.scores)
        print("Number of tests", num_tests)
        
        average = self.total / num_tests
        print("Average: ", average)
        return average

bob = Student() # creates and instance or object of Student class
bob.average_score()

