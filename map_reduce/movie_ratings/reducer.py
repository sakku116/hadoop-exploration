
import sys

args = sys.argv
if len(args) < 2:
    print("please provide filepath as argument")
    sys.exit(1)

file_path = args[1]
result_map = {}
with open(file_path, "r") as data_file:
    lines = data_file.readlines()

    for line in lines:
        line = line.strip()

        (rating, count) = line.split(" ")
        count = int(count)

        if rating not in result_map:
            result_map[rating] = count
        else:
            result_map[rating] += count

with open("./outputs/reducer.data", "w") as f:
    result_lines = []
    for key, value in result_map.items():
        result_lines.append(f"{key} {value}\n")
    f.writelines(result_lines)


