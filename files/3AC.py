def inf_pos(exp):
    operators = ['+', '-', '*', '/', '(', ')']
    precedance = {'+':1, '-':1, '*':2, '/':2}
    postfix = ""
    stack = []
    
    for i in exp:
        print(f"stack: {stack} postfix: {postfix}")
        if i not in operators:
            postfix = postfix+i
        if i in operators:
            if len(stack)==0 or stack[-1]=="(":
                stack.append(i)
            elif i == '(':
                stack.append(i)
            elif i == ')':
                while stack and stack[-1] != '(':
                    postfix += stack.pop()
                    stack.pop() # pop '('
            else: 
                while(precedance[stack[-1]] >= precedance[i] or stack[-1] == ')'):
                    postfix = postfix+stack[-1]
                    stack.pop(-1)
                    if len(stack) == 0:
                        break
                stack.append(i)

    for item in stack:
        print(f"stack: {stack} postfix: {postfix}")
        if item == '(' or item == ')':
            pass
        else:
            postfix = postfix+item
            
    print(postfix)      
    return postfix


def generate3AC(pos):
	print("### THREE ADDRESS CODE GENERATION ###")
	exp_stack = []
	t = 1
	op = []
	for i in pos:
		print(exp_stack)
		if i not in operators:
			exp_stack.append(i)
		else:
			print(f't{t} := {exp_stack[-2]} {i} {exp_stack[-1]}')
			op.append((f't{t} := {exp_stack[-2]} {i} {exp_stack[-1]}'))
			exp_stack=exp_stack[:-2]
			exp_stack.append(f't{t}')
			t+=1
	return op

            
def main():
    exp = input("enter expression without spac: ")
    pos = inf_pos(exp)
    print(generate3AC(pos))
    
main()