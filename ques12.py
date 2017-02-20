def sorted_words(alist):

	new_line = []
    w_words = []
	for i in alist:
		new_line.append(i)
	w_words=sorted(new_line)
    return ",".join(w_words)

listInput=map(str,input().split(","))
print(sorted_words(listInput))
