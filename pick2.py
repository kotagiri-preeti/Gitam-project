import pickle
'''data = {'name':'abc','age':26,'course':'Bsc'}

with open('xyz4.txt', 'wb') as f:
    pickle.dump(data, f)
f = open('xyz.txt','wb')
pickle.dump(data,f)
f.close()'''

with open('xyz4.txt', 'rb') as f:
    a = pickle.load(f)
    print(a)
    

