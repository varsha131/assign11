Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def file_size(fname):
    import os
    startinfo=os.start(fname)
    return startinfo.st_size
print("file size in bytes of a plain file:", file_size("test.txt"))