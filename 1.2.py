#Долган Ксенія
#Варіант 7
#7. Задано текст, слова в якому розділені пробілами і розділовими знаками. Розробити програму, яка
#вилучає з цього тексту всі повторні входження слів.

string1 = "Hello . My name is Ksenia . I love my name . I love to say Hello "
words = string1.split()
print (" ".join(sorted(set(words), key=words.index)))