from __future__ import annotations
from tqdm import trange, tqdm
from pytrace.vec import Color, Point3, Vec3
from pytrace.ray import Ray

def ray_color(r: Ray) -> Color:
    if hit_sphere(Point3(0, 0, -1), 0.5, r):
        return Color(1, 0, 0)
    unit_direction: Vec3 = r.dir.unit_vector()
    t: float = 0.5 * (unit_direction.y + 1.0)
    return (1.0 - t) * Color(1, 1, 1) + t * Color(0.5, 0.7, 1.0)

def hit_sphere(center: Point3, radius: float, r: Ray) -> bool:
    oc: Vec3 = r.orig - center
    
    a = r.dir.dot(r.dir)
    b = 2 * oc.dot(r.dir)
    c = oc.dot(oc) - radius * radius
    
    discriminant = b * b - 4 * a * c
    return discriminant > 0

def main():
    # set image dimensions
    aspect_ratio: float = 16. / 9.
    image_width: int = 400
    image_height: int = int(image_width / aspect_ratio)
    
    # Camera
    viewport_height: float = 2.
    viewport_width: float = aspect_ratio * viewport_height
    focal_length: float = 1.
    
    origin: Point3 = Point3(0, 0, 0)
    horizontal: Vec3 = Vec3(viewport_width, 0, 0)
    vertical: Vec3 = Vec3(0, viewport_height, 0)
    lower_left_corner: Point3 = origin - (horizontal / 2) - (vertical / 2) - Vec3(0, 0, focal_length)

    with open("blue_gradient.ppm", "w") as f:
        # Header
        hdr = f"P3\n{image_width} {image_height}\n255\n"
        f.write(hdr)

        # Image data
        for j in tqdm(range(image_height-1, -1, -1)):
            for i in trange(image_width, leave=False):
                u = i / (image_width - 1)
                v = j / (image_height - 1)
                
                r = Ray(origin, lower_left_corner + (u * horizontal) + (v * vertical) - origin)
                pc = ray_color(r)
                
                if not isinstance(pc, Color):
                    raise TypeError(f"Expected Color, not {type(pc)}")
        
                f.write(f"{pc}\n")

main()
