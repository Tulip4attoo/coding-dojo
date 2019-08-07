import time
import os

problem = input("Please input the number of the problem: ")
running_text = "python p{}.py".format(problem)
start_time = time.time()
os.system(running_text)
print("--- %s seconds ---" % (time.time() - start_time))
