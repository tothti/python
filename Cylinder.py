import math

class Cylinder():
    """
    This class represents a cylinder, which has height and ratio.

    """
    def __init__(self, height, ratio):
        self.height = height
        self.ratio = ratio
        self.diameter = self.ratio * 2

    def volume(self):
        """
        This method will calculate the volume of the cylinder.
        volume = m * r2 * pi

        >>> cylinder = Cylinder(3, 2)
        >>> cylinder.volume()
        37.7
        """
        total_volume = self.height * pow(self.ratio, 2) * math.pi
        return round(total_volume, 2)

    def surface(self):
        """
        This method will calculate the surface area of the cylinder.
        surface = 2 * pi * r * (m + r)

        >>> cylinder = Cylinder(3, 2)
        >>> cylinder.surface()
        62.83
        """
        total_surface = 2 * math.pi * self.ratio * (self.ratio + self.height)
        return round(total_surface, 2)

    def __repr__(self):
        """
        Represents the Cylinder's information
        :return:
        """
        return (f"Cylinder is {self.height} tall and has ratio of {self.ratio}")