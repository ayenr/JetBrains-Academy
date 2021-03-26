help_ = """Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line
Special commands: !help !done"""


def plain():
    text = input("- Text: ")
    return text


def bold():
    return f"**{plain()}**"


def italic():
    return f"*{plain()}*"


def inline_code():
    return f"`{plain()}`"


def header():

    level = int(input('- Level:'))

    if level <= 0 or level > 6:
        return "The level should be within the range of 1 to 6"

    else:
        text = plain()
        return f"{'#' * level} {text}\n"


def link():

    label = input('- Label:')
    url = input('- URL:')

    return f'[{label}]({url})'


def new_line():
    return '\n'


def ordered_list():

    lst = ""

    while True:
        rows = int(input("- Number of rows: "))
        if rows <= 0:
            print('The number of rows should be greater than zero')
        else:
            break
            
    for r in range(1, rows + 1):
        rs = input(f'- Row #{r}: ')
        lst += f'{r}. {rs}\n'

    return lst


def unordered_list():
    lst = ""

    while True:
        rows = int(input("- Number of rows: "))
        if rows <= 0:
            print('The number of rows should be greater than zero')
        else:
            break

    for r in range(1, rows + 1):
        rs = input(f'- Row #{r}: ')
        lst += f'* {rs}\n'

    return lst


formatter = {"plain": plain,
             "bold": bold,
             "italic": italic,
             "header": header,
             "link": link,
             "inline-code": inline_code,
             "ordered-list": ordered_list,
             "unordered-list": unordered_list,
             "new-line": new_line}

edited = ''

while True:
    user_input = input("- Choose a formatter: ")

    if user_input.lower() in formatter:
        edit = formatter[user_input.lower()]()
        edited += edit
        print(edited)

    elif user_input == '!help':
        print(help_)
    elif user_input == '!done':
        doc = open('output.md', 'w')
        doc.write(edited)
        doc.close()
        break
    else:
        print('Unknown formatting type or command')
