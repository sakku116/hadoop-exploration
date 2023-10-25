
import sys

args = sys.argv
if len(args) < 2:
    print("please provide filepath as argument")
    sys.exit(1)

file_path = args[1]
result_lines = []
with open(file_path, "r") as data_file:
    lines = data_file.readlines()
    for line in lines:
        line = line.strip()
        (userID, movieID, rating, timestamp) = line.split("\t")

        result_lines.append(f"{rating} 1\n")

with open("./outputs/mapper.data", "w") as f:
    f.writelines(result_lines)


