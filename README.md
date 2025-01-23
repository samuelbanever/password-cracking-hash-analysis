
Password Cracking and Hash Analysis

I learned about hashing in my second year of college, and this project of mine shows how different password hashing algorithms (SHA1&MD5 vs bcrypt) can be generated and tested against dictionary based password cracker tools such as John the Ripper. This was done in a controlled and ethical environment. Comparing the speed and difficulty of cracking each hash type we can understand why algorithms that are strong like bcrypt are preferred over the faster, but weaker, algorithms like MD5 and SHA1. 


Overview
Objective: Generate various hashes (MD5, SHA1, bcrypt) for sample passwords, then attempt to crack them using dictionary-based attacks.
Goal: Illustrate how “fast” hashes (like MD5 or SHA1) are more easily cracked, whereas “slow” hashes (like bcrypt) provide better security.




Tools & Environment
VirtualBox: Used to run a Kali Linux virtual machine (VM).
Kali Linux ISO: Security-focused distro with John the Ripper pre-installed.
Python (3.x): For generating MD5, SHA1, and bcrypt hashes.
Apache utilities (optional): For quickly generating bcrypt hashes in Linux.
John the Ripper (or Hashcat): Cracking tools used to test the hash difficulty.
RockYou Wordlist: A popular password dictionary included with Kali (located at /usr/share/wordlists/rockyou.txt.gz).



Hash Generation (Python & CLI)
Python Script

Created a generate_hashes.py file in VSCode, leveraging:
hashlib for MD5 (128-bit) and SHA1 (160-bit).
bcrypt module for salted bcrypt hashes (slower, more secure).
Script takes a few plaintext passwords (e.g., "password123", "letmein") and outputs three .txt files:
hashes_md5.txt
hashes_sha1.txt
hashes_bcrypt.txt
Each file contains one hash per line.
Linux Command Line

Verified MD5 and SHA1 generation using:

-bash-
echo -n "password123" | md5sum
echo -n "password123" | sha1sum

Installed Apache utilities (apt-get install apache2-utils) to generate bcrypt:

-bash-
htpasswd -nbB user password123

Saved the outputs to .txt files for later cracking.


Cracking Hashes with John the Ripper
Setup

Decompressed the RockYou wordlist:

-bash-
gunzip /usr/share/wordlists/rockyou.txt.gz

Confirmed the project folder was accessible in Kali (handled a small hiccup setting up a shared folder from the Windows host).
Running John the Ripper

Command for SHA1:

-bash-
john --wordlist=/usr/share/wordlists/rockyou.txt hashes_sha1.txt
john --show hashes_sha1.txt

Achieved a 50% crack rate on the SHA1 sample (2 out of 4 hashes).
bcrypt Cracking

Attempted the same dictionary attack with bcrypt hashes:

-bash-
john --wordlist=/usr/share/wordlists/rockyou.txt hashes_bcrypt.txt

John initially estimated a 3-week runtime because bcrypt is intentionally slow.
After letting it run for about 65 minutes, it managed to crack 2 passwords.





Results & Observations
MD5 & SHA1

Extremely fast to generate and also much faster to crack.
Typically cracked within seconds or minutes using a large wordlist.
Emphasizes why MD5 and SHA1 are not recommended for password storage.
bcrypt

Designed with key-stretching, making each hash computation slower.
Salts are automatically generated, preventing the use of precomputed rainbow tables.
Cracking can take significantly longer, especially with higher cost factors.
Even on a moderate GPU, expect a longer ETA, demonstrating enhanced security.
Dictionary Attacks

All attempts here were dictionary-based, matching known wordlists to hashed values.
If the password is not in the wordlist, it will likely remain uncracked.
GPU & System Limitations

Running in a VM or on limited hardware further increases the time to crack bcrypt.
This slowness illustrates that bcrypt’s design is inherently more robust.



Conclusion
bcrypt emerges as a much stronger hashing algorithm compared to MD5 and SHA1. Its built-in salting and slow verification process drastically increase the difficulty of cracking.
MD5/SHA1 are much less secure. They can often be cracked quickly with common wordlists.
For secure password storage, modern applications should use bcrypt (or similar algorithms like PBKDF2, Argon2, or scrypt), enforce password complexity, and educate users about password best practices.




DISCLAIMER
This project was performed only to test passwords for educational purposes. Attempting to crack any password without explicit permission is unethical as well as illegal, as is storing or using cracked passwords for access.

The methods shown here were used to improve Kali Linux and Python skills, improve security awareness, and demonstrate vulnerabilities. Not to exploit them

A few commands were found via Reddit, and Discord servers.

Thanks for checkin out my Password Cracking and Hash Analysis project. I learned a lot and feel free to reach out. 