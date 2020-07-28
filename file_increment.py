import os

i = 0
while os.path.exists("test%s.jpg" % i):
    i += 1

fh = open("test%s.jpg" % i, "w")