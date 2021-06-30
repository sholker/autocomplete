from anytree import Node, RenderTree
import os



def add_2_tree_from_file(filename):
    lst = list()

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
        raise e




def search_in_tree(word, root=None):
    # todo: what happend when the word is one char
    if not root:
        root = dk.get(word[0])
    if root:
        if root.name ==word:
            return word[1:],root
        
        if root.children:
            if len(word) > 1:
                # todo bad to open children twis --done
                ch = word[1]
                child = [n for n in root.children if n.name == ch]
                
                if child :
                    
                    child=child[0]
                    if child.name == word[-1]:
                        return word[2:],child
                    
                    return search_in_tree(word[1:], child)


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
    todo: what happend when the word is one char --done
    :param word:
    :return: add new word to tree, continue in hirarchy
    '''
    # node_end,word = search_in_tree(word)
    word,node_end = search_in_tree(word) # ! retrurn 'eetah',c/h
    if not node_end:
        node_end = Node(word[0])
        dk[word[0]]=node_end
        word=word[1:]
    # if not node_end:
    #     dk[word[0]] = Node(word[0])
    #     node_end = dk[word[0]]
        if not word: # ! if is more then one char
            node_end.endpoint=True
            return
        
    # if get root node
    # update endpoint to Ture when this word include in other word
    if not word:
        if node_end.endpoint:
            # this word already exist  - the endpoind already true
            node_end.priority+=1
        else:
            node_end.endpoint=True
        return

    for i,char in enumerate(word):
        node_end = Node(char,parent=node_end)
        if char ==word[-1] and len(word)-1 ==i:# if there is same char in the end but the words dosent end yet
            node_end.endpoint=True



def get_words(root,str='',lst_words=list()):
    # if len(lst_words) ==3:
    #     return lst_words
    
    # lst_words.append(''.join([p.name for p in root.path]))
    
    if root.endpoint:
        if len(lst_words)==3 and root.priority > 0:
            del lst_words[-1]
            lst_words.insert(0,''.join([p.name for p in root.path]))
        if len(lst_words)<3:
            lst_words.append(''.join([p.name for p in root.path]))
            
            
    if root.children:
        for child in root.children:
            get_words(child,lst_words)
    return lst_words
    
def complite(input_key):
    lst_word=list()
    # todo: if there arent root key --done
    if dk[input_key[0]]:
        root = dk[input_key[0]]
        if root.endpoint:
            lst_word.append(root.name)
        if root.children:
            w_left,root = search_in_tree(input_key)
            if w_left:
                return None
            # todo: if there no continue to inpute --done
            return get_words(root, input_key)
    return None



def print_simple(root):
    for pre, fill, node in RenderTree(root):
        print(pre,node.name)

if __name__ == '__main__':
    dk = dict()
    setattr(Node, "endpoint", False)
    setattr(Node, "priority", 0)
    filename = 'C:/Users/Avigail/PycharmProjects/gcp/autocomplite/word-list-short-52.txt'
    # add_2_tree_from_file(filename)
    # todo: update node to endpoint like add ori and then or --need to update r Node to endpoint --done
    add_2_tree_from_file(['i','cow','cat','cow','ori','camember','camel','puppet','pull'])

    print(dk.get('i'))
    # print(dk.get('c').children[1].children[0].name)
    # print(dk.get('c').children[1].children[0].priority)
    # print(return_v)
    
    # print_simple(dk.get('c'))

    string = input("enter your input: ")

    print(complite(string))

    # for k in dk:
    #     print_simple(dk.get(k))