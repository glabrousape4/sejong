
from PIL import Image
import os
src = r"C:\Users\glabr\.cloudflared\sites\sejong\promo-cafe.jpg"
img = Image.open(src)
print(f"Original: {img.size}, {os.path.getsize(src):,} bytes")
target_w = 800
ratio = target_w / img.size[0]
target_h = int(img.size[1] * ratio)
img2 = img.resize((target_w, target_h), Image.LANCZOS)
img2.save(src, 'JPEG', quality=88, optimize=True, progressive=True, dpi=(300, 300))
print(f"Optimized: {img2.size}, {os.path.getsize(src):,} bytes")
