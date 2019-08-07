alphabet = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}

data = open("p042_words.txt", "r")
base_text = []
dumb_text = []
count = 0

triangle_numbers_list = []
for i in xrange(1, 100):
	triangle_numbers_list.append(i * (i - 1) / 2)

for raw_text in data:
	text = raw_text.split(",")
	base_text = map(str, text)

for word in xrange(0, len(base_text)):
	dumb = list(base_text[word])
	dumb_value = 0
	for char in xrange(1, len(dumb) - 1	):
		dumb_value = dumb_value + alphabet[dumb[char]]
	if dumb_value in triangle_numbers_list:
		count = count + 1


print count