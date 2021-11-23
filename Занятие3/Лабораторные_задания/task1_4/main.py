INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    with open(INPUT_FILE,"r") as file_1:# TODO перезаписать содержимое одного файла в другой
        with open(OUTPUT_FILE,"w") as file_2:
            for line in map(str.upper, file_1):
               file_2.write(line)

if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")


