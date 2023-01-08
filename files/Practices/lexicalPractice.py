import re

f = open('inputprog.c', 'r')

operators = { '=': 'Assignment Operartor', '+': 'Addition Operator', '-': 'Substraction Operator', '/': 'Division Operator', '*': 'Multiplication Operator', '++': 'Increment Operator', '--': 'Decrement Operator'}
optr_keys = operators.keys()

comment = { r'//': 'Single line comment', r'/*': 'Multiline line comment start', r'*/': 'Multiline line comment end', '/**/': 'Empty line comment'}
comment_keys = comment.keys()

header = {'.h': 'Header files'}
header.keys()

sp_header_file = {'<Studio.h>': 'Standard Input Output Header', '<String.h>': 'Standard Maniputlation Library'}

macros = { r'#\w+': 'Macro'}
macro_keys = macros.keys()

datatypes = {'int': 'Integer', 'float': 'Floating point', 'char': 'character', 'long': 'Long int'}
datatype_keys = datatypes.keys()

keywords = {'return': 'return a value from block'}
keyword_keys = keywords.keys()

delimeter = {';': 'Terminator symbol semicolon (;)'}
delimeter_keys = delimeter.keys()

blocks = { '{': 'Blocked statement body open', '}': 'Blocked statement body closed'}
blocks_key = blocks.keys()

builtin_functions = {'printf': 'printf prints the output in console'}

non_identifiers = ['~' ,'`' ,'@' ,'#' ,'$' ,'%' ,'^' ,'&' ,'*' ,'(' ,')' ,'_' ,'-' ,'+' ,'+' ,'[' ,'{' ,'}' ,']' ,'"' ,':' 
,';' ,'<' ,',' ,'>' ,'. ','?' ,'/' ,'|' ]

numerals = ['0','1','2','3','4','5','6','7','8','9','10']

#Flags
dataFlag = False

i = f.read()

count = 0
program = i.split('\n')

for line in program:
    count = count+1
    print('Line #', count, '\n', line)

    tokens = line.split(' ')
    print('Tokens are', tokens)
    print('Line #', count, 'Properties \n')

    for token in tokens:
        if '\r' in token:
            position = token.find('\r')
            token = token[:position]
        
        if token in blocks_key:
            print(blocks[token])
        if token in optr_keys:
            print("Operator is: ", operators[token])
        if token in comment_keys:
            print("Comments types: ", comment[token])
        if token in macros:
            print('Macro is: ', macros[token])
        if '.h' in token:
            print('Header File is: ',token, sp_header_file[token])
        if '()' in token:
            print("Function named", token)
            
        if dataFlag == True and (token not in non_identifiers) and ('()' not in token):
            print('Identifier: ', token)
        if token in datatype_keys:
            print("type is: ", datatypes[token])
            dataFlag = True
        
        if token in keyword_keys:
            print(keywords[token])
        
        if token in delimeter:
            print("Delimiter ", delimeter[token])
        if '#' in token:
            mat





