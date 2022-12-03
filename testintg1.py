print('hello')

new_list = []
for i in range(20):
    print(i*2, end=' ')
    new_list.append(i*2)

for i in new_list:
    print(i*3)

print('Bye')
