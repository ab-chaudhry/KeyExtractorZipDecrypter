import pyzipper

def main():
	inFile = 'C:\\Users\\user1\\Desktop\\ProductSubmission\\attempt3.zip'
	outDir = 'C:\\Users\\user1\\Desktop\\ProductSubmission\\\keyExtractor\\extracts'
	userInput = input("Enter password for the ZIP file: ")
	pwd = bytes(userInput, 'utf-8')
	print("pwd: ", pwd)
	open('keys.txt', 'w').close() #Clears the contents of the text file containing keys
	with pyzipper.AESZipFile(inFile) as fileIn:
		fileIn.setpassword(pwd)
		list_files = fileIn.namelist()
		fileIn.extractall(outDir)
		
if __name__ == '__main__': main()
