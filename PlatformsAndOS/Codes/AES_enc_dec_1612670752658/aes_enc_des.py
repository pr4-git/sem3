from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
import binascii

key = get_random_bytes(16) # Use a stored / generated key
buffer_size = 65536 # 64KB
print('Please select option:\n1. Encryption\n2. Decryption\n3. Exit')

while True:
    user_choice = input("Choose a option: ")
    if user_choice == "1":
        #=== Encrypt ===#
        file_to_encrypt = input('Enter the file name with extension: ')
        key = get_random_bytes(16)  # Use a stored / generated key
        prtKey = key.hex()
        print(f'Your Key is: {prtKey}')
        # Open the input and output files
        input_file = open(file_to_encrypt, 'rb')
        output_file = open(file_to_encrypt + '.encrypted', 'wb')

        # Create the cipher object and encrypt the data
        cipher_encrypt = AES.new(key, AES.MODE_OFB)

        # Initially write the iv to the output file
        output_file.write(cipher_encrypt.iv)

        # Keep reading the file into the buffer, encrypting then writing to the new file
        buffer = input_file.read(buffer_size)
        while len(buffer) > 0:
            ciphered_bytes = cipher_encrypt.encrypt(buffer)
            output_file.write(ciphered_bytes)
            buffer = input_file.read(buffer_size)

        # Close the input and output files
        input_file.close()
        output_file.close()

    elif user_choice == "2":
        #=== Decrypt ===#

        # Open the input and output files
        newKey = input('Please enter the key: ')
        newKEY = binascii.unhexlify(newKey)
        file_to_decrypt = input('Enter the file name with extension to decrypt: ')
        input_file = open(file_to_decrypt, 'rb')
        output_file = open(file_to_decrypt + '.decrypted', 'wb')

        # Read in the iv
        iv = input_file.read(16)

        # Create the cipher object and encrypt the data
        cipher_encrypt = AES.new(newKEY, AES.MODE_OFB, iv=iv)

        # Keep reading the file into the buffer, decrypting then writing to the new file
        buffer = input_file.read(buffer_size)
        while len(buffer) > 0:
            decrypted_bytes = cipher_encrypt.decrypt(buffer)
            output_file.write(decrypted_bytes)
            buffer = input_file.read(buffer_size)

        # Close the input and output files
        input_file.close()
        output_file.close()

    elif user_choice == "3":
        print("Quitting The Program....")
        break

    else:
        print("Please Choose a correct option")
