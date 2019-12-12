a=open('a.txt','w')
a.write("Hello there")
a.flush()
a.close()
with open('a.txt','w') as f:
    f.write("Hello there")
    f.flush()
