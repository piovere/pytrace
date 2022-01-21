from tqdm import trange, tqdm
from pytrace.vec import Color

def main():
    # set image dimensions
    image_width = 256
    image_height = 256

    with open("rendered.ppm", "w") as f:
        # Header
        hdr = f"P3\n{image_width} {image_height}\n255\n"
        f.write(hdr)

        # Image data
        for j in tqdm(range(image_height-1, -1, -1)):
            for i in trange(image_width, leave=False):
                r = i / (image_width - 1)
                g = j / (image_height - 1)
                b = 0.25

                pc = Color(r, g, b)
        
                f.write(f"{pc}")

main()
