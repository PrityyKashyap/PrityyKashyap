from PIL import Image
import numpy as np
import os

BASE = os.path.dirname(os.path.dirname(__file__))

image_path = os.path.join(BASE, "images", "img.jpeg")

image = Image.open(image_path).convert("L")

new_width = 60

ratio = image.height / image.width
new_height = int(new_width * ratio * 0.55)

image = image.resize((new_width, new_height))

pixels = np.array(image)

chars = np.array(list("@%#*+=-:. "))

normalized = pixels / 255 * (len(chars) - 1)

ascii_image = chars[normalized.astype(int)]

# Convert to list of strings
lines = ["".join(row) for row in ascii_image]

# Find the last non-space character in all rows
max_len = max(len(line.rstrip()) for line in lines)

# Remove only trailing blank columns
lines = [line[:max_len] for line in lines]

# Save
ascii_text = "\n".join(lines)

text_path = os.path.join(BASE, "ascii_art.txt")

with open(text_path, "w") as f:
    f.write(ascii_text)

print("ASCII text saved!")

ascii_text = "\n".join("".join(row) for row in ascii_image)

text_path = os.path.join(BASE, "ascii_art.txt")

with open(text_path, "w") as f:
    f.write(ascii_text)

print("✅ ASCII Art saved!")
print(text_path)