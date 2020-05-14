file = open('assets/spam.txt')
global contents
contents = file.read()

word_list = list()
stop = 0

for x in range(contents.count('{')):
  start = contents.find('{', stop)
  stop = contents.find('}', start)
  word = contents[start : stop +1]
  word_list.append(word)

mad_lib = str()

for x in word_list:
  user_input = input('Give me a/n' + x + ':')
  print(user_input)
  contents = contents.replace(x, user_input, 1)
  print(mad_lib)

def print_welcome():
  print('Madlibs: Make Me A Video Game!')
  #print welcome and instructions
  # -print- console, maybe -return- to file?

def read_template():
  pass 
  #read and parse file
  
  # f'string' 

def prompt_input():
  pass
  #propt user for adjective words

def populate_template():
  pass
  #insert user input into template

  # text.format('user', 'input', 'string')

def print_response():
  print('Your Madlib is complete!')

def new_file():
  pass

