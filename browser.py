import sys
import os
import requests
from colorama import init, Fore, Style
from bs4 import BeautifulSoup

# requests
user_agent = 'Mozilla/5.0'
# colorama initialize
init()
# cmd operations and make dir
args = sys.argv
dir_name = args[1]
os.makedirs(f'{dir_name}', exist_ok=True)
incomplete_p = f'D:/Hanshin/Python FLAG/Text-Based Browser/Text-Based Browser/task/{dir_name}/'

tabs = []
stack = ['head']

while True:
    choice = input()
    # back and exit case
    if choice == 'back':
        if stack[-1] != 'head':
            stack.pop()
            choice = stack.pop()
        else:
            continue
    elif choice == 'exit':
        break
    # if file exist
    file_name = choice[:choice.rfind(".")]
    complete_p = os.path.join(incomplete_p, f'{file_name}')
    if file_name in tabs:
        with open(complete_p, 'r') as file:
            print(file.read())
    # if file doesnt
    else:
        text = []
        target_tags = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'ol', 'li']
        if not choice.startswith('https://'):
            choice = 'https://' + choice
        try:
            r = requests.get(choice)
        except requests.exceptions.ConnectionError:
            print('Error: Incorrect URL\n')
            continue
        soup = BeautifulSoup(r.content, 'lxml')
        complete_p = os.path.join(incomplete_p, f'{file_name}')
        with open(complete_p, 'w', encoding='utf-8') as file:
            for i in soup.find_all(target_tags):
                k = (i.text.strip()).replace('\n', '')
                if i.name != 'a':   # if its a link
                    k = Fore.BLUE + k
                print(k)
                file.write(k + '\n')
                print(Style.RESET_ALL)
        stack.append(file_name)
        tabs.append(file_name)
        print(tabs)
