from pathlib import Path

file_path = Path(__file__).parent / "sample.txt"
print(file_path)
try:
    with open(file_path, "r") as file:
        print("Line 1:",file.readline())
        print("Line 2:",file.readline())
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
