from PIL import Image
import numpy as np

def encrypt_image(image_path, key, output_path):
    image = Image.open(image_path)
    image_data = np.array(image)
    encrypted_data = image_data ^ key 
    encrypted_image = Image.fromarray(encrypted_data)
    encrypted_image.save(output_path)
    print("Encryption Done. Saved as:", output_path)
def decrypt_image(encrypted_path, key, output_path):
    encrypted_image = Image.open(encrypted_path)
    encrypted_data = np.array(encrypted_image)
    decrypted_data = encrypted_data ^ key 
    decrypted_image = Image.fromarray(decrypted_data)
    decrypted_image.save(output_path)
    print("Decryption Done. Saved as:", output_path)

if __name__ == "__main__":
    option = input("Enter 'e' to encrypt or 'd' to decrypt: ")
    image_path = input("Enter image file path: ")
    output_path = input("Enter output file path: ")
    key = int(input("Enter encryption key (0-255): "))
    
    if option == 'e':
        encrypt_image(image_path, key, output_path)
    elif option == 'd':
        decrypt_image(image_path, key, output_path)
    else:
        print("Invalid option!")
