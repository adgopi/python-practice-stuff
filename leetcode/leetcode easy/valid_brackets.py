class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets_map = { '}' : '{' , ']' : '[', ')' : '(' }
        for char in s:
            if char in brackets_map:
                if len(stack) == 0 or stack.pop() != brackets_map[char]:
                    return False
            else:        
                stack.append(char)
        return not stack

print( Solution.isValid('', '()') )             #true
print( Solution.isValid('', '()()[][]{}{}') )   #true
print( Solution.isValid('', '([{}])') )         #true
print( Solution.isValid('', '(){[}]') )         #false
print( Solution.isValid('', '{]') )             #false
print( Solution.isValid('', '{') )              #false
print( Solution.isValid('', '}') )              #false
