def task():
    list_words = [ "Два", "Три","четыре"]

    filename = "output.txt"
    with open(filename, "w", encoding="utf-8") as f:
        for word in list_words:
            f.write(word + "\n") # TODO с помощью метода write запишите построчно содержимое списка

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            print(line)


if __name__ == "__main__":
    task()
