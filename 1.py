def game():
    progress = True
    word = ['orange']
    lifes = 3

    word_in_play =  get_word(word)
    template = start_template(word_in_play)
    welcome_speech(list_to_string_convert(template))

    while progress:
        user_guess = user_input()
        template = build_template(template, word_in_play, user_guess)
        guessed = list_to_string_convert(template)
        print_result(guessed)
        progress = check_win(guessed)
    
def welcome_speech(t):
    '''
    input: t - template (string)
    output: return None, used as just built-in function print()
    '''
    print(f'''
    Добро пожаловать в игру - hangman 2000!
    Ваша задача - угадать загаданное слово за несколько попыток,
    иначе вас ждет расплата.
    Загаданное словов состоит из {len(t)} букв {t}
    ''')

def start_template(w):
    '''
    input: w - string (word)
    output: replace all chars in string to '_',
            return replaced chars as string  with length w == t
    '''
    t = []
    for i in w:
        t.append('_')
    return t    
        
        

def list_to_string_convert(t):
    '''
    input: t - template (list)
    output: s - list converted to string
    '''
    s = ''
    for i in t:
        s += i
    return s

def get_word(w):
    '''
    input: w - list with strings (words)
    output: for now: first element in list as string
    '''
    return w[0]

def build_template(t, w, g=''):
    """
    input: t - template (list), w - word (string), g - guess (string)
    output: t - template (list) with replaced characters in templade
                if character in word == guess:
                    'character'
                else:
                    '_'
                
    """
    for i in range(len(w)):
        if t[i] == '_':
            if w[i] == g:
                t[i] = w[i]
    return t            
                
def print_result(g):
    """
    input: g - template (string)
    output: return None, used as just built-in function print(g)
    """
    print(f'result: {g}')
    
def user_input():
    """
    output: return str, built-in input() function
    """
    return input('Введите букву')

def check_win(g):
    """
    input: g - template (string)
    output: bool, if no '_' in g retutn False, else True
    """
    for i in g:
         print(i)
  


  

    
game()

