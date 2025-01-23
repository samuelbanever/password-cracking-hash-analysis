import hashlib
import bcrypt 

# plaintext words to hash
passwords = ["password123", "helloWorld", "letmein","supersecure"]

# generate MD5 and SHA1 hashes (hashlib)
with open("hashes_md5.txt", "w") as md5_file, open("hashes_sha1.txt", "w") as sha1_file:
    for pwd in passwords:
        md5_hash = hashlib.md5(pwd.encode()).hexdigest()
        sha1_hash = hashlib.sha1(pwd.encode()).hexdigest()

        md5_file.write(f"{md5_hash}\n")
        sha1_file.write(f"{sha1_hash}\n")

# generate bcrypt hashes (bcrypt)
with open("hashes_bcrypt.txt", "w") as bcrypt_file:
    for pwd in passwords:
        salt = bcrypt.gensalt() # auto generate random salt
        bcrypt_hash = bcrypt.hashpw(pwd.encode(),salt)
        bcrypt_file.write(f"{bcrypt_hash.decode()}\n")

