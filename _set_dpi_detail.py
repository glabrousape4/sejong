from PIL import Image
img = Image.open(r"C:/Users/glabr/.cloudflared/sites/sejong/detail-compare-render.png")
img.save(r"C:/Users/glabr/.cloudflared/sites/sejong/detail-compare-render.png", dpi=(300, 300), optimize=True)
print("Size:", img.size)
import os
print("Bytes:", os.path.getsize(r"C:/Users/glabr/.cloudflared/sites/sejong/detail-compare-render.png"))
