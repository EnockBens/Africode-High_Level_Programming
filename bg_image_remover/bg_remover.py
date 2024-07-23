from  rembg import remove
from PIL import Image


img_path = r'/Users/mac/Downloads/Benz.jpeg'
img = Image.open(img_path)

r = remove(img)

output_path = r'/Users/mac/Documents/Benz2.png'
r.save(output_path)