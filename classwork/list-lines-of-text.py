# Lines of text
from os import system

# list of str
# one-dimension list / array / vector
text_lines = [
    "Python is a high-level, interpreted, general-purpose programming language.",
    "Its design philosophy emphasizes code readability with the use of significant indentation.",
    "Python is dynamically-typed and garbage-collected."
]
system("cls")

# 1. len(..list..) --> 3
# 2. range(start=0, end=3, step=1) -> [0,1,2]
# 3. for i in [0,1,2], i = 0, execute block, i = 1, execute block, i = 2, execute block

# HW1: draw the diagram
# HW2: write code which adds 2 more lines from keyboard

for n in range(2):
    text_lines.append(input("Add elements in list: "))

print()

# indexed list iteration
for i in range(len(text_lines)):
    print(i, text_lines[i])

# OR

# for line in text_lines:
#     print(line)

print()