
from PIL import Image
import os

src = r"C:\Users\glabr\AppData\Local\hermes\cache\images\img_84844ded49c8.png"
dst = r"C:\Users\glabr\.cloudflared\sites\sejong\promo-new.png"

img = Image.open(src)
print(f"Original size: {img.size}")
print(f"Original bytes: {os.path.getsize(src):,}")

# Resize to 800px wide (web-friendly, fits mobile + desktop)
target_w = 800
ratio = target_w / img.size[0]
target_h = int(img.size[1] * ratio)
img_resized = img.resize((target_w, target_h), Image.LANCZOS)
print(f"Resized: {img_resized.size}")

# Save as PNG with optimize
img_resized.save(dst, 'PNG', optimize=True, dpi=(300, 300))
print(f"PNG saved: {os.path.getsize(dst):,} bytes")

# Also save as JPG (smaller file size, same quality for photos)
dst_jpg = dst.replace('.png', '.jpg')
if img_resized.mode == 'RGBA':
    bg = Image.new('RGB', img_resized.size, (255, 255, 255))
    bg.paste(img_resized, mask=img_resized.split()[-1])
    img_resized = bg
img_resized.save(dst_jpg, 'JPEG', quality=88, optimize=True, progressive=True, dpi=(300, 300))
print(f"JPG saved: {os.path.getsize(dst_jpg):,} bytes")
