import tkinter as tk
from PIL import Image, ImageTk
import zlib
import struct
import sys

def parse_compressed_psri(psri_path):
    with open(psri_path, 'rb') as file:

        width, height = struct.unpack('II', file.read(8))
        
 
        compressed_data = file.read()

        raw_data = zlib.decompress(compressed_data)

    pixels = []
    for i in range(0, len(raw_data), 3):
        r, g, b = raw_data[i:i+3]
        pixels.append((r, g, b))
    
    return width, height, pixels

def resize_image(image, max_width, max_height):
   
    width, height = image.size
    scale_factor = min(max_width / width, max_height / height)
    

    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)
    
    return image.resize((new_width, new_height), Image.LANCZOS)

def view_compressed_psri(psri_path):
    width, height, pixels = parse_compressed_psri(psri_path)


    image = Image.new('RGB', (width, height))
    image.putdata(pixels)


    window = tk.Tk()
    window.title("Compressed PSRI Image Viewer")


    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()


    max_width = int(screen_width * 0.8)
    max_height = int(screen_height * 0.8)
    resized_image = resize_image(image, max_width, max_height)


    tk_image = ImageTk.PhotoImage(resized_image)


    label = tk.Label(window, image=tk_image)
    label.pack()


    window.mainloop()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        psri_path = sys.argv[1]
        view_compressed_psri(psri_path)
    else:
        print("Please drag and drop a .psri file onto this script icon to view it.")
