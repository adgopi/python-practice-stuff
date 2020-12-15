class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets_map = { '}' : '{' , ']' : '[', ')' : '(' }
        for char in s:
            try:
                if char in brackets_map:
                    if stack.pop() != brackets_map[char]:
                        return False
                else:        
                    stack.append(char)
            except:
                return False
        return len(stack) == 0

print( Solution.isValid('', '()') )             #true
print( Solution.isValid('', '()()[][]{}{}') )   #true
print( Solution.isValid('', '([{}])') )         #true
print( Solution.isValid('', '(){[}]') )         #false
print( Solution.isValid('', '{]') )             #false
print( Solution.isValid('', '{') )              #false
print( Solution.isValid('', '}') )              #false
