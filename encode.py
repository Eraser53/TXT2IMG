from PIL import Image

def encode_file_to_image(file_path):
    # Read the content of the TXT file
    with open(file_path, 'rb') as file:
        file_content = file.read()
    
    # Determine the image dimensions
    image_width = 100
    image_height = (len(file_content) // 3) + 1  # Each pixel encodes 3 bytes
    
    # Create a new image
    image = Image.new('RGB', (image_width, image_height))
    
    # Encode the file content into pixel colors
    pixel_index = 0
    for byte in file_content:
        red = byte
        green = byte
        blue = byte
        image.putpixel((pixel_index % image_width, pixel_index // image_width), (red, green, blue))
        pixel_index += 1
    
    # Save the image
    image.save('encoded_image.png')
    print("Image saved with encoded file content.")

# Replace this with the path to your TXT file
txt_file_path = 'test.txt'

encode_file_to_image(txt_file_path)
