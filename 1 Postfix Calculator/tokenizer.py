#define lists with the operators and digits
operators  = ['+', '-', '*', '/', '^', '&', '|', 'v']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']

#define a function to tokenize the expression
def tokenize(exp):
    tokens = [] #list to carry all the tokens
    token = ''  #individual token
    number = [] #handling multiple digit numbers
    for i in exp:
        if i in digits: 
            number.append(i)  #Build the number from digits
        elif i not in digits: #Handling spaces
            if i == ' ':
                if len(number) != 0:
                    token = ''.join(number)
                    tokens.append(token)
                    number.clear()
                    token = ''
            elif i  in operators: #Handling operators
                if len(number) != 0:
                    token = ''.join(number)
                    tokens.append(token)
                    number.clear()
                    token = ''
                tokens.append(i)
            else: #Error handling
                print(f"Syntax Error! invalid character: '{i}' not recognized as an operator or digit")
                return 'VOID'
    if len(number) != 0:  # Add any leftover number
        tokens.append(''.join(number))

    return tokens

if __name__ == '__main__':
    a = '1 a 23 65*  87^'
    t = tokenize(a)
    print(t)