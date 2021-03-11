res_tup = []
spam_dict = {}
line_count = 0
with open('nginx_log.txt', 'r', encoding='utf-8') as f:
    for nxt in f:
        buf_list = nxt.replace('"', "").split(" ")
        if buf_list[0] not in spam_dict:
            spam_dict.update({buf_list[0]: 1})
        else:
            for i in spam_dict:
                spam_dict[i] += 1
        if "GET" in buf_list:
            method_str = buf_list[buf_list.index("GET")]
            url_str = buf_list[buf_list.index("GET")+1]
        line_count += 1
        res_tup.append((buf_list[0], method_str, url_str))
print(f"Start Values: {line_count}\nSuccessfully: {len(res_tup)}\nSpammer is: {max(spam_dict)}")
print(res_tup[100])
