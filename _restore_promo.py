
from PIL import Image
import os

src = r"C:\Users\glabr\.cloudflared\sites\sejong\promo.png"
print(f"Original size: {os.path.getsize(src):,} bytes")

img = Image.open(src)
print(f"Dimensions: {img.size}")

# Resize to 800px wide (web-friendly)
target_w = 800
ratio = target_w / img.size[0]
target_h = int(img.size[1] * ratio)
img2 = img.resize((target_w, target_h), Image.LANCZOS)
print(f"Resized to: {img2.size}")

# Save as optimized PNG
img2.save(src, 'PNG', optimize=True, dpi=(300, 300))
print(f"Optimized PNG: {os.path.getsize(src):,} bytes")
