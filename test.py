from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Shopping cart")

# Use a raw string literal for the icon path
root.iconbitmap(r"C:\Users\natha\PycharmProjects\EGX154\Preo-x-Nathan-code-\images")

# Use the full path for the image and resize it
image_path = r"C:\Users\natha\PycharmProjects\EGX154\Preo-x-Nathan-code-\images\aceOfClubs.jpg"
image = Image.open(image_path)
resized_image = image.resize((150, 300))  # Resize the image to 200x200 pixels
img = ImageTk.PhotoImage(resized_image)

panel = Label(root, image=img)
panel.pack()

root.mainloop()
