import itertools
from sys import argv


if len(argv) == 3:
    with open("backery.csv", 'r', encoding='utf-8') as f:
        for string in itertools.islice(f, int(argv[1])-1, int(argv[2])):
            print(string.split(":")[1].rstrip())
elif len(argv) == 2 and argv[1].replace(",", "").isdigit():
    with open("backery.csv", 'r+', encoding='utf-8') as f:
        get_last_index = f.readlines()[-1].split(":")[0].rstrip()
        f.write(f'{int(get_last_index)+1}:{str(argv[1])}\n')
elif len(argv) == 1:
    with open("backery.csv", 'r', encoding='utf-8') as f:
        for i in f:
            print(i.split(":")[1].rstrip())
