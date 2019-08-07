data_99 = read.csv("p099_base_exp.txt", header = F)

which.max(data_99$V2 * log(data_99$V1))