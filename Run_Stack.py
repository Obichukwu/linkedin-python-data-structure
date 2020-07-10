from Stack import Stack

symbol_pair = {
    '{':'}',
    '[':']',
    '(':')'
}
openers = symbol_pair.keys()
def is_balanced(symbol_list):
    int_stack = Stack()
    
    for symbol in symbol_list:
        if int_stack.is_empty():
            int_stack.push(symbol)            
        else:
            if symbol in openers:
                int_stack.push(symbol)                
            else:
                ol = int_stack.pop()               
                if symbol_pair[ol] == symbol:
                    continue
                else:
                    return False
    
    return int_stack.is_empty()

print(is_balanced(['{','}','[',']', '(',')']))

print(is_balanced(['{','[','(',')',']','}']))

print(is_balanced(['{','[',')''(',']','}']))
