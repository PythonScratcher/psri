from PIL import Image
import zlib
import struct

def jpg_to_compressed_psri(jpg_path, psri_path):

    image = Image.open(jpg_path)
    width, height = image.size
    pixels = image.load()

    
    raw_data = bytearray()
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y][:3] 
            raw_data.extend([r, g, b])
    

    compressed_data = zlib.compress(raw_data)
    
  
    with open(psri_path, 'wb') as file:
 
        file.write(struct.pack('II', width, height))
  
        file.write(compressed_data)

    print("Compressed PSRI file created successfully.")

# Example usage
jpg_path = 'example.jpg'  # Path to your JPG image
psri_path = 'example.psri'  # Path to save the compressed .psri file
jpg_to_compressed_psri(jpg_path, psri_path)
