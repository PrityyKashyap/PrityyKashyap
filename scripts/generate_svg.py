import os

BASE = os.path.dirname(os.path.dirname(__file__))

txt_path = os.path.join(BASE, "ascii_art.txt")
svg_path = os.path.join(BASE, "ascii.svg")

with open(txt_path, "r") as f:
    lines = f.readlines()

font_size = 8
line_height = 9
padding = 20

max_line = max(len(line.rstrip()) for line in lines)

width = max_line * font_size
height = len(lines) * line_height

height = len(lines) * line_height

svg = []

svg.append(f'''<svg xmlns="http://www.w3.org/2000/svg"
width="{width + padding * 2}"
height="{height}"
style="background:black">''')

svg.append(f'''
<style>
text {{
font-family: monospace;
font-size:{font_size}px;
fill:white;
white-space:pre;
}}
</style>
''')
for i, line in enumerate(lines):
    line = line.rstrip()
    line = (
        line.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
    )

    padding = 20

    svg.append(
        f'<text x="{padding}" y="{(i+1)*line_height}">{line}</text>'
    )

svg.append("</svg>")

with open(svg_path, "w") as f:
    f.write("\n".join(svg))

print("SVG Created Successfully!")
print(svg_path)