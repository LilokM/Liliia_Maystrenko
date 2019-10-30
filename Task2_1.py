Zen = '''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren\'t special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it. 
Although that way may not be obvious at first unless you\'re Dutch.    
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it\'s a bad idea.
If the implementation is easy to explain, it may be a good idea.      
Namespaces are one honking great idea -- let\'s do more of those!'''
# Prints number of occurrence of certain words
occurrence = "2.1.1 Count of certain words:\n"
print(occurrence)
print("The count of \'better\' is:", Zen.count("better"))
print("The count of \'never\' is:", Zen.count("never"))
print("The count of \'is\' is:", Zen.count("is"))

# Prints Zen string in lowercase
print("\n")
lettercase = "2.1.2 Python philosophy in lowercase:\n"
print(lettercase)
print(Zen.lower())

# Prints Zen string with replacing 'i' by '&' 
print("\n")
change = "2.1.3 Python philosophy with \'i\' being replaced by \'&\':\n"
print(change)
print(Zen.replace("i","&"))
