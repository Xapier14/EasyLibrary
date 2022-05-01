from PIL import Image, ImageTk

def MakeSizedImage(imagePath, size):
    image = Image.open(imagePath)
    image = image.resize(size)
    return ImageTk.PhotoImage(image)