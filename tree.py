from anytree import Node,RenderTree

class triNode(Node):
	def __init__(self,value,parent=None):
		'''
		:param value: value Node
		:param parent: Node parent
		:parameter endpoint: True \ False. Ture if end of the word. default: flase
		:parameter priority: priority by the number of show(inserts). default: 0
		:parameter child_d: dictionary of all childs. the first char in words
		'''
		
		super().__init__(value,parent=parent)
		self.endpoint = False
		self.priority = 0 
		self.child_d = dict()


	
	def add_2_tree(self,word):
		'''
		:param self: triNode
		:param word: the new word to add
		:return: add new word to tree, if the there is word that include, continue in hirarchy .
		'''
		# todo: what happend when the word is one char --done
		# todo: update node to endpoint like add ori and then or --need to update r Node to endpoint --done
		
		word, node_end = self.__search_in_tree(word)  # ! retrurn 'eetah',c/h
		if not node_end:  # ! no match with this word, and need to create new tree
			node_end = triNode(word[0], self)
			self.child_d[word[0]] = node_end
			word = word[1:]  # ! the first char added
			
			if not word:  # ! if is more then one char
				node_end.endpoint = True
				return
		
		# ! root node != None
		# ! update endpoint to Ture when this word include in other word
		if not word:
			# ! return from __search_in_tree empty word, but there is root
			
			if node_end.endpoint:
				# ! this word already exist  - the endpoind already true
				node_end.priority += 1
			else:  # ! the word should be inclued into other word but its not mark as endpoint
				node_end.endpoint = True
			return
		
		# ! add all left word to tree
		for i, char in enumerate(word):
			node_end = triNode(char, parent=node_end)
			if char == word[-1] and len(word) - 1 == i:  # ! if there is same char in the end but the words dosent end yet
				node_end.endpoint = True  # ! end of the word
		
	def __get_Node_of_strt(self,ch):
		if self.children:
			root = [child for child in self.children if child.name == ch]
		if root:
			return root[0]
		return Node(ch,paren=self)
	
	def __search_in_tree(self, word, root=None):
		'''
		:param self: triNode
		:param word: the word to looking for
		:param root: the highest node by first char
		:return: the lowest node in path is match with word
		'''
		# todo: what happend when the word is one char --done
		
		if self.name is None:
			self = self.child_d.get(word[0])  # ! get the highest node by first char, None otherwise
		
		if self:
			if self.name == word:
				return word[1:], self
			
			if self.children:
				if len(word) > 1:
					# todo bad to open children twice --done
					ch = word[1]
					child = [n for n in self.children if n.name == ch]
					
					if child:
						
						child = child[0]
						if child.name == word[-1]:
							return word[2:], child
						
						return child.__search_in_tree(word[1:])
			
			return word[1:], self
		return word, None  # ! no match charter ordanization
	
	
	def __get_words(self, lst_words=list(), str_w=''):
		'''
		:param self: triNode
		:param lst_words: list of the word are found
		:return: list of 3 or less words ,are complite from root
		'''
		
		# if len(lst_words) ==3:
		#     return lst_words
		
		# lst_words.append(str_w + self.name)
		
		# todo: if there is duppicate char is skiped :( --done
		
		if self.depth  <= len(str_w):
			if self.name not in str_w[self.depth-1]:
				str_w += self.name
		else:
			str_w += self.name
		
		if self.endpoint:  # ! end of word
			if len(lst_words) == 3 and self.priority > 0:  # ! when this word with high priority then other
				del lst_words[-1]
			if len(lst_words) < 3:  # ! dont appent if there are 3 elemnts
				lst_words.append(str_w)
		
		if self.children:
			for child in self.children:
				child.__get_words(lst_words=lst_words, str_w=str_w)
		return lst_words
	
	def complite(self,input_key):
		'''
		:param self: triNode
		:param input_key: the input for complite
		:return: 3 option to complite
		'''
		lst_word = list()
		# todo: if there arent root key --done
		if self.child_d.get(input_key[0]):  # ! if there is a root tree for this by first char
			root = self.child_d[input_key[0]]
			if root.endpoint:
				lst_word.append(root.name)
				if not root.children:  # ! just endpoint char can be witout children
					return lst_word
			
			# ! if its not endpoint its must be with children
			w_left, root = self.__search_in_tree(
				input_key)  # ! to get the lowest node in tree, and the latters arent exist in tree
			if w_left:  # ! the word dosent exist in tree
				return None
			# todo: if there no continue to input --done
			return root.__get_words(str_w=input_key)
		return None
	
	def print_simple(self):
		for pre, fill, node in RenderTree(self):
			print(pre, node.name)