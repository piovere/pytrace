from tqdm import trange, tqdm

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

                almost = 255.999

                ir = int(almost * r)
                ig = int(almost * g)
                ib = int(almost * b)
        
                f.write(f"{ir} {ig} {ib}\n")

main()
