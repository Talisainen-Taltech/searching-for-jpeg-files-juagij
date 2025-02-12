import os

for i in range(10, 200):
    filename = "file%d" % i
    f = open('random_files/' + filename, 'rb').read(2)
    if f == (b'\xff\x8d'):
        os.rename('random_files/' + filename, 'random_files/' + filename + ".jpg")
    else:
        os.remove('random_files/' + filename)
