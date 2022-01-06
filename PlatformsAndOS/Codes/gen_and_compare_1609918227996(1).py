from Crypto.Hash import SHA256


# here we will define a function to generate the hashes for us so that we dont have to repeat again and again
def generate_sha256_hash(text):
    h = SHA256.new()
    h.update(f"{text}".encode("utf-8"))
    return h.hexdigest()


print("1. Generate a hash")
print("2. Check login")
print("3. Exit Program")

while True:
    user_choice = input("Choose a option: ")

    if user_choice == "1":
        user_input_text = input("Enter your password: ")
        user_text_hash = generate_sha256_hash(user_input_text)
        print(f"The SHA256 hash of your password is: {user_text_hash}")
    elif user_choice == "2":
        user_input_password_1 = input("Enter Password: ")

        user_pwd1_hash = generate_sha256_hash(user_input_password_1)


        if user_pwd1_hash == user_text_hash:
            print("congratulation! You logged In! :)")
        else:
            print("Incorrect Password!")
    elif user_choice == "3":
        print("Quitting The Program....")
        break
    else:
        print("Please Choose a correct option")
