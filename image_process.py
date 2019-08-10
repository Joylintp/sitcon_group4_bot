from PIL import Image

def img_pro(path):
    col = Image.open(path)
    gray = col.convert('L')
    bw = gray.point(lambda x : 0 if x < 128 else 255, '1')
    bw.save("pic.jpg")