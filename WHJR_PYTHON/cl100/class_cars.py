class Cars(object):
    def __init__(self, model, colour, company, speedlimit):
        self.model = model
        self.colour = colour
        self.company = company
        self.speedlimit = speedlimit

    def start(self):
        print ("Started")
    def stop(self):
        print("Stopped")
    def accelerate(self):
        print("Accelerate")
    def change_gear(self, gear_type):
        print("Change gear")
''' go to cmmand prompt, and call the class 
 audi = Cars("A6", "red" "Audi", "80")
 audi.color 
 *if executed the result will be "red"*
 '''