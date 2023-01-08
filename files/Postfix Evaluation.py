#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Evaluation rule of a Postfix Expression states


# # While reading the expression from left to right, push the element in the stack if it is an operand.
# Pop the two operands from the stack, if the element is an operator and then evaluate it.
# Push back the result of the evaluation. Repeat it till the end of the expression.
# Algorithm
# 1) Create a stack to store operands (or values).
# 2) Scan the given expression and do following for every scanned element.
# 
#      a) If the element is a number, push it into the stack
#      b) If the element is a operator, pop operands for the operator from stack. Evaluate the operator and push the result back to the stack
# 3) When the expression is ended, the number in the stack is the final answer

# In[5]:


def postfix_evaluation(s):

    s=s.split()

    n=len(s)

    stack =[]

    for i in range(n):

        if s[i].isdigit():

          #append function is equivalent to push

            stack.append(int(s[i]))

        elif s[i]=="+":

            a=stack.pop()

            b=stack.pop()

            stack.append(int(a)+int(b))

        elif s[i]=="*":

            a=stack.pop()

            b=stack.pop()

            stack.append(int(a)*int(b))

        elif s[i]=="/":

            a=stack.pop()

            b=stack.pop()

            stack.append(int(b)/int(a))

        elif s[i]=="-":

            a=stack.pop()

            b=stack.pop()

            stack.append(int(b)-int(a))            

    return stack.pop()

#space separtor is required , for solving 2 or more digits .

s="10 2 8 * + 3 -"

val=postfix_evaluation(s)

print(val)

s="10 5 3 - / 2 6 * +"  # Original expression: 10/(5-3)+2*6

val=postfix_evaluation(s)

print(val)


# In[ ]: