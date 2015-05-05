#!/usr/bin/env python

'''
2. Write a function that converts a list to a dictionary where the index of the list is used as the key to the new dictionary (the function should return the new dictionary).
'''

# Func defenition
def list2dic(a_list):
    a_dic = {}
    i = 1
    for s in a_list:
        a_dic[i] = s
        i += 1
    return a_dic

# Main body

text = '''
2. Write a function that converts a list to a dictionary where the index of the list is used as the key to the new dictionary (the function should return the new dictionary).
'''

words = text.split()

word_dic = list2dic(words)

print ""
for key in word_dic:
    print "%-3d.%-20s" % (key, word_dic[key])
print ""

# The END
