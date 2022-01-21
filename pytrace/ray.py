from __future__ import annotations
from .vec import Vec3, Point3

class Ray:
    def __init__(self, origin:Point3, direction:Vec3):
        self.orig: Point3 = origin
        self.dir: Vec3 = direction
        
    def at(self, t:float) -> Point3:
        return self.orig + t * self.dir
