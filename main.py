from PIL import Image

image_path = input("画像のパス:")
base_file = Image.open(image_path)

z = int(input("ズームレベル:"))
root = 2**z

width = base_file.width / root
height = base_file.height / root

for x in range(root):
    sx = width * x
    ex = sx + width
    for y in range(root):
        sy = height * y
        ey = sy + height
        base_file.crop((sx, sy, ex, ey)).resize((256, 256)).save(f"{z}_{x}_{y}.png")

base_file.close()
