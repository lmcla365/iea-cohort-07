# Instructor solution

# GOAL: Given a file, reverse the lines in the file and write
# the output into a new file
filename = "../poem.txt"
with open(filename) as f:
    lines = f.readlines()
lines.reverse()
with open(filename + ".reversed", "w") as f:
    f.writelines(lines)
