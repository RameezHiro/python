from random import randint


class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo
        
    def book(self, fro, to):
        print(f"Ticket is Booked in train no: {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    
    
    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo}  from {fro} to {to} is {randint(400,1500)}")


t = Train(12399) 
t.book("Kalos", "Delhi")   
t.getStatus()   
t.getFare("Kalos", "Delhi") 