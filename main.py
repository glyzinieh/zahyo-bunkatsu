import os

from PIL import Image


def bunkatsu(max_zoom, image_path):
    save_dir = os.path.splitext(image_path)[0]
    if not os.path.exists(f"tiles/{save_dir}"):
        os.mkdir(f"tiles/{save_dir}")

    base_file = Image.open(image_path)
    for z in range(max_zoom + 1):
        root = 2**z

        width = base_file.width / root
        height = base_file.height / root

        for x in range(root):
            sx = width * x
            ex = sx + width
            for y in range(root):
                sy = height * y
                ey = sy + height
                base_file.crop((sx, sy, ex, ey)).resize((256, 256)).save(
                    f"tiles/{save_dir}/{z}_{x}_{y}.png"
                )
    base_file.close()


max_zoom = int(input("最大ズームレベル:"))

dir_path = os.getcwd()
files = [f for f in os.listdir(dir_path) if os.path.splitext(f)[1] == ".png"]

if not os.path.exists("tiles"):
    os.mkdir("tiles")

for image_path in files:
    bunkatsu(max_zoom, image_path)
