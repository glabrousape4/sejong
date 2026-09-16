
from PIL import Image
import os
img = Image.open(r"C:\Users\glabr\.cloudflared\sites\sejong\compare-output.png")
print("Size:", img.size)
print("DPI:", img.info.get('dpi'))
print("File size:", os.path.getsize(r"C:\Users\glabr\.cloudflared\sites\sejong\compare-output.png"), "bytes")
