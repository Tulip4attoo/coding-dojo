import sys

def convert_input(s_input):
    adj_input = s_input.splitlines()
    length = int(adj_input[0])
    str_array = adj_input[4].replace(' ', '')[1]
    for row in range(1, 4):
        str_array += adj_input[row].replace(' ', '')
    return length, str_array

def produce_code(length, str_array):
    result = []
    if length == 1:
        return get_len1_code(str_array)
    else:
        for ind in range(0, 10):
            if str_array[ind] != '0':
                new_str_array = str_array[0 : ind] + str(int(str_array[ind]) - 1) + str_array[ind + 1 : ]
                recursive_result = produce_code(length - 1, new_str_array)
                for sequence in recursive_result:
                    result.append(str(ind) + sequence)
        return result

def get_len1_code(str_array):
    result = []
    for ind in range(0, 10):
        if str_array[ind] != '0':
            result.append(str(ind))
    return result

def convert_output(length, output_list):
    result = []
    for output in output_list:
        result.append(output.replace('', ' ')[1: length * 2])
    return '\n'.join(result)

if __name__ == "__main__":
    # with open('input.txt', 'r') as myfile:
    #     s_input = myfile.read()
    s_input = sys.stdin.read()
    s_input = str(s_input)
    length, str_array = convert_input(s_input)
    s_output = produce_code(length, str_array)
    result = convert_output(length, s_output)
    # output_file = open("output.txt", "w")
    # output_file.write(result)
    # output_file.close()
    print(result)
