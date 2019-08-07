import time
import decimal

context = decimal.Context(prec=200)

start_time = time.time()

def check_pair(x, y, D):
    if x ** 2 - D * y ** 2 == 1:
        return True
    else:
        return False

def cv_contFrac_to_Frac(cont_list):
    numerator, denominator = 1, cont_list[-1]
    for ind in xrange(1, len(cont_list)):
        tmp = denominator
        denominator = cont_list[len(cont_list) - ind - 1] * denominator + numerator 
        numerator = tmp
    final_nume, final_deno = denominator, numerator
    return final_nume, final_deno

def create_contFrac(preFrac = None, magic_number = None):
    contFrac = list(preFrac)
    leftover = context.divide(1, magic_number)
    contFrac.append(int(leftover))
    magic_number = context.add(leftover, decimal.Decimal(-int(leftover)))
    return contFrac, magic_number

def find_min_x(D):
    status = False
    contFrac, magic_number = [], context.divide(1, context.sqrt(decimal.Decimal(D)))
    while status != True:
        contFrac, magic_number = create_contFrac(contFrac, magic_number)
        x, y = cv_contFrac_to_Frac(contFrac)
        status = check_pair(x, y, D)
    return x

result = 0
max_x = 0
for D in xrange(2, 1000):
    print(D)
    if D == (int(D ** 0.5)) ** 2:
        continue
    min_x_d = find_min_x(D)
    if min_x_d > max_x:
        max_x = min_x_d
        result = D

print(result)

print("--- %s seconds ---" % (time.time() - start_time))


