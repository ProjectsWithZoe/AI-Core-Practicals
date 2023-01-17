import math

class Cylinder:
    def __init__(self, height, radius=1):
        self.height = height
        self.radius = radius
        self.surface_area = self.get_surface_area()
        self.volume = self.get_volume()

    def get_surface_area(self):
        surface_area = (2*math.pi* self.radius * self.height) + (2 * math.pi * self.radius**2)
        return round(surface_area,2)

    def get_volume(self):
        volume = math.pi*self.radius**2*self.height
        return round(volume,2)


cylinder1=Cylinder(10,5)
print(cylinder1.get_surface_area())
print(cylinder1.get_volume())