from PIL import Image
import pathlib
import glob

image_dir = pathlib.Path('./temp')
png_path = list(image_dir.glob('**/*.png'))

def resize_png(image_path, save_path):
    img = Image.open(image_path)
    img_resize = img.resize((img.width // 2, img.height // 2))
    img_resize.save(str(save_path), "PNG")

for i in png_path:
    m = "./" + str(i)
    n = './resize/' + str(i.stem) + '.png'
    resize_png(m, n)