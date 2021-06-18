

class ErrorValue :
    def __init__ (self, world):
        self.world = world
        super () .__init__ ()
        self.finity = 1_000_000_000     

    def input (self):   # Input from hardware
        super() .input ()
    
    def output (self):  # Output to hardware
        super () .output ()          
    
    def steeringAngle (self):
        return (self.world.physics.steeringAngle())
    def slipping (self):
        return (self.world.physics.slipping())
    def steeringAngle (self):
        return (self.world.physics.steeringAngle())        