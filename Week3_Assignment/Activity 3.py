data = open (r"C:\Users\indus\Downloads\Junk.txt", "r")
lines=data.readlines()
for line in data:
    print(line[0:-1])
data.close()