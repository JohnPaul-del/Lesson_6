

def users_hobbies(names, hobbies, result_f):
    """

    :param names: Input file with names
    :param hobbies: input file with hobbies
    :param result_f: Output file with pares of name and hobby
    :return: File
    """
# *######################### VAR WITHOUT DICT ############################
    with open(names, 'r', encoding='utf-8') as f_names:
        with open(hobbies, 'r', encoding='utf-8') as f_hobby:
            with open(result_f, 'w') as f_res:
                for buf_names in f_names:
                    f_res.write(f'{buf_names.replace(",", " ").rstrip()}: {f_hobby.readline().rstrip()}\n')

# ######################### END VAR WITHOUT DICT #########################


# ############################ VAR WITH DICT #############################
#    res_tup = {}
#    with open(names, 'r', encoding='utf-8') as f_names:
#        with open(hobbies, 'r', encoding='utf-8') as f_hobby:
#            for buf_names in f_names:
#                res_tup.update({buf_names.replace(',', ' ').rstrip(): f_hobby.readline().rstrip()})
#    with open(result_f, 'w') as f_res:
#        for key, value in res_tup.items():
#            f_res.write('{}: {}\n'.format(key, value))
# ########################## END VAR WITH DICT #############№#############

if __name__ == "__main__":
    bf_names = input("Names: ")
    bf_hobbies = input("Hobbies: ")
    bf_result_f = input("Save to: ")
    users_hobbies(bf_names, bf_hobbies, bf_result_f)
