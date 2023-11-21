#read a text file and display into the console

def read_and_display(file_name):
       file1 = open(file_name, 'r') 
       content = file1.read()
       print(content)
       file1.close()

file_name = input("Enter the name of the textfile:")
read_and_display(file_name)
