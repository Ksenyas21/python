num = int(input('N= '))
dict = {}
for i in range(num):
    print("key prb value")
    key = input()
    value = input()
    dict[key] = value
print(dict)
arg = input()
for key in dict:
    if arg == key:
        print(value-1)


