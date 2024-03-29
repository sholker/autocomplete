# Autocomplete
#### AutoComplete is a Python Script that provides an easy-to-use autocomplete feature for text input fields in Python applications.
----
This a Python script that imports a `triNode` class from a module named tree. It defines a function `add_2_tree_from_file` to read a list of words from a file or from a provided list, and then adds each word to a trie data structure represented by an instance of the triNode class (q). Finally, it prompts the user to enter an input string and prints the autocomplete suggestions based on the trie structure.

Here's a breakdown of what each part of your code does:

- It imports the `triNode` class from a module named tree.
- It initializes a trie node `q`.
- It defines a function `add_2_tree_from_file` that takes a filename as input, reads words from the file (or a list if provided), and adds each word to the trie.
- It checks if the input filename is a list or a file, reads the contents accordingly, and adds each word to the trie.
- It defines a main block that sets the filename, calls `add_2_tree_from_file` function to populate the trie, prompts the user to input a string, and prints the autocomplete suggestions based on the trie structure.

Please note the following points about the code:

The triNode class and its methods, such as `add_2_tree`, are assumed to be defined in the tree module.
There seems to be a typo in the function name complete, it's likely intended to be complete.


### Usage Example:

**Let's assume we have the following words in our trie: "cat", "dog", "cart", "car", "apple".**

```
root
|
+- c
   |
   +- a
   |  |
   |  +- r
   |  |  |
   |  |  +- t (*)
   |  |
   |  +- t (*)
   |
   +- d
      |
      +- o
      |  |
      |  +- g (*)
      |
      +- a
         |
         +- r
            |
            +- t (*)
```

> In this visualization:
> - Each node represents a letter in a word.
>- The (*) indicates the end of a word.
>- The path from the root to a node represents a word.
>- Words with common prefixes share nodes in the trie.

#### Run Example:
```
oris@centos01:~$ ./autocomplete.py ⏎
Enter your input: ca ⏎
['camel', 'cat']
```

**This example demonstrates running the autocomplete.py script from the command line with a specified file containing stock words ([word-list-short-52.txt](word-list-short-52.txt)). 
After executing the script, the user is prompted to input a string (ca in this case). The script then provides autocomplete suggestions based on the input, returning ['camel', 'cat'].**