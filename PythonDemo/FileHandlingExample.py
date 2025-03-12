
import os
import FunctionsExamples as fe
# read the file
"""
data=open("C:\\Users\\JAYA VYAWHARE\\Documents\\PythonFiles\\demoText.txt","r")
#print(data.read())
#print(data.read(18))
#print(data.readline())

try:
    data=open("C:\\Users\\JAYA VYAWHARE\\Documents\\PythonFiles\\demoText.txt","r")

    for a in data:
       print(a)
except:

     print("file does not exist executing next line code")

finally:
     data.close()

# write the data into file

filewrte=open("C:\\Users\\JAYA VYAWHARE\\Documents\\PythonFiles\\demoText.txt","w")

filewrte.write("Automation****************************Automation")
filewrte.close()

fileread=open("C:\\Users\\JAYA VYAWHARE\\Documents\\PythonFiles\\demoText.txt","r")
print(fileread.read())


# file creation
file=open("C:\\Users\\JAYA VYAWHARE\\Documents\\PythonFiles\\newfileText12.txt","x")
file.write("new file created ***********")
file.close()


# delete the existing file

if os.path.exists("C:\\Users\\JAYA VYAWHARE\\Documents\\PythonFiles\\newfileText12.txt"):
      os.remove("C:\\Users\\JAYA VYAWHARE\\Documents\\PythonFiles\\newfileText12.txt")
else:
    print("file does not exist ")
"""
# deleing the folder
#os.rmdir("C:\\Users\\JAYA VYAWHARE\\Documents\\PythonFiles")

