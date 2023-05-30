### ANYONE WELCOME TO MAKE A BETTER README ###


I created a simple cipher script just to test how to do it,
I know for sure that the cipher works with txt files, haven't tested with other files.

In simple explanaition, the code will get the contents of a file, and using a key, it will change the binary values.

The code can bring back to normal from ciphered text. 

Usage:

python cypher.py [OPTIONAL FILE-TO-CIPHER PATH]


In Chat-GPT explanation:


File Cipher and Decipher
This Python script allows you to cipher and decipher files using a key cipher. It provides a simple command-line interface for performing the operations.

Prerequisites
Python 3.x
Usage
Run the script using the following command:

Copy code
python file_cipher.py
You will be presented with a menu to choose an action:

Option 1: Cipher a file
Option 2: Decipher a file
Option 3: Exit
Select the desired option by entering the corresponding number.

If you choose option 1 (Cipher a file):

You will be prompted to enter the path to the file you want to cipher. If no command-line argument is provided, you can enter the path interactively.
Next, enter the key cipher. This key is used to cipher the file and should be kept secret.
The script will cipher the file using the key cipher and generate a new file with the ciphered data. The new file will have "-cip" appended to its name.
If you choose option 2 (Decipher a file):

You will be prompted to enter the path to the file you want to decipher. If no command-line argument is provided, you can enter the path interactively.
Next, enter the key cipher. This should be the same key that was used to cipher the file.
The script will decipher the file using the key cipher and generate a new file with the deciphered data. The new file will have "de" prepended to its name.
After the file is ciphered or deciphered, the script will display the path to the new file.

Important Notes
Make sure to remember the key cipher used for encryption. Without the correct key, it will not be possible to decipher the file.
The script uses base64 encoding and binary operations to perform the ciphering and deciphering. The resulting files may not be readable in their raw form.
It is recommended to keep a backup of the original file before ciphering or deciphering it.
