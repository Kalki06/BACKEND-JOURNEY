with open ("notes.txt", "w") as file:
    file.write("hello world \n")
    file.write("I am manjeet\n")
    file.write("I am learning backend engineering\n")

with open("notes.txt", "a") as file:
    file.write("I am building the world class coding skills\n")
    file.write("I am the best coder in the world")


with open ("notes.txt", "r") as file:
    content = file.read()
    print(content)

with open("notes.txt", "r") as file:
    line_count = 0

    for line in file:
        line_count += 1

print("Total lines:", line_count)