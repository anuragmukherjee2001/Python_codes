import os

# print(dir(os))

# print(os.getcwd())   // To see the current directory

# os.chdir("D://coursera")      // To changew the current directory

# print(os.getcwd())        // To see the current directory

# print(os.listdir())         # will list all files present in the working directory 

# print(os.listdir("D://"))       // will list all files present in the mentioned directory in the form of a list

# os.mkdir("This")            // creates a folder in the working directory with the name passed as the parameter

# os.makedirs("This/that")        // makes multiple folders taking the first as the parent folder

# os.rename("leapYear.py","leap_year.py")         // renames any file, 1st parameter is the original name followed by the renamed name

# print(os.environ.get('Path'))           // used to get the environment variables present in path

# os.path.join("D://", "list.py")             //helps to join paths

# print(os.path.join("D://", "list.py"))      // printing the joining path

# print(os.path.exists("D://"))             // helps to know us wheather a path exists or not

# print(os.path.exists("C://"))

# print(os.path.exists("D://anurag"))           //false

# print(os.path.isdir("D://coursera"))            //returns true or false whether coursera is a directory or not

# print(os.path.isfile("D://coursera"))           //returns true or false whether coursera is a file or not

