class Tire:
    """
    Tire represents a tire that would be used with an automobile
    """
    def __init__(self, tire_type, width, ratio, diameter, brand='', construction='R'):
        self.tire_type = tire_type
        self.width = width
        self.ratio = ratio
        self.diameter = diameter
        self.brand = brand
        self.construction = construction
    def __repr__(self):
        """
        Represents the tire's information in the standard notation present on the side of the tire
        example: 'P215/65/R15'
        """
        return (f"{self.tire_type}{self.width}/{self.ratio}"
                + f"{self.construction}{self.diameter}")
    