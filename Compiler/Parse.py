var = {}
func = {'print': 'string,string2:out string=>out string2'}
run = {}
errorCode = 0


def error(message):
    print("syntax error :", message)


def parse(location):
    error_code = 0
    with open(location, 'r') as f:
        while True:
            word = f.readline()
            if not word: break

            # print(word)

            word = word.split(' ')
            for i in range(len(word)):
                if '\n' in word[i]:
                    word[i] = word[i][:-1]
            for i in range(len(word)):
                try:
                    if word[i] == '=' and word[0] != 'function':
                        string = word[i + 1]
                        for j in range(i + 2, len(word) - 1):
                            if word[j] == '+':
                                string = string + '+' + word[j + 1]
                            if word[j] == '-':
                                string = string + '-' + word[j + 1]
                            if word[j] == '*':
                                string = string + '*' + word[j + 1]
                            if word[j] == '/':
                                string = string + '/' + word[j + 1]
                        var[word[i - 1]] = string
                        break
                    elif word[i] == 'function':
                        if i == 0 and word[i + 2] == '=' and word[i + 3] == '{' and word[len(word) - 1] == '}':
                            string = word[4]
                            for j in range(6, len(word) - 1):
                                if word[j - 1] == '=>':
                                    string = string + '=>' + word[j]
                            func[word[i + 1]] = string
                            break
                        else:
                            error('E1: word connected')
                            error_code = 1
                            break
                    elif word[i] == '/-/':
                        break
                    elif word[i] == 'run':
                        string = word[i + 2]

                        for j in range(i + 3, len(word)):
                            string = string + ' ' + word[j]
                        run[word[i + 1]] = string
                        break
                    elif i != 0:
                        if error_code == 0:
                            error('E0: invalid token')
                            error_code = 1
                            break
                except:
                    if error_code == 0:
                        error('runtime error')
                        error_code = 1
                        break

    if error_code == 1:
        exit('build failed')
    else:
        print('var:', var)
        print('func:', func)
        print('run:', run)
