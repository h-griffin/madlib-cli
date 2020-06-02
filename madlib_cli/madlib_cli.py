# file = open('assets/spam.txt')
# global contents
# contents = file.read()

from textwrap import dedent

def print_welcome():
      print(dedent(f"""
        {"*"*40}
        *** Welcome to Lab-03 Matlib Project ***
        {"*"*40}
        ******         How To Play        ******
        * There will be a series of questions  *
        * asked, please reply to each question *
        * and after the series is complete a   * 
        * result will be populated for you     *
        {"*"*40}
        """)) 

# search for assets/spam.txt and grab {values}
def read_template():
    """searches assets folder for template and extract {}"""
    with open('assets/spam.txt') as contents:
        contents = contents.read()
        word_list = list()
        stop = 0

    for i in range(contents.count('{')):
        start = contents.find('{', stop) + 1
        stop = contents.find('}', start)
        word = contents[start : stop ]
        word_list.append(word)
    return word_list
 
# mad_lib = str()

def prompt_input(word_list):
    """takes user input for each {} extracted from template"""
    input_list = list()
    for i in word_list:
        user_input = input(f"Please provide a(n) {i}: ")
        input_list.append(user_input)

    return input_list

def populate_template(input_list):
    """populates template with user input"""
    with open("./assets/madlib_template.txt") as template:
        content = template.read()

    repetitions = content.count("{")
    for i in range(repetitions):
        start = content.find("{", 0)
        end = content.find("}", 0) + 1
        content = content[:start] + input_list[i] + content[end:]
    return content

def new_file(data):
    """saves template with user inputs to a new file"""
    with open("./assets/saved_data.txt", "a") as f:
        f.write(data)

if __name__ == "__main__":
    print_welcome()
    keys = read_template()
    input_list = prompt_input(keys)
    rendered = populate_template(input_list)
    print(rendered)
    new_file("\n\n" + rendered)
