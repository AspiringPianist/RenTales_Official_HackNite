# pip install rembg
# benchmarked on Intel Macbook Air 2017, 8GB Ram, Intel HD 6000 -> 6~7 seconds per image
from rembg import remove
from PIL import Image

def clear_bg(input_path, output_path):
    input = Image.open(input_path)
    output = remove(input)
    output.save(output_path)