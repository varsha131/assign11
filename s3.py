Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> file=open("gfg.txt","r")
count=0
content=file.read()
colist=content.split("\n")
for i in colist:
        if i:
            counter+=1
print("this is number of lines in the file")
print(count)