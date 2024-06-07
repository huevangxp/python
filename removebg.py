from rembg import remove
from PIL import Image

input_path = "./huevang.png"
output_path = "output.png"

input = Image.open(input_path)
output = remove(input)
print(output)
output.save(output_path)
