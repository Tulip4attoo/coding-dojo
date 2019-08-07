import time
import decimal

context = decimal.Context(prec=100)

start_time = time.time()

def cv_contFrac_to_Frac(cont_list):
    numerator, denominator = 1, cont_list[-1]
    for ind in xrange(1, len(cont_list)):
        tmp = denominator
        denominator = cont_list[len(cont_list) - ind - 1] * denominator + numerator 
        numerator = tmp
    final_nume, final_deno = denominator, numerator
    return final_nume, final_deno

def create_contFrac(preFrac = None):
    contFrac = list(preFrac)
    contFrac.append(2)
    return contFrac

def count(D, number):
    count = 0
    contFrac = [1]
    for i in xrange(0, number):
        contFrac = create_contFrac(contFrac)
        x, y = cv_contFrac_to_Frac(contFrac)
        if len(str(x)) != len(str(y)):
            count += 1
    return count

print(count(2, 1000))

print("--- %s seconds ---" % (time.time() - start_time))


