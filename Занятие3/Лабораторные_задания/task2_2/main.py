import json


def task(input_filename: str, output_filename: str) -> None:
    with open(input_filename,"r") as file_1:
        js_file_1 = json.load(file_1)
        # TODO считать содержимое json файл input.json

    with open(output_file,"w") as file_2:
        js_file_2 = json.dump(js_file_1,file_2,indent=4)# TODO записать содержимое в json файл output.json с отступами


if __name__ == "__main__":
    input_file = "input.json"
    output_file = "output.json"

    task(input_file, output_file)

    with open(output_file) as output_f:
        for line in output_f:
            print(line, end="")
