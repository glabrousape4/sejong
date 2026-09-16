from PIL import Image
img = Image.open(r"C:/Users/glabr/.cloudflared/sites/sejong/compare-output.png")
img.save(r"C:/Users/glabr/.cloudflared/sites/sejong/compare-output.png", dpi=(300, 300), optimize=True)
print("Size:", img.size)
print("Bytes:", __import__('os').path.getsize(r"C:/Users/glabr/.cloudflared/sites/sejong/compare-output.png"))
