class Car:
    """
    documentation
    Doctring describing the class
    car models a car w/ tires and an engine
    """
    def __init__(self, engine, tires):
        self.engine = engine
        self.tires = tires
        """
        Doctring describing the class
        """
    def description(self):
        print(f"Un automovil con un motor de  {self.engine} engine y {self.tires} llantas")
    def wheel_circumference(self):
        if len(self.tires) > 0:
            return self.tires[0].circumference()
        else:
            return 0