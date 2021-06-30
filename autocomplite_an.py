from anytree import Node, RenderTree
import os



def add_2_tree_from_file(filename):
    lst = list()
    if type(filename) is not list:
        if not os.path.isfile(filename):
            print('not a file or list')
            raise

    try:
        if type(filename) is not list:
            with open(filename, 'r') as f:
                lst = f.readlines()
        else:
            lst = filename
        for line in lst:
            add_2_tree(line.strip())

    except Exception as e:
        print(e)
        raise



def search_in_tree(word, root=None,return_value = None):
    '''
    :param word:
    :param root:
    :param return_value: Endpoint node and word left
    :return: the end latter - (add continue)
    '''
    global dk
    if not root and dk.get(word[0]):
        root = dk.get(word[0])
        
    elif not return_value:
        return None,word
    
    elif root.name == word[-1]:
        return root,''

    if root.name == word[0]:
        if root.children:
            if len(word) > 1: # for example word = 't'
                if word[1] not in [n.name for n in root.children]:
                    return root,word[1:]

                for child in root.children:
                    if len(word) > 1:
                        # return search_in_tree(word[1:], child, root)
                        if child.name == word[1]:
                            return search_in_tree(word[1:], child, root)
                
                
                    return child, word[1:]
            
        else:
            return root,word[1:]
    return None


def find_match(word, root=None):
    if not root:
        root = dk.get(word[0])
    if root:
        if root.name ==word:
            return word[1:],root
        
        if root.children:
            if len(word) > 1:
                # todo bad to open children twis
                ch = word[1]
                child = [n for n in root.children if n.name == ch]
                
                if child :
                    
                    child=child[0]
                    if child.name == word[-1]:
                        return word[2:],child
                    
                    return find_match(word[1:],child)


        return word[1:],root
    return word,None
    
                    


def search_in_tree_origin(word, root=None,return_value = None):
    '''
    :param word:
    :param root:
    :param return_value: Endpoint node and word left
    :return: the end latter - (add continue)
    '''
    global dk
    if not root and dk.get(word[0]):
        root = dk.get(word[0])

    elif not return_value:
        return None,word

    if root.name == word[0]:
        if root.children:
            for child in root.children:
                if len(word) > 1:
                    # return search_in_tree(word[1:], child, root)

                    if child.name == word[1]:
                        return search_in_tree(word[1:], child, root)
                return child,word[1:]

        else:
            return root,word[1:]
    return None

def add_2_tree(word):
    '''
    todo: what happend when the word is one char
    :param word:
    :return: add new word to tree, continue in hirarchy
    '''
    # node_end,word = search_in_tree(word)
    word,node_end = find_match(word)
    if not node_end:
        node_end = Node(word[0])
        dk[word[0]]=node_end
        word=word[1:]
    # if not node_end:
    #     dk[word[0]] = Node(word[0])
    #     node_end = dk[word[0]]
        if not word: # if is more then one char
            node_end.endpoint=True
            return

    # update endpoint to Ture when this word include in other word
    if not word:
        if node_end.endpoint:
            # this word already exist  - the endpoind already true
            node_end.priority+=1
        else:
            node_end.endpoint=True
        return

    for char in word:
        node_end = Node(char,parent=node_end)
        if char ==word[-1]:
            node_end.endpoint=True

def get_words(root, str_w='',lst_words=list()):
    # if len(lst_words) == 3:
    #     return lst_words
    
    if root.endpoint:
        if len(lst_words) ==3:
            if root.priority > 0:
                del lst_words[-1]
                lst_words.insert(0,str_w)
        else:
            lst_words.append(str_w)

    if root.children:
        for child in root.children:
            str_w += child.name
            get_words(child,str_w,lst_words)
    return lst_words

def complite(input_key):
    lst_word=list()
    if dk[input_key[0]]:
        root = dk[input_key[0]]
        if root.endpoint:
            lst_word.append(root.name)
        if root.children:
            # return get_words(search_in_tree(input_key)[0],input_key)
            return get_words(find_match(input_key)[1],input_key)
    return None



def print_simple(root):
    for pre, fill, node in RenderTree(root):
        print(pre,node.name)

if __name__ == '__main__':
    dk = dict()
    setattr(Node, "endpoint", False)
    setattr(Node, "priority", 0)
    filename = "word-list-short-52.txt"
    add_2_tree_from_file(filename)
    # todo: update node to endpoint like add ori and then or --need to update r Node to endpoint
    # add_2_tree_from_file(['cam','cow','cat','cow','ori'])

    return_v = find_match('c',dk.get('c'))
    # print(dk.get('c').children[1].children[0].name)
    # print(dk.get('c').children[1].children[0].priority)
    print(return_v)
    
    # print_simple(dk.get('c'))


    print(complite('c'))

    # for k in dk:
    #     print_simple(dk.get(k))