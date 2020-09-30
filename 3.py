num = int(input('N= '))
dict = {}
for i in range(num):
    print("key prb value")
    key = input()
    value = input()
    dict[key] = value
print(dict)

arg = input()
for key, value in dict.items():
    if arg == key:
        print(dict[key])
    elif arg == value:
        print(key)