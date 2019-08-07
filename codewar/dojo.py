

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








