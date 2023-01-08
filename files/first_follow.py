def first_follow(grammar, non_terminal, first, follow):
    if non_terminal in first:
        return
    
    first[non_terminal] = set()
    for production in grammar[non_terminal]:
        for symbol in production:
            if symbol in grammar:
                first_follow(grammar, symbol, first, follow)
                first[non_terminal] |= first[symbol]
            else:
                first[non_terminal].add(symbol)
                break
    
    if '' in first[non_terminal]:
        follow[non_terminal] = set()
        for key in grammar:
            for production in grammar[key]:
                if non_terminal in production:
                    index = production.index(non_terminal)
                    if index == len(production) - 1:
                        follow[non_terminal] |= follow[key]
                    else:
                        follow[non_terminal] |= first[production[index+1]]
                        if '' not in first[production[index+1]]:
                            break
        first[non_terminal].remove('')
    else:
        follow[non_terminal] = set()
grammar = {
    'S': ['AB', 'CD'],
    'A': ['a', ''],
    'B': ['b'],
    'C': ['c'],
    'D': ['d']
}

first = {}
follow = {}

for non_terminal in grammar:
    first_follow(grammar, non_terminal, first, follow)

print(first)
print(follow)