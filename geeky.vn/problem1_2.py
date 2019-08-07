import sys
import time


def convert_input(s_input):
    adj_input = s_input.splitlines()
    encrypted_text = adj_input[0].split(' ')
    dictionary = adj_input[1]
    pre_table = adj_input[2 :]
    return encrypted_text, dictionary, pre_table

def split_pre_table(pre_table):
    simple_pre_table = []
    complex_pre_table = []
    for substitution in pre_table:
        if len(substitution) == 3:
            simple_pre_table.append(substitution)
        else:
            complex_pre_table.append(substitution)
    return simple_pre_table, complex_pre_table

def create_table_list(pre_table, simple_pre_table, encrypted_text, dictionary):
    result = encrypted_text[:]
    compare_list = encrypted_text[:]
    start_time = time.time()

    simple_string_list = create_simple_string_list(pre_table)
    print("--- %s seconds ---" % (time.time() - start_time))
    pair_complex_list = create_pair_complex_list(simple_string_list)
    print("--- %s seconds ---" % (time.time() - start_time))
    count = 0
    while len(compare_list) > 0:
        for simple_pair_list in pair_complex_list:
            tmpTable = create_simple_table_case(simple_pair_list \
                + simple_pre_table)
            for ind in range(len(compare_list) - 1, -1, -1):
                word = compare_list[ind]
                decoded_word = word.translate(tmpTable)
                if decoded_word in dictionary:
                    result[ind] = decoded_word
                    del(compare_list[ind])
    print("--- %s seconds ---" % (time.time() - start_time))
    return ' '.join(result)

def create_pair_complex_list(simple_string_list):
    result = []
    for string in simple_string_list:
        result.append(string.split('.'))
    return result

def create_simple_string_list(pre_table):
    result = []
    if len(pre_table) == 1:
        return produce_1len_pair(pre_table[0])
    else:
        for ind in range(0, len(pre_table)):
            new_addition_pair = produce_1len_pair(pre_table[ind])
            recursive_result = create_simple_string_list(pre_table[ind + 1:])
            for simple_pair in new_addition_pair:
                for recursive_pairs in recursive_result:
                    result.append(simple_pair + '.' + recursive_pairs)
    return result

def produce_1len_pair(substitution):
    '''
    substitution: string
    '''
    result = []
    base = substitution[0 : 2]
    for char in substitution[2::2]:
        result.append(base + char)
    return result

def create_simple_table_case(simple_pair_list):
    base_dict = {}
    for substitution in simple_pair_list:
        base_dict[ord(substitution[0])] = substitution[2]
    return base_dict

f = lambda x: [[y for j, y in enumerate(set(x)) if (i >> j) & 1] for i in range(2**len(set(x)))]

f = lambda l: reduce(lambda z, x: z + [y + [x] for y in z], l, [[]])


# def decode_1_word(word, tables_list, dictionary):
#     for table in tables_list:
#         decoded_word = word.translate(table)
#         if decoded_word in dictionary:
#             return decoded_word

# def get_decode_text(encrypted_text, tables_list, dictionary):
#     result = []
#     for word in encrypted_text:
#         result.append(decode_1_word(word, tables_list, dictionary))
#     return ' '.join(result)

if __name__ == "__main__":
    # s_input = sys.stdin.read()
    # s_input = str(s_input)
    s_input = '''pgfqp td c bt bh dhschddg
rage am holy an fairy engine tale engineer i le me my trust yes thunder truth oh april goddess beach please godzilla neo matrix mogu al capone you know tired of this sheet
b a f
c i 
d e k d s w e r c x
f k d s w e u
g r k d s w e r
s g k d s w e r
h k d s w e n 
p t k d s w e r
q s
t m'''
    encrypted_text, dictionary, pre_table = convert_input(s_input)
    simple_pre_table, complex_pre_table = split_pre_table(pre_table)
    tables_list = create_table_list(complex_pre_table, \
        simple_pre_table, encrypted_text, dictionary)
    print(tables_list)