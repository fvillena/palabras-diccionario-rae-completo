
# coding: utf-8

# In[20]:


import os
import re


# In[21]:


words = []
for file in os.listdir():
    if file.endswith(".txt") and not file.startswith('dict'):
        file = open(file, "r", encoding="utf-8")
        for line in file:
            words.append(line.rstrip())


# In[22]:


cleanWords = sorted(set([re.sub('[0-9- ]', '', word) for word in words]))


# In[23]:


withComma = [word for word in cleanWords if ',' in word]
withoutComma = [word for word in cleanWords if ',' not in word]


# In[24]:


genderized = []
for word in withComma:
    male = re.search(r'(\w*),(\w*)',word)[1]
    suffix = re.search(r'(\w*),(\w*)',word)[2]
    try:
        if suffix != 'a':
            bondingPoint = abs(re.search(suffix[0], male[::-1]).start()-len(male)+1)
            prefix = male[:bondingPoint]
            female = prefix+suffix
            genderized.append(male)
            genderized.append(female)
            print('%s - %s' % (male, suffix))
            print(female)
        else:
            if male.endswith('o'):
                female = male[:-1] + suffix
                genderized.append(male)
                genderized.append(female)
                print('%s - %s' % (male, suffix))
                print(female)
            else:
                female = male + suffix
                genderized.append(male)
                genderized.append(female)
                print('%s - %s' % (male, suffix))
                print(female)
    except:
        genderized.append(male)
        print(male)


# In[25]:


words = sorted(set(withoutComma + genderized))


# In[26]:


with open('../diccionario-rae-completo.txt', mode='wt', encoding='utf-8') as file:
    file.write('\n'.join(words))

