def game():
    progress = True
    word = ['orange']
    lifes = 3

    word_in_play =  get_word(word)
    template = start_template(word_in_play)
    welcome_speech(list_to_string_convert(template))
    
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
    k = ()
    for i in t:
        k = '_' * len(t)
    return k

def get_word(w):
    '''
    input: w - list with strings (words)
    output: for now: first element in list as string
    '''
    return w[0]

    
game()
