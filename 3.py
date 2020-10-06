num = int(input('N= '))
dict = {}
for i in range(num):
    print("key prb value")
    key = input()
    value = input()
    dict[key] = value
    dict[value] = key
print(dict)

arg = input('Enter word- ')
if dict[arg]:
    print(key)
