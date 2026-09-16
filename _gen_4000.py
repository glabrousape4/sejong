
from PIL import Image
import os

img = Image.open(r"C:\Users\glabr\.cloudflared\sites\sejong\compare-output.png")
print("Original:", img.size)
print("Original DPI:", img.info.get('dpi'))

# Downscale 7200 → 4000 (preserves quality)
img_4000 = img.copy()
img_4000.thumbnail((4000, 3500), Image.LANCZOS)
print("New size:", img_4000.size)

# Save with 300 DPI + optimize=True (best PNG compression)
out_path = r"C:\Users\glabr\.cloudflared\sites\sejong\compare-output-4000.png"
img_4000.save(out_path, 'PNG', dpi=(300, 300), optimize=True)
print("Saved")
print("Size:", os.path.getsize(out_path), "bytes")
print("DPI:", Image.open(out_path).info.get('dpi'))
