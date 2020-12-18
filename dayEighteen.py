from operator import add, mul
from collections import deque 

with open("dayEighteen.txt") as file:
   expressions = [line.strip().replace(" ", "") for line in file]

op_dict = { 
    "*": mul,
    "+": add 
}
precedence = {
    "*" : 1,
    "+" : 1,
    "(" : 0 
}
precedence2 = {
    "*" : 1,
    "+" : 2,
    "(" : 0 
}

# nums = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

nums = {str(i) for i in range(10)}

def get_total(e, precedence, nums, op_dict):
    total_sum = 0 
    for e in expressions:
        n = len(e)
        op_stack = deque()
        num_stack = deque()
        i = 0
        while i < n:
            if e[i] == "(":
                op_stack.append(e[i])

            elif e[i] in nums:
                number  = 0

                # agnostic to whether the number is more than one digit  
                while i < n and e[i] in nums:
                    number  = number  * 10 + int(e[i])
                    i += 1  
                num_stack.append(number)
                i -= 1                      # as i is no longer at a number

            elif e[i] == ")":
                while op_stack and op_stack[-1] != "(":
                    num2 = num_stack.pop()
                    num1 = num_stack.pop()
                    operator = op_stack.pop()
                    op = op_dict[operator]
                    
                    num_stack.append(op(num1, num2))

                # pop the opening bracket 
                op_stack.pop()
            
            # e[i] is * or +  
            # apply op on top of op_stack to top two nums in num_stack while op has same or higher precedence as e[i]
            # there will always be 2 top nums as precedence of (  i set to 0 
            else:
                while op_stack and precedence[op_stack[-1]] >= precedence[e[i]]:
                    num2 = num_stack.pop()
                    num1 = num_stack.pop()
                    operator = op_stack.pop()
                    op = op_dict[operator]
                    
                    num_stack.append(op(num1, num2))    
                op_stack.append(e[i])
            
            i += 1

        while op_stack:
            num2 = num_stack.pop()
            num1 = num_stack.pop()
            operator = op_stack.pop()
            op = op_dict[operator]
                    
            num_stack.append(op(num1, num2))  
        # print(num_stack[-1])
        total_sum += num_stack[-1]

    return total_sum

print(f"q1: {get_total(expressions, precedence, nums, op_dict)}")
print(f"q2: {get_total(expressions, precedence2, nums, op_dict)}")


 
