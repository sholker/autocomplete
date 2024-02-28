from tree import triNode

q = triNode(None)


def add_2_tree_from_file(filename):
	'''
	:param filename: path of file words or list of words
	:return: loop all words and call to add_2_tree each word
	'''
	lst = list()
	
	try:
		if type(filename) is not list:
			with open(filename, 'r') as f:
				lst = f.readlines()
		else:
			lst = filename  # ! when I get a list of words
		for line in lst:
			q.add_2_tree(line.strip())
	
	except Exception as e:
		print(e)
		exit(1)


if __name__ == '__main__':
	# filename = './word-list-short-52.txt'
	filename = 'word-list-short-52.txt'
	
	add_2_tree_from_file(filename)
	print(q.children)
	
	string = input("enter your input: ")
	
	print(q.complite(string))
