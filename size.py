import os

extensions = []

for subdir, dirs, files in os.walk("."):
	for file in files:
		if (os.path.getsize(subdir + os.sep + file)/1000000.0  >= 100.0) and "." in file :
			extensions.append(os.path.splitext(file)[1])

print (set(extensions))
