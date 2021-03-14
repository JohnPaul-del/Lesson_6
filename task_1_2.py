import collections

with open('nginx_log.txt', 'r', encoding='utf-8') as f:
    result = ((line.split()[0], line.split()[5][1:], line.split()[6]) for line in f)
    for i in result:
        print(i)
    spam_dict = collections.Counter()
    f.seek(0)
    for spammer in f:
        spammer = spammer.split()[0]
        spam_dict[spammer] += 1
    spam_ip, count = spam_dict.most_common(1)[0][0], spam_dict.most_common(1)[0][1]
    print(f"Spammer is {spam_ip}. Find {count} times")
