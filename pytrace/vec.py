class Vec3:
    def __init__(self, e0:float=0, e1:float=0, e2:float=0):
        self.e0:float = e0
        self.e1:float = e1
        self.e2:float = e2
    
    def __neg__(self):
        ret = Vec3(-self.e0, -self.e1, -self.e2)
        return ret
    
    @property
    def x(self):
        return self.e0
    
    @property
    def y(self):
        return self.e1
    
    @property
    def z(self):
        return self.e2
    
    def __add__(self, o):
        return Vec3(
            self.x + o.x,
            self.y + o.y,
            self.z + o.z
        )
    
    def __radd__(self, o):
        if o == 0:
            return self
    
    def __getitem__(self, i):
        d = [self.e0, self.e1, self.e2]
        return d[i]
    
    def __repr__(self):
        return f"Vec3({self.x}, {self.y}, {self.z})"

    def __unicode__(self):
        return f"({self.x}, {self.y}, {self.z})"

    @property
    def tuple(self):
        return self.x, self.y, self.z
