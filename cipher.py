import sys
import getpass
import base64


def load_file(args):
    """
    Prompts the user to input a file path or retrieves it from command-line arguments.

    Args:
        args (list): Command-line arguments.

    Returns:
        str: The file path.
    """
    if len(args) <= 1:
        file_path = input("What is the path to the file:\n")
    else:
        file_path = args[1]
    return file_path


def get_file_contents(file_path):
    """
    Reads the contents of a file and returns them as a string.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The contents of the file.
    """
    try:
        with open(file_path, "r", encoding='utf-8') as file:
            file_data = file.read()
        str_file = str(file_data)
        return str_file
    except IOError as e:
        print(f"Error opening file: {e}")


def get_cipher_bin(cip):
    """
    Converts a base64-encoded string into a list of binary chunks.

    Args:
        cip (str): The base64-encoded string.

    Returns:
        list: The binary chunks.
    """
    decoded_data = base64.b64decode(cip.encode("ascii")).decode("ascii").encode("ascii").hex()
    bin_cip = bin(int(decoded_data, 16))[2:]

    if len(bin_cip) % 8 != 0:
        bin_cip = "0" * (8 - len(bin_cip) % 8) + bin_cip

    bin_chunk = [bin_cip[i:i+8] for i in range(0, len(bin_cip), 8)]
    return bin_chunk


def bin_file(str_file):
    """
    Converts a string into a list of binary chunks.

    Args:
        str_file (str): The input string.

    Returns:
        list: The binary chunks.
    """
    file_hex = str_file.encode('utf-8').hex()
    file_bin = bin(int(file_hex, 16))[2:]

    if len(file_bin) % 8 != 0:
        file_bin = "0" * (8 - len(file_bin) % 8) + file_bin

    file_bin_chunk = [file_bin[i:i+8] for i in range(0, len(file_bin), 8)]
    return file_bin_chunk


def cipher_data(chunk, key):
    """
    Applies a bitwise XOR operation between two lists of binary chunks.

    Args:
        a (list): List of binary chunks.
        b (str): Binary string.

    Returns:
        list: The result of the XOR operation on each binary chunk.
    """
    new_chunk  = []
    for i in range(len(chunk)):
        sink = chunk[i]
        keying = key[i % len(key)]
        new_bin = ""
        for x, char in enumerate(sink):
            if keying[x] == "1":
                new_bi = "0" if char == "1" else "1"
            else:
                new_bi = char
            new_bin += new_bi
        new_chunk.append(new_bin)
    return new_chunk


def debin_data(bin_data):
    """
    Converts a list of binary chunks back to its original string representation.

    Args:
        bin_data (list): List of binary chunks.

    Returns:
        str: The original string representation.
    """
    bin_string = ''.join(bin_data)
    hex_bin = format(int(bin_string, 2), 'x')
    data = bytearray.fromhex(hex_bin).decode()
    return data


def write_new_file(file_path, data):
    """
    Writes data to a new file.

    Args:
        file_path (str): The path to the new file.
        data (str): The data to be written.

    Returns:
        None
    """
    try:
        with open(file_path, "w", encoding='ascii') as file:
            file.write(data)
    except IOError as e:
        print(f"Error opening file: {e}")


repeat = False

while True:
    if repeat:
        usr = input("Please choose a valid option\n")  # Prompt user for a valid option if repeat is True
    else:
        usr = input(
            "What do you want to do?\n1 - Cipher a file\n2 - Decipher a file\n3 - Exit\n")  # Prompt user for action choice

    if (usr != "1" and usr != "2" and usr != "3"):  # Check if the chosen option is valid
        repeat = True  # Set repeat to True to indicate an invalid option
    elif usr == "3":  # Check if the chosen option is to exit
        break  # Exit the while loop and end the program
    else:
        repeat = False  # Reset repeat to False for a valid option
        path_to_file = load_file(sys.argv)  # Load the file path
        file_in_str = get_file_contents(path_to_file)  # Get the contents of the file
        cipher = base64.b64encode(
            str(getpass.getpass("What is the key cipher?\nDo not forget this key!!\n")).encode("ascii")).decode(
            "ascii")  # Prompt user for the cipher key and encode it
        bin_key = get_cipher_bin(cipher)  # Get the binary representation of the cipher key
        file_chunk = bin_file(file_in_str)  # Convert file contents to binary chunks
        new_data_bin = cipher_data(file_chunk, bin_key)  # Apply cipher to the file data
        new_data = debin_data(new_data_bin)  # Convert the ciphered data back to its original form

        if usr == "1":  # Check if the chosen option is to cipher the file
            path_to_new_file = path_to_file[:-4] + "-cip" + path_to_file[-4:]  # Generate the path for the new ciphered file
        else:  # The chosen option is to decipher the file
            path_to_new_file = path_to_file[:-7] + "de" + path_to_file[-7:]  # Generate the path for the new deciphered file

        write_new_file(path_to_new_file, new_data)  # Write the ciphered or deciphered data to a new file
        print(f"File ciphered, new file in\n{path_to_new_file}")  # Print a message indicating the file operation is completed

    repeat = False  # Reset repeat to False before the next iteration of the while loop
