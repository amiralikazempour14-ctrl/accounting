v = {'a': 15, 'b': 12, 'c': 19}
print(v['a'])
print(v.get('z'))
v['c'] = 20
print(len(v))
print('b' in v)
print(12 in v)
for i in v:
    print(i)