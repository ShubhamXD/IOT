a={'model':'Tesla','made':1994} # instantiation of dict object
a['model']  # get value using key
a.get('model') # get value using key
for i in a:
    print(f"{i} : {a.get(i)}")

a.pop(key) # delete a certain key value pair
del a['model'] # delete a key value pair
a.popitem() # delete a random key value pair after 3.7 version and it 
            # always return last delete key value pair
a['color']='red' # add another key value pair


