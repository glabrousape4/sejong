from PIL import Image
img = Image.open(r"C:/Users/glabr/.cloudflared/sites/sejong/compare-output.png")
img.save(r"C:/Users/glabr/.cloudflared/sites/sejong/compare-output.png", dpi=(300, 300), optimize=True)
print("DPI set:", Image.open(r"C:/Users/glabr/.cloudflared/sites/sejong/compare-output.png").info.get('dpi'))
import os
print("Size:", os.path.getsize(r"C:/Users/glabr/.cloudflared/sites/sejong/compare-output.png"), "bytes")
