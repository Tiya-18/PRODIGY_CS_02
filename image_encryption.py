from PIL import Image
import numpy as np
import random

def encrypt_image(image_path, output_path, key, constant=10):
    # Load the image
    img = Image.open(image_path)
    img = img.convert('RGB')
    data = np.array(img)

    # Encrypt the image
    np.random.seed(key)
    indices = np.arange(data.size // 3)
    np.random.shuffle(indices)
    shuffled_data = data.reshape(-1, 3)[indices].reshape(data.shape)
    encrypted_data = (shuffled_data + constant) % 256

    # Save the encrypted image
    encrypted_img = Image.fromarray(encrypted_data.astype(np.uint8))
    encrypted_img.save(output_path)

def decrypt_image(encrypted_path, output_path, key, constant=10):
    # Load the encrypted image
    img = Image.open(encrypted_path)
    img = img.convert('RGB')
    data = np.array(img)

    # Decrypt the image
    decrypted_data = (data - constant) % 256
    np.random.seed(key)
    indices = np.arange(decrypted_data.size // 3)
    np.random.shuffle(indices)
    reverse_indices = np.argsort(indices)
    original_data = decrypted_data.reshape(-1, 3)[reverse_indices].reshape(data.shape)

    # Save the decrypted image
    decrypted_img = Image.fromarray(original_data.astype(np.uint8))
    decrypted_img.save(output_path)

def main():
    choice = input("Do you want to encrypt or decrypt an image? (e/d): ").strip().lower()
    if choice not in ['e', 'd']:
        print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")
        return
    
    image_path = input("Enter the path to the image: ").strip()
    output_path = input("Enter the output path for the image: ").strip()
    key = int(input("Enter the key (integer): ").strip())
    constant = int(input("Enter the constant value (integer, default is 10): ").strip() or 10)
    
    if choice == 'e':
        encrypt_image(image_path, output_path, key, constant)
        print(f"Image encrypted and saved to {output_path}")
    elif choice == 'd':
        decrypt_image(image_path, output_path, key, constant)
        print(f"Image decrypted and saved to {output_path}")

if __name__ == "__main__":
    main()
