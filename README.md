# KeyExtractorZipDecrypter
KeyExtractor and ZipDecrypter tools created using 'PyZipper' by danifus (https://github.com/danifus/pyzipper)

KeyExtractor Program
---------------------
KeyExtractor is a Python 3 program which uses PyZipper as a module. It takes password of an encrypted Zip file as input from the user and calculates and prints the AES keys for the files being extracted from the encrypted Zip file. Note that the encrypted Zip file must be hard-coded in the program Python file 'keyExtractor.py'.

KeyExtractor is run from command-prompt and prompts user to enter the password of the Zip file. Once password is entered, the program lists information of files being decrypted and extracted from the Zip file, such as filename and file size, followed by the key that was used to decrypt them. 
 
The program also exports the keys into a text file called ‘keys.txt’, which is helpful as the user can copy keys from the text file if he accidentally closes the command-prompt without having to re-run the program.

ZipDecrypter Program
---------------------
ZipDecrypter imports PyZipper as a module and uses AES keys input by the user to decrypt files from a password-protected Zip file.

When Python file ‘zipDecrypter.py’ is run from command prompt, ZipDecrypter shows the files contained in the Zip file that is hard-coded in the program. User is then prompted to select one of three files contained in the Zip file to decrypt.

Once the file is selected, the program confirms the file selection and states the name of the selected file. Then the program prompts the user to enter the AES key in hexadecimal format without spaces.

Once the key is entered, the program decrypts the file and displays a message saying that the file has been decrypted and extracted to the directory and states the path of the directory containing the decrypted file.
