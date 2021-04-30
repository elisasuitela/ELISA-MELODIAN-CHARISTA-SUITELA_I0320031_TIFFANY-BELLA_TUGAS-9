import array
# mengonversi list ke dalam array.array
li = [10, 20, 30, 40, 50]
c = array.array('1')
c.fromlist(li)
type(c)
type 'array.array'
for nilai in c:
    print("%d " % nilai, end='')
