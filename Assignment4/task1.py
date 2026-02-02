from pathlib import Path

file_path = Path(__file__).parent / "sample.txt"
print(file_path)
try:
    with open(file_path, "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: sample.txt file does not exist.")
