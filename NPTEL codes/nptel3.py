# with open("f.txt","w") as myfile:
#     myfile.write("0110");
# myfile.close()

# with open("f.txt","r") as myfile:
#     l = list(myfile.read());
#     suml = 0
#     for each in l:
#         suml = suml + int(each)
#     print(suml)
# myfile.close()        

with open("fi.txt","w")as f:
    f.write("Hey! I am writing");
f.close()
with open("fi.txt","w")as f:
    f.write("hey i am writing the second line");
f.close()
with open("fi.txt","r")as f:
    print(f.read())
f.close()            