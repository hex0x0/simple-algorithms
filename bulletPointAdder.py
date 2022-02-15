import pyperclip

text = pyperclip.paste()


lines = text.strip('\n')

   
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)

pyperclip.copy()