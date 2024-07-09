from PIL import Image
import zlib
import struct

def jpg_to_compressed_psri(jpg_path, psri_path):
    # Open the image using Pillow
    image = Image.open(jpg_path)
    width, height = image.size
    pixels = image.load()

    # Prepare raw pixel data
    raw_data = bytearray()
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y][:3]  # Ignore alpha channel if present
            raw_data.extend([r, g, b])
    
    # Compress the raw pixel data using zlib
    compressed_data = zlib.compress(raw_data)
    
    # Write the compressed data to a binary file
    with open(psri_path, 'wb') as file:
        # Write the width and height
        file.write(struct.pack('II', width, height))
        # Write the compressed pixel data
        file.write(compressed_data)

    print("Compressed PSRI file created successfully.")

# Example usage
jpg_path = 'example.jpg'  # Path to your JPG image
psri_path = 'example.psri'  # Path to save the compressed .psri file
jpg_to_compressed_psri(jpg_path, psri_path)
