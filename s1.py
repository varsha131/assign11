Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def file_read(fname):
    from itertools import islice
    with open(fname,"w") as myfile:
        myfile.write("python exercises\n")
        myfile.write("java exercises")
    txt=open(fname)
    print(txt.read())
file_read('abc.txt')
python exercises
java exercises