d=[]
d.append('add to cart')
d.append('not in stock')
# print("no" in d or "Not" in d)
no_stock = ['no', 'not']
in_stock = ['cart', 'add']
#
res_no = [ele for ele in no_stock if(ele in d[0])]
res_yes = [ele for ele in in_stock if(ele in d[0])]
# print((bool(res_no)))
# print(str(bool(res_yes)))
print(bool(res_no))
print(bool(res_yes))

print(d[0])
print(d[1])
for i in range(2):

    if bool([ele for ele in no_stock if(ele in d[i])]):
        print('1')
    elif bool([ele for ele in in_stock if(ele in d[i])]):
        print('2')
    else:
        print('3')

xx = 1
if xx == 2:
    print('11')
elif xx == 1:
    print('22')
