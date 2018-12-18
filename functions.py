
# coding: utf-8

# In[8]:


import ast


# In[9]:


def read_vocabulary(file = 'vocabulary.txt'):
    vocabulary = {}
    # opening the .txt file
    with open(file, 'r', encoding = 'utf8') as f: 
        # splitting the file into rows
        rows = f.read().split('\n') 
        # the last row in rows is empty
        for r in rows[:-1]:
            items = r.split('\t')
            # the firt element of each row is the word string
            key = items[0] 
            # the second element is the word_id
            value = int(items[1])
            # dictionary structure: {word : word_id}
            vocabulary[key] = value
    return vocabulary


# In[10]:


def read_inv_indx(file = 'inverted_indx.txt'):
    inv_indx = {}
    # opening the .txt file
    with open(file, 'r', encoding = 'utf8') as f: 
        # splitting the file into rows
        rows = f.read().split('\n') 
        # the last row in rows is empty
        for r in rows[:-1]:
            items = r.split('\t')
            # the firt element of each row is the word_id
            key = int(items[0]) 
            # values are stored into a list
            values = []
            for num in items[1:]:
                values.append(int(num))
            # dictionary structure: {word_id : doc_id}
            inv_indx[key] = values
    return inv_indx


# In[29]:


def read_inv_indx_tfidf(file = 'inverted_indx_tfid.txt'):
    inv_indx_tfidf = {}
    # opening the .txt file
    with open(file, 'r', encoding = 'utf8') as f: 
        # splitting the file into rows
        rows = f.read().split('\n') 
        # the last row in rows is empty
        for r in rows[:-1]:
            items = r.split('\t')
            # the firt element of each row is the word_id
            key = int(items[0]) 
            # values are stored into a list of tuples
            values = []
            for tup in items[1:]:
                values.append(ast.literal_eval(tup))
            # dictionary structure: {word_id : [(doc_id, tfidf)]}
            inv_indx_tfidf[key] = values
    return inv_indx_tfidf

inv_indx_tfidf = read_inv_indx_tfidf(file = 'inverted_indx_tfid.txt')


