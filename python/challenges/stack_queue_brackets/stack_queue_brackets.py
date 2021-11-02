def validate_brackets(input):
    open=['(','{','[']
    close=[')','}',']']
    brackets=[]
    if len(input)==0:
        return 'please insert a validate input'
    for i in input:
        if i in open:
            brackets.append(i)
        elif i in close:
            index=close.index(i)
            if len(brackets)==0 or open[index] not in brackets:
                return False
            else:
                brackets.pop()
    
    if len(brackets)==0:
        return True
    return False

if __name__=='__main__':
    
    print(validate_brackets('[({})]'))
