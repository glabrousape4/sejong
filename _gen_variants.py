
import os
import subprocess
from PIL import Image

src = r"C:\Users\glabr\.cloudflared\sites\sejong\compare-output.png"

# Original: 7200x6300 PNG 909 KB 300 DPI

# OPTION A: JPG 92% quality (~400 KB, same resolution)
# Convert PNG to JPG with 300 DPI
img = Image.open(src)
print(f"Original: {img.size}")
# Drop alpha if present
if img.mode in ('RGBA', 'LA'):
    bg = Image.new('RGB', img.size, (255, 255, 255))
    bg.paste(img, mask=img.split()[-1])
    img = bg
elif img.mode != 'RGB':
    img = img.convert('RGB')

# Save as 4000x3500 JPG (downscaled for normal use, high quality)
img_4000 = img.copy()
img_4000.thumbnail((4000, 3500), Image.LANCZOS)
img_4000.save(src.replace('.png', '-4000.jpg'), 'JPEG', dpi=(300, 300), quality=92, optimize=True, progressive=True)
print(f"4000px JPG: {os.path.getsize(src.replace('.png', '-4000.jpg')):,} bytes")

# OPTION B: Smaller 2400x2100 JPG (~200 KB)
img_2400 = img.copy()
img_2400.thumbnail((2400, 2100), Image.LANCZOS)
img_2400.save(src.replace('.png', '-2400.jpg'), 'JPEG', dpi=(300, 300), quality=92, optimize=True, progressive=True)
print(f"2400px JPG: {os.path.getsize(src.replace('.png', '-2400.jpg')):,} bytes")

# OPTION C: PNG optimized smaller version
img_optimized = Image.open(src)
img_optimized.thumbnail((3600, 3150), Image.LANCZOS)
img_optimized.save(src.replace('.png', '-3600.png'), 'PNG', dpi=(300, 300), optimize=True)
print(f"3600px PNG: {os.path.getsize(src.replace('.png', '-3600.png')):,} bytes")

# Original full size
print(f"7200px PNG (current): {os.path.getsize(src):,} bytes")
