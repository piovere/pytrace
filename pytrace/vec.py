from __future__ import annotations
from typing import Union

class Vec3:
    def __init__(self, e0:float=0, e1:float=0, e2:float=0):
        self.e0:float = e0
        self.e1:float = e1
        self.e2:float = e2
    
    def __neg__(self) -> Vec3:
        ret = Vec3(-self.e0, -self.e1, -self.e2)
        return ret
    
    @property
    def x(self) -> float:
        return self.e0
    
    @property
    def y(self) -> float:
        return self.e1
    
    @property
    def z(self) -> float:
        return self.e2
    
    def __add__(self, o:Vec3) -> Vec3:
        return Vec3(
            self.x + o.x,
            self.y + o.y,
            self.z + o.z
        )
    
    def __radd__(self, o:Union[int, Vec3]) -> Vec3:
        if o == 0:
            return self
    
    def __sub__(self, o: Vec3) -> Vec3:
        return self + -o

    def __mul__(self, o: Union[int, float, Vec3]) -> Vec3:
        if isinstance(o, Union[int, float]):
            ret = Vec3(self.x * o, self.y * o, self.z * o)
        elif isinstance(o, Vec3):
            ret = Vec3(self.x * o.x, self.y * o.y, self.z * o.z)
        else:
            raise TypeError(
                f"Unsupported operation on {type(self)} and {type(o)}"
            )
        return ret
    
    def __rmul__(self, o: Union[int, float, Vec3]) -> Vec3:
        return self.__mul__(o)

    def length_squared(self) -> float:
        return self.x * self.x + self.y * self.y + self.z * self.z
    
    def length(self) -> float:
        return self.length_squared() ** 0.5

    def __getitem__(self, i) -> float:
        d = [self.e0, self.e1, self.e2]
        return d[i]
    
    def __repr__(self) -> str:
        return f"Vec3({self.x}, {self.y}, {self.z})"
    
    def __str__(self) -> str:
        return f"{self.x} {self.y} {self.z}"

    def __eq__(self, o) -> bool:
        return self.x == o.x and self.y == o.y and self.z == o.z

    @property
    def tuple(self) -> tuple[float, float, float]:
        return self.x, self.y, self.z
    
    def __truediv__(self, o:Union[int, float]) -> Vec3:
        return self * (1 / o)

    def dot(self, o):
        return sum(self * o)

    def unit_vector(self):
        return self / self.length()

Point3 = Vec3
Color = Vec3
