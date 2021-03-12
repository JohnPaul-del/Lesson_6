import itertools

with open("backery.csv", 'r+', encoding='utf-8') as f:
    buf_string = f.readlines()[0].split(":")[1].rstrip()
    f.write(buf_string.replace(f.readlines()[0].split(":")[1].rstrip(), "122112"))





### Append Function ###
#with open("backery.csv", 'r', encoding='utf-8') as f:
#    for string in itertools.islice(f, num_1, num_2+1):
#        print(string.split(":")[1].rstrip())

### Append Function ###
#with open("backery.csv", 'r+', encoding='utf-8') as f:
#    get_last_index = f.readlines()[-1].split(":")[0].rstrip()
#    f.write(f'{int(get_last_index)+1}:9876,12\n')

### Read all Function ###
#def read(argv):
#    with open("backery.csv", 'r', encoding='utf-8') as f:
#        for i in f:
#            print(i.split(":")[1].rstrip())
