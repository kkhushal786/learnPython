content = input("Enter text to write to the file:")

with open("output.txt", "w") as file:
    file.write(content+'\n')

print("Data successfully written to output.txt.")

with open("output.txt", "a") as file:
    file.write(input("Enter additional text to append:"))

print("Data successfully appended.")
print("Final content of output.txt:")
with open("output.txt", "rt") as file:
    for line in file:
        print(line.strip())