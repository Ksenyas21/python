import cgi

form = cgi.FieldStorage()


def count_v2(word):
    vowels = 0
    for letter in word:
        if letter.isalpha():
            if letter.lower() in 'aeiouy':
                vowels += 1

    return vowels


word = str(form.getfirst('word'))
result = count_v2(word)

print('Content-type: text/html\n')
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Variant 7</title>
        </head>
        <body>""")

print('<h1  align="center">Amount of vowels: {}</h1>'.format(result))
print('</body></html>')
