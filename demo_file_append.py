
"""
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
"""

"""
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())
"""

#f = open("site.html", "x")

f = open("mySite.html", "w")

f = open("mySite.html", "a")
f.write("Stay tuned for our amazing summer sale!")
f.close()

f = open("mySite.html", "r")
print(f.read())
