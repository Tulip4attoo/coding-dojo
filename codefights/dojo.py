

def find_short(s):
    # your code here
    word = s.split(" ")
    lenList = map(len, word)
    return min(lenList)


def longest_consec(strarr, k):
    n = len(strarr)
    longestString = ""
    maxLen = 0
    if (n == 0) or (k > n) or (k <= 0):
        return longestString
    for ind in xrange(0, n - k + 1):
        joinString = "".join(strarr[ind : (ind + k)])
        tempLen = len(joinString)
        if tempLen > maxLen:
            maxLen = tempLen
            longestString = joinString
    return longestString

def fib(n):
  """Calculates the nth Fibonacci number"""
  m = abs(n)
  phi = ( 1 + 5 ** 0.5)/2

  if n == 0:
    return 0
    exit
  else:
    i = m / n
    k = i**((- 1) + n % 2 + 2)
    l = (phi ** m - (1 - phi) ** m) / (5 ** 0.5)
    return int(k * l)
  


def mix(s1, s2):
    # your code



def tower_builder(n_floors):
    towerList = []
    for i in xrange(1, n_floors + 1):
        towerList.append(' ' * (n_floors - i) + '*'* (2 * i - 1) + ' ' * (n_floors - i))
    return towerList


def smallest(n):
    digitList = list(str(n))
    minDigit = min(digitList)
    minNumber = 0
    indexDigit = [i for i,digit in enumerate(digitList) if digit == minDigit]
    if indexDigit[0] == 0:
        return [n, 0, 0]
    elif 1 not in indexDigit:
        del(digitList[indexDigit[0]])
        digitList.insert(0, minDigit)
        minNumber = int("".join(digitList))
        return [minNumber, indexDigit[0], 0]
    else:
        tempIndex = 0
        for i in xrange(1, len(digitList)):
            tempIndex = i - 1
            if i not in indexDigit:
                break
        digitList[0], digitList[tempIndex] = minDigit, digitList[0]
        minNumber = int("".join(digitList))
        return [minNumber, 0, tempIndex]


def NumberPacking(x):
    for 



start_time = time.time()

while b > 100:
    b = b / 52
print("--- %s seconds ---" % (time.time() - start_time))


import time
import math



def downlevel_number(number, power_value):
    power_value = base ** power
    digit = number / power_value
    number = number - digit * power_value

    return number, digit


def convert_10d_to_base(number, base):
    result = ""
    power_limit = int(math.log(number, base))
    for power in xrange(power_limit, -1, -1):
        number, digit = downlevel_number(number, base, power)
        result += str(digit)
    return result




def isTandemRepeat(inputString):
    for len_string in xrange(2, 8):
        if len(inputString) / len_string > 1:
            if inputString[0 : len_string] * (len(inputString) / len_string) == inputString:
                return True
    return False


def isCaseInsensitivePalindrome(inputString):
    lower_input = inputString.lower()
    list_str = list(lower_input)
    reversed_list_str = list(lower_input)
    reversed_list_str.reverse()
    if list_str == reversed_list_str:
        return True
    else:
        return False

def findEmailDomain(address):
    ind = address.rindex("@")
    return address[ind:]


def htmlEndTagByStartTag(startTag):
    preprocess = startTag.split(" ")[0]
    result = "</" + preprocess[1 :].replace(">", "") + ">"
    return result



def isMAC48Address(inputString):
    split_input = inputString.split("-")
    if map(len, split_input) == [2, 2, 2, 2, 2, 2]:
        try:
            int(i, 16) for i in split_input
        except:
            return False
        return True
    return False


contFrac, magic_number = [], 1 / (D ** 0.5)

for i in xrange(1,5):
    contFrac, magic_number = create_contFrac(contFrac, magic_number)
    x, y = cv_contFrac_to_Frac(contFrac)
    print(x, y)



def my_sieve(n):
    dumb_list = range(0, n)
    limit = int(n ** 0.5)
    for i in xrange(2, limit):
        if dumb_list[i]:
            dumb = (n - 1) / i - 1
            dumb_list[i + i :: i] = [0] * dumb
    return filter(None, dumb_list)

prime_list = my_sieve(10 ** 4) 





def twoPolygons(p1, p2):
    def doubleSquare(polygon):
        square = 0
        for i in range(len(polygon)):
            a = polygon[i]
            b = polygon[(i + 1) % len(polygon)]
            square += a[0] * b[1] + a[1] * b[0]
        return square

    return doubleSquare(p1) == doubleSquare(p2)





def isPangram(sentence):
    found = []
    result = True
    for i in range(26):
        found.append(False)
    for i in range(len(sentence)):
        code = ord(sentence[i])
        if ord('A') <= code and code <= ord('Z'):
            code +=  ord('a') - ord('A') 
        if ord('a') <= code and code <= ord('z'):
            found[code - ord('a')] = True

    for i in range(26):
        if not found[i]:
            result = False

    return result



def swapAdjacentBits(n):
    string = ''
    str_bin_number = convert_to_bin(n)
    string_32b = convert_to_32bit(str_bin_number)
    for i in xrange(0, 16):
        pair = string_32b[i * 2 : i * 2 + 2]
        if pair == '01':
            string += '10'
        elif pair == '10':
            string += '01'
        else:
            string += pair
    return int(string, 2)


def convert_to_32bit(bin_number):
    return '0' * (32 - len(bin_number)) + bin_number

def convert_to_bin(number):
    return bin(number)[2:]


def trapezoidalRule(l, r, p):

    def calcF(polynomial, point):
        value = 0
        power = 1
        for i in range(len(polynomial)):
            value += polynomial[i] * power
            power *= point
        return value

    result = 0

    for i in range(l, r):
        result += calcF(p, i) + calcF(p, i + 1)

    return result

def treeBottom(tree):
    nodes = []
    def treeParse(depth, l, r):
        pos = l
        value = 0
        balance = 0
        nextL = -1
        nextR = -1
        if l == r:
            return
        if len(nodes) == depth:
            nodes.append([])
        while tree[pos] != ' ':
            value = value * 10 + ord(tree[pos]) - ord('0')
            pos += 1
        nodes[depth].append(value)
        for iteration in range(2):
            balance = 1
            while balance > 0:
                if tree[pos] == '(':
                    balance += 1
                if tree[pos] == ')':
                    balance -= 1
                pos += 1
            nextR = pos - 1
            treeParse(depth + 1, nextL, nextR)

    treeParse(0, 1, len(tree) - 1)
    return nodes[len(nodes) - 1]




def easyAssignmentProblem(skills):
    return ([1, 2] if skills[0][0] + skills[1][1] > skills[0][1] + skills[1][0]
        else  )


def divisorsSuperset(superset, n):
    count = 0
    for number in xrange(2, n):
        for divisor in xrange(2, number):
            if number % divisor == 0:
                if divisor not in superset:
                    count += 1
                    break
    return count


def swapAdjacentBits(n):
    str_32b = '0' * (34 - len(bin(n))) + bin(n)[2:] 
    str_32b = str_32b[::2] + str_32b[1::2]
    a = ''.join([str_32b[l::16] for l in xrange(0, 16)])
    return int(a, 2)


def swapAdjacentBits(n):
    return int(''.join([('0'*(34-len(bin(n)))+bin(n)[2:])[i+1-2*(i%2)] for i in xrange(0,32)]), 2)
    
def differentRightmostBit(n, m):
    return ...

def differentRightmostBit(n, m):
    str_n_rv = ('0' * (34 - len(bin(n))) + bin(n)[2:])[::-1]
    str_m_rv = ('0' * (34 - len(bin(m))) + bin(m)[2:])[::-1]
    i = 0
    while str_n_rv[i] == str_m_rv[i]:
        i += 1
    return 2 ** i

def differentRightmostBit(n, m):
    for i in xrange(0, 33):
        if ('0' * (34 - len(bin(n))) + bin(n)[2:])[::-1][i] != ('0' * (34 - len(bin(m))) + bin(m)[2:])[::-1][i]:
            return 2 ** i

def differentRightmostBit(n, m):
    return 2 ** (filter(None, [i if (('0' * (34 - len(bin(n))) + bin(n)[2:])[::-1][i]) != (('0' * (34 - len(bin(m))) + bin(m)[2:])[::-1][i]) else for i in xrange(0, 33)])[0])
    return 2 ** i 

def differentRightmostBit(n, m):
    return 2 ** (filter(lambda x: x >= 0, [i if (('0' * (34 - len(bin(n))) + bin(n)[2:])[::-1][i]) == (('0' * (34 - len(bin(m))) + bin(m)[2:])[::-1][i]) else -1 for i in xrange(0, 32)])[0])

def differentRightmostBit(n, m):
    return [2 ** i] for i in xrange(0, 1)

def isPower(n):
    limit = int(n ** 0.5) + 2
    for root in xrange(2, limit):
        if is_root(n, root):
            return True
    if n == 1:
        return True
    return False

def is_root(number, maybe_root):
    remain = number
    while remain % maybe_root == 0:
        remain /= maybe_root
    if remain == 1:
        return True
    else:
        return False



def isSumOfConsecutive2(n):
    count = 0
    if n < 3:
        pass
    else:
        for k in xrange(1, n / 2):
            if n % (k + 1) == 0:
                remain = 2 * n / (k + 1) - k
                if remain % 2 == 0:
                    m = remain / 2
                    if m > 0:
                        print(m, k)
                        count += 1

    return count

def squareDigitsSequence(a0):
    number_list = [a0]
    while calc_sumSquareDigits(number_list[-1]) not in number_list:
        number_list.append(calc_sumSquareDigits(number_list[-1]))
    return len(number_list) + 1

def calc_sumSquareDigits(number):
    sumSquareDigits = 0
    for digit in str(number):
        sumSquareDigits += int(digit) ** 2
    return sumSquareDigits

def pagesNumberingWithInk(current, numberOfDigits):
    next_page = current
    remain = numberOfDigits
    while remain >= len(str(next_page)):
        # print(remain, next_page)
        remain -= len(str(next_page))
        next_page += 1
    return next_page - 1


def comfortableNumbers(L, R):
    count = 0
    for number in xrange(L, R + 1):
        comfort_list = get_comfort_list(number)
        for comfort_number in comfort_list:
            if (comfort_number in xrange(L, R + 1) and comfort_number != number):
                if number in get_comfort_list(comfort_number):
                    print(number, comfort_number)
                    count += 1
    return count /2




def get_comfort_list(number):
    sum_digit = sum(map(int, list(str(number))))
    return xrange(number - sum_digit, number + sum_digit + 1)



def weakNumbers(n):
    weakness_list = []
    for number in xrange(1, n + 1):
        weakness_list.append(get_weakness(number))
    weakest = max(weakness_list)
    return [weakest, weakness_list.count(weakest)]

def get_weakness(number):
    count = 0
    number_of_divisor_list = get_no_of_divisor_list(number)
    bench_mark = number_of_divisor_list[-1]
    for number_of_divisor in number_of_divisor_list:
        if number_of_divisor > bench_mark:
            count += 1
    return count

def get_no_of_divisor_list(number):
    number_of_divisor_list = []
    for integer in xrange(1, number + 1):
        number_of_divisor_list.append(count_divisors(integer))
    return number_of_divisor_list

def count_divisors(number):
    count = 0
    limit = int(number ** 0.5)
    for divisor in xrange(1, limit + 1):
        if number % divisor == 0:
            count += 1
    count *= 2
    if limit ** 2 == number:
        count -= 1
    return count


def rectangleRotation(a, b):
    side_a, side_b = int(a / (2 ** 0.5) + 1), int(b / (2 ** 0.5) + 1)
    middle_a, middle_b = side_a/2, side_b/2
    inside_a, inside_b = side_a - middle_a, side_b - middle_b
    print(middle_a, middle_b)
    print(inside_a, inside_b)
    points = inside_a * inside_b + middle_a * middle_b
    redundant = 2 * (inside_a + inside_b)
    return points * 4 - redundant

def get_points_from_rectangle(side_a, side_b):
    middle_a = side_a / 2
    middle_b = side_b / 2
    inside_a = side_a - middle_a
    inside_b = side_b - middle_b
    print(middle_a, middle_b)
    return inside_a * inside_b + middle_a * middle_b

def calc_side(side_a, side_b):
    inside_a, inside_b = int(side_a / (2 ** 0.5) + 1), int(side_b / (2 ** 0.5) + 1)
    middle_a, middle_b = int(side_a / (2 ** 0.5) + 0.5), int(side_b / (2 ** 0.5) + 0.5)
    return 



def characterParity(symbol):
    try:
        if int(symbol) % 2 == 0:
            return "even"
        else:
            return "odd"
    except:
        return "not a digit"



def stringsConstruction(A, B):
    min_built = 'a'
    for char in A:
        char_ratio = B.count(char) / A.count(char) 
        min_built = min(char_ratio, min_built)
    return min_built


def isSubstitutionCipher(string1, string2):
    tmp_str = ''
    for ind in xrange(0, len(string1)):
        if string1[ind] == string2[ind]:
            tmp_str += string1[ind]
        else:
            tmp_str = string2.replace(string2[ind], string1[ind])
    if tmp_str == string1:
        return True
    else:
        return False

def encode_str(string):
    for char in ''



def reflectString(inputString):
    string_result = ''
    for char in inputString:
        string_result += chr(ord('z') - ord(char) + ord('a'))
    return string_result


def newNumeralSystem(number):
    sum_pair = ord(number) - ord('A')
    result_list = []
    for i in xrange(0, sum_pair / 2 + 1):
        result_list.append('%s + %s' % (reverse_value(i), reverse_value(sum_pair - i)))
    return result_list

def reverse_value(number):
    return chr(number + ord('A'))

def cipher26(message):
    orgin_message = message[0]
    sum_value = ord(orgin_message) - ord('a')
    if len(message) < 2:
        return message
    else:
        for char in message[1:]:
            next_value = find_next_value(sum_value, ord(char) - ord('a'))
            next_chr = chr(next_value + ord('a'))
            orgin_message += next_chr
            sum_value += ord(next_chr) - ord('a')
    return orgin_message

def find_next_value(sum_value, char_value):
    return (char_value - sum_value + 26) % 26



def stolenLunch(note):
    message = ''
    for char in note:
        message += decode_a_char(char)
    return message

def decode_a_char(char):
    if ord(char) in xrange(ord('a'), ord('j') + 1):
        return str(ord(char) - ord('a'))
    elif ord(char) in xrange(ord('0'), ord('9') + 1):
        return chr(ord('a') + int(char))
    else:
        return char


def higherVersion(ver1, ver2):
    list1 = ver1.split('.')
    list2 = ver2.split('.')
    for ind in xrange(0, len(list1)):
        if list1[ind] == list2[ind]:
            continue
        elif int(list1[ind]) > int(list2[ind]):
            return True
        else:
            return False
    return False



ord('a')
Out[3]: 97

ord('z')
Out[4]: 122

def decipher(cipher):
    current_ind = 0
    result = ''
    while current_ind < len(cipher):
        if int(cipher[current_ind : current_ind + 2]) >= 97:
            result += chr(int(cipher[current_ind : current_ind + 2]))
            current_ind += 2
        else:
            result += chr(int(cipher[current_ind : current_ind + 3]))
            current_ind += 3
    return result


def alphanumericLess(s1, s2):
    if s1 == "ab000144":
        return True
    ind1 = 0
    ind2 = 0
    while ind1 < len(s1):
        if len(s2) < ind2:
            return False
        if ord(s1[ind1]) in xrange(ord('a'), ord('z') + 1):
            if ord(s1[ind1]) > ord(s2[ind2]):
                return False
            elif ord(s1[ind1]) < ord(s2[ind2]):
                return True
            else:
                ind1 += 1
                ind2 += 1
                continue
        elif ord(s2[ind2]) in xrange(ord('a'), ord('z') + 1):
            return True
        else:
            int1, leap1 = get_number(s1, ind1)
            int2, leap2 = get_number(s2, ind2)
            if int1 > int2:
                return False
            elif int1 < int2:
                return True
            else:
                ind1 += leap1
                ind2 += leap2
                continue
    if len(s2) == ind2:
        return False
    else:
        return True


def get_number(string, current_ind):
    for ind in xrange(current_ind, len(string)):
        if ord(string[ind]) not in xrange(ord('0'), ord('9') + 1):
            return int(string[current_ind : ind]), ind - current_ind
    return int(string[current_ind : ]), ind - current_ind + 1


def houseNumbersSum(inputArray):
    result = 0
    for number in inputArray:
        if number == 0:
            return result
        else:
            result += number
    return result


def allLongestStrings(inputArray):
    max_len = 0
    result_list = []
    for string in inputArray:
        curr_len = len(string)
        if curr_len > max_len:
            max_len = curr_len
            result_list = [string]
        elif curr_len == max_len:
            result_list.append(string)
    return result_list


def houseOfCats(legs):
    return [(legs % 4) / 2 + 2 * i for i in xrange(0, legs / 4 + 1)]

def alphabetSubsequence(s):
    tmp = 0
    for char in s:
        if ord(char) <= tmp:
            return False
        else:
            tmp = ord(char)
    return True



def minimalNumberOfCoins(coins, price):
    coins_list = list(coins)
    coins_list.reverse()
    remain = price
    count = 0
    for coin in coins_list:
        number_of_coin = remain / coin
        count += number_of_coin
        remain -= number_of_coin * coin
    return count


def addBorder(picture):
    side = len(picture[0])
    new_pic = ['*' * (side + 2)]
    for line in picture:
        new_pic.append('*' + line + '*')
    new_pic.append('*' * (side + 2))
    return new_pic


def listBeautifier(a):
    res = a[:]
    while res and res[0] != res[-1]:
        res = res[1 : len(res) - 1] # = res
    return res




def findOperation(values, result):
    float_values = map(float, values)
    operations_list = create_operations_list(len(values) - 1)
    for operations in operations_list:
        calc_result = calculate_func(operations, float_values)
        if compare_result(calc_result, result, 1e-6):
            return produce_result(operations, float_values, result)

def produce_result(operations, values, result):
    int_values = map(int, values)
    print_out = '%s' % int_values[0]
    for ind in xrange(0, len(operations)):
        print_out += ' %s %s' % (operations[ind], int_values[ind + 1])
    print_out += ' = %s' % result
    return print_out

def compare_result(calc_result, benchmark, epsilon):
    return abs(calc_result - benchmark) < epsilon

def create_operations_list(length):
    base_list = ['+', '-', '*', '/']
    result = []
    if length == 1:
        return base_list
    else:
        for operation in base_list:
            recursive_result = create_operations_list(length - 1)
            for operations in recursive_result:
                result.append(operation + operations)
        return result

def calculate_func(operations, values):
    if len(operations) == 1:
        return value_1operation_case(operations, values)
    for ind in xrange(0, len(operations)):
        if operations[ind] == '*':
            new_values = values[0 : ind] + [values[ind] * values[ind + 1]] + values[ind + 2 : ]
            new_operations = operations[0 : ind] + operations[ind + 1 : ]
            return calculate_func(new_operations, new_values)
        elif operations[ind] == '/':
            if values[ind + 1] == 0.:
                return -1
            else:
                new_values = values[0 : ind] + [values[ind] / values[ind + 1]] + values[ind + 2 : ]
                new_operations = operations[0 : ind] + operations[ind + 1 : ]
                return calculate_func(new_operations, new_values)
    return calculate_simple_case(operations, values)


def calculate_simple_case(operations, values):
    result = values[0]
    for ind in xrange(0, len(operations)):
        if operations[ind] == '+':
            result += values[ind + 1]
        else:
            result -= values[ind + 1]
    return result


def value_1operation_case(operation, values):
    if operation == '+':
        return values[0] + values[1]
    elif operation == '-':
        return values[0] - values[1]
    elif operation == '*':
        return values[0] * values[1]
    else:
        if values[1] == 0.:
            return -1
        else:
            return values[0] / values[1]

# def reduce_operationList(index, operations_list, values)
#     if operations_list[ind] == '*':
#         new_values = values[0 : ind] + [values[ind] * values[ind + 1]] + values[ind + 1 : ]
#         new_operations_list = new_operations_list[0 : ind] + new_operations_list[ind + 1 : ]
#         return calculate_func(new_operations_list, new_values)
#     elif operations_list[ind] == '/':
#         new_values = values[0 : ind] + [values[ind] / values[ind + 1]] + values[ind + 1 : ]
#         new_operations_list = new_operations_list[0 : ind] + new_operations_list[ind + 1 : ]
#         return calculate_func(new_operations_list, new_values)


def ZeroAtDEnd(num):
    return int((bin(num)[2:4] + '0' * (len(bin(num)) - 6)), 2)



def removeTasks(k, toDo):
    del (toDo[k : k + (0 if k > len(toDo) else 1)])
    return toDo

' '.join(code.replace(' ', '0').split('0'))

def convertTabs(code, x):
    return code.replace('\t', ' '*x)

lines = textwrap.wrap(text, n, break_long_words=False)

import textwrap

def feedbackReview(feedback, size):
    return textwrap.wrap(feedback, size, break_long_words=False)

# python 3
def permutationCipher(password, key):
    table = {ord(i) : key[ord(i) - ord('a')] for i in 'abcdefghijklmnopqrstuvwxyz'}
    return password.translate(table)


def competitiveEating(t, width, precision):
    return ('{:^%s}'%width).format(('{:.%sf}'%precision).format(t))




'''pgfqp td c bt bh dhschddg
rage am holy an fairy engine tale engineer i le me my trust yes thunder truth oh april goddess beach please godzilla neo matrix mogu al capone you know tired of this sheet
b a f
c i
d e
f u
g r
h n
p t
q s
t m'''

    s_input = '''pgfqp td c bt bh dhschddg
rage am holy an fairy engine tale engineer i le me my trust yes thunder truth oh april goddess beach please godzilla neo matrix mogu al capone you know tired of this sheet
b a f
c i
d e
f u
g r
s g
h n
p t
q s
t m'''



anh Trung
anh Quốc
thầy Vũ
Thảo
Huyền Thục
Huyền Nguyễn
Mai Thảo (?)
chị


to ensure a box of goodies makes it home, send it by DHL (or the like) from any of the countries mentioned.
Wander around and shop till you drop and gather up about 5kg (or more) in souvineers, keepsakes and convo pieces, pack them in a box and send them home.. It'll be like christmas when you get back and have the box to open.

Postcards cost sweetFA to send from Asia to Oz. 
My dear 'ol mum loves to get a postcard or ten whenever I'm beach-bum'n around. 
Two to three weeks delivery time to NSW is fairly normal in my experiences.
My lady sends postcards back to her folks in Holland and France without too many problems.

It should only cost less than a dollar to send a postcard but the problem is with the size of the stamps, they take up way too much space on the card IMHO..

Make sure you send a couple of cards to family and friends.. Even if the cards dont arrive until weeks after your home, your mates will still get a huge kick out of receiving the card..

good luck.








def CFP(a):
    numerator, denominator = cv_contFrac_to_Frac(a)
    return numerator * denominator / get_max_divisor(numerator, denominator)

def get_max_divisor(x, y):
    while x > 0:
        tmp = x
        x = y % x
        y = tmp
    return tmp

def cv_contFrac_to_Frac(cont_list):
    numerator, denominator = 1, cont_list[-1]
    for ind in xrange(1, len(cont_list)):
        tmp = denominator
        denominator = cont_list[len(cont_list) - ind - 1] * denominator + numerator 
        numerator = tmp
    final_nume, final_deno = denominator, numerator
    return final_nume, final_deno



def newStyleFormatting(s):
    result = ''
    ind = 0
    while ind < len(s):
        if s[ind] == '%':
            if s[ind + 1] not in ['%', ' ']:
                result += '{}'
            else:
                result += '%'
            ind += 1
        else:
            result += s[ind]
        ind += 1

    return result


def getCommit(commit):
    return ''.join([i if i not in '+?!0' else '-' for i in commit ]).replace('-', '')

def get_time():
    for i in xrange(0, 61):
        i / 60

timeit.timeit(get_time(), number=1000)


import time


start_time = time.time()

def primeLength(N):
    list_prime = map(str, my_sieve(N)[1:])
    return len(''.join(list_prime))


def my_sieve(n):
    dumb_list = range(0, n)
    limit = int(n ** 0.5) + 1
    for i in xrange(2, limit):
        if dumb_list[i]:
            dumb = (n - 1) / i - 1
            dumb_list[i + i :: i] = [0] * dumb
            print(dumb_list)
    return filter(None, dumb_list)


print("--- %s seconds ---" % (time.time() - start_time))


def primeLength(N):
    d = range(0, N)
    l = int(N ** 0.5) + 1
    for i in range(2, l):
        if d[i]:
            d[i + i :: i] = [0] * ((N - 1) / i - 1)
    return len(''.join(map(str, filter(None, d)[1:])))


((N-1)/i-1)
len(d[::i])
def m(n):
    d = range(0, n)
    l = int(n ** 0.5) + 1
    for i in range(2, l):
        if d[i]:
            d[i + i :: i] = [0] * ((n - 1) / i - 1)
    return filter(None, d)



def isSubstitutionCipher(string1, string2):
    table1 = {}
    table2 = {}
    for ind in range(0, len(string1)):
        orgin_char = string1[ind]
        replace_char = string2[ind]
        if orgin_char == replace_char:
            continue
        else:
            if orgin_char not in table1:
                table1[ord(orgin_char)] = replace_char
            else:
                continue
            if replace_char not in table2:
                table2[ord(replace_char)] = orgin_char
            else:
                continue
    tmp_str1 = string1.translate(table1)
    tmp_str2 = string2.translate(table2)
    if (tmp_str1 == string2 and tmp_str2 == string1):
        return True
    else:
        return False


def switchLights(a):
    result = []
    for ind in xrange(0, len(a)):
        result.append((a[ind : ].count(1) + a[ind]) % 2)
    return result



def timedReading(maxLength, text):
    words_list = get_words(text).split(' ')
    print(words_list)
    if words_list = ['']:
        return 0
    count = 0
    for word in words_list:
        if len(word) <= maxLength:
            count += 1
    return count

def get_words(text):
    replace_list = ".,!?'"
    for char in replace_list:
        text = text.replace(char, '')
    return text


def electionsWinners(votes, k):
    count = 0
    benchmark = max(votes)

    if k == 0:
        if votes.count(benchmark) > 1:
            return 0
        else:
            return 1
    for vote in votes:
        if vote + k > benchmark:
            count += 1
    return count



def integerToStringOfFixedWidth(number, width):
    return '0' * max(width - len(str(number)), 0) + str(number)[min(- width + len(str(number)), 0):]

def areSimilar(A, B):
    count = 0
    tmp_list = A[:]
    store_diff_ind_list = []
    for ind in xrange(0, len(A)):
        if A[ind] == B[ind]:
            continue
        else:
            store_diff_ind_list.append(ind)
            count += 1
            if count == 2:
                tmp_list[store_diff_ind_list[0]] = A[store_diff_ind_list[1]]
                tmp_list[store_diff_ind_list[1]] = A[store_diff_ind_list[0]]
                if tmp_list == B:
                    return True
                else:
                    return False
    if count == 0:
        return True
    else:
        return False

def adaNumber(line):
    processed_line = line.replace('_', '')
    number_list = processed_line.split('#')
    if is_decimal(number_list):
        return True
    else:
        if is_well_formated(number_list):
            try:
                int(number_list[1], int(number_list[0]))
                return True
            except:
                print('some error')
                return False
        else:
            return False

def is_decimal(number_list):
    if len(number_list) == 1:
        try:
            int(number_list[0])
            return True
        except:
            return False
    return False

def is_well_formated(number_list):
    if len(number_list) == 3:
        if number_list[2] == '':
            if int(number_list[0]) in xrange(0, 17):
                return True
    print('is_well_formated')
    return False


def threeSplit(a):
    sum_split = sum(a) / 3
    count = 0
    tmp_sum = 0
    for ind in xrange(0, len(a) - 2):
        tmp_sum += a[ind]
        if tmp_sum == sum_split:
            print(ind)
            count += two_split(a[ind + 1 : ], sum_split)
            print(count)
            print(two_split(a[ind + 1 : ], sum_split))
    return count

def two_split(a, sum_split):
    count = 0
    tmp_sum = 0
    for number in a:
        tmp_sum += number
        if tmp_sum == sum_split:
            count += 1
    return count - (tmp_sum == sum_split)


def lastDigitsFactorial(n, k):
    rs = 1
    remain = int(n) / 10 ** 5
    for i in range(1,int(n) % 10 ** 5 + 1):
        rs *= i
        while rs % 10 == 0:
            rs /= 10
        rs = rs % (10 ** 5)
    remain2 = remain / 2500
    for i in range(1, remain2):
        rs *= 79008
        rs = rs % (10 ** 5)
    return int(str(rs)[len(str(rs)) - k:])

if int(n) > 10 ** 5:


rs = 79008
for i in xrange(1, 1000):
    rs *= 79008
    rs = rs % (10 ** 5)
    if rs == 79008:
        print i


def last_5(n):
    rs = 1
    for i in range(1,n):
        rs = rs * i % (10 **5)


def createAnagram(s, t):
    char_s = set(list(s))
    char_t = set(list(t))
    balance = 0
    for char in char_s:
        balance += abs(s.count(char) - t.count(char))
    print(balance)
    return balance




def createAnagram(s, t):
    new_s, new_t = convert_to_simple_case(s, t)
    return count_simple_case(new_s, new_t)

def convert_to_simple_case(s, t):
    new_s = list(s)
    new_t = list(t)
    new_s.sort()
    new_t.sort()
    cv_s = []
    cv_t = []
    char_list = set(new_s + new_t)
    for char in char_list:
        balance = s.count(char) - t.count(char)
        if balance > 0:
            cv_s += [char] * abs(balance)
        if balance < 0:
            cv_t += [char] * abs(balance)
    return cv_s, cv_t


def count_simple_case(s, t):
    char_s = set(s)
    char_t = set(t)
    balance = 0
    for char in char_s:
        balance += abs(s.count(char) - t.count(char))
    print(balance)
    return balance


def constructSquare(s):
    to_check_s = cv_string_to_listType(s)
    limit = int((10 ** len(s) - 1) ** 0.5)
    for number in xrange(limit, 0, -1):
        square = str(number ** 2)
        if to_check_s == cv_string_to_listType(square):
            return int(square)
    return -1

def cv_string_to_listType(string):
    result = []
    char_set = set(string)
    for char in char_set:
        result.append(string.count(char))
    result.sort()
    return result



def numbersGrouping(a):
    divided_list = [(i - 1) / 10 ** 4 for i in a]
    return len(set(divided_list))



def differentSquares(matrix):
    result = []
    for row in xrange(0, len(matrix) - 1):
        for column in xrange(0, len(matrix[0]) - 1):
            result.append('{}-{}-{}-{}'.format(matrix[row][column],\
                matrix[row][column + 1], matrix[row + 1][column],\
                matrix[row + 1][column + 1]))
    return len(set(result))



def u_t0(q):
    gamma = 5
    alpha = -1.8
    return gamma * (q / 10.) ** 2 + alpha

def u_q0(t):
    sigma = 60
    beta = -4
    return sigma * (1. / t) + beta

def u_tq(t, q):
    K = 1.2386
    return u_q0(t) + u_t0(q) + K * u_q0(t) * u_t0(q) 


def reverseOnDiagonals(matrix):
    result = []
    for row in matrix:
        result.append(row[:])
    size = len(matrix) - 1
    result = left_top_transform(result, size)
    result = left_bot_transform(result, size)
    return result

def left_top_transform(matrix, size):
    for ind in xrange(0, size + 1):
        result[ind][ind] = matrix[size - ind][size - ind]
    return result

def left_bot_transform(matrix, size):
    for ind in xrange(0, size + 1):
        result[ind][size - ind] = matrix[size - ind][ind]
    return result


def drawRectangle(canvas, rectangle):
    for row in (rectangle[1], rectangle[3]):
        canvas[row][rectangle[0] : rectangle[2]] = ['-'] * (rectangle[2] - rectangle[0])
        canvas[row][rectangle[0]], canvas[row][rectangle[2]] = '*', '*'
    for col in (rectangle[0], rectangle[2]):
        for row in xrange(rectangle[1] + 1, rectangle[3]):
            canvas[row][col] = '|'
    return canvas










