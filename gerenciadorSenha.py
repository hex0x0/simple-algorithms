#!python3

#pw.py - um programa para repositório de senha que não é seguro
import sys, pyperclip

passwords = {'email':'dsfjlkdsfudsrjewru7ewyrw', 'blog':'fshjdfjadsfdsa', 'luggage':2324}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] = copy account password')
    sys.exit()


account = sys.argv[1]

if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password for ' + account + 'copied to clipboard')
else:
    print('There is no account named ' + account)



print(passwords)


