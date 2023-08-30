from PIL import Image

def decode_image_to_text(image_path):
    image = Image.open(image_path)
    decoded_text = ""
    
    for pixel_index in range(image.width * image.height):
        pixel = image.getpixel((pixel_index % image.width, pixel_index // image.width))
        byte_value = pixel[0]  # Use the red channel
        
        # Stop decoding when encountering a zero byte (end of text)
        if byte_value == 0:
            break
        
        decoded_text += chr(byte_value)
    
    return decoded_text

def save_text_to_file(text, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(text)
    print("Decoded text saved to", output_file_path)

# Replace this with the path to your encoded image
encoded_image_path = 'encoded_image.png'
output_text_file_path = 'decoded_text.txt'

decoded_text = decode_image_to_text(encoded_image_path)
save_text_to_file(decoded_text, output_text_file_path)
