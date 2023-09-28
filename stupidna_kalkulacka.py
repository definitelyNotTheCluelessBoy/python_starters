class Stack:
    def __init__(self):
        self.__items=[]
    def push(self,value):
        self.__items.append(value)
    def pop(self):
        return self.__items.pop()
    def lenght(self):
        return len(self.__items)
    def reset(self):
        self.__items=[]
    def check(self):
        return self.__items[-1]

class InToPos:
    def __init__(self,exp):
        self.__op_stack=Stack()
        self.output=[]
        self.exp=exp
    def transform(self):
        temp= self.exp.split(' ')
        prior={'(':0,')':0,'*':2,'/':2,'+':1,'-':1}
        for i in temp:
            if i.isdigit():
                self.output.append(i)
            elif i =='(':
                self.__op_stack.push(i)
            elif i ==')':
                while self.__op_stack.lenght() >0 and self.__op_stack.check()!='(':
                    self.output.append(self.__op_stack.pop())
                if self.__op_stack.lenght()!=0:
                    self.__op_stack.pop()
            elif i in '+-*/':
                while self.__op_stack.lenght() >0 and prior[self.__op_stack.check()] >= prior[i]:
                    self.output.append(self.__op_stack.pop())
                self.__op_stack.push(i)
        while self.__op_stack.lenght() > 0:
            self.output.append(self.__op_stack.pop())
        return self.output

class QiucMafs:
    def __init__(self,priklad):
        self.priklad=priklad
        self.stack = Stack()
    def letsgo(self):
        for i in self.priklad:
            if i.isdigit():
                self.stack.push(i)
            else:
                b=float(self.stack.pop())
                a=float(self.stack.pop())
                if i == '+':
                    self.stack.push((a+b))
                elif i == '-':
                    self.stack.push((a-b))
                elif i == '/':
                    self.stack.push((a/b))
                elif i == '*':
                    self.stack.push((a*b))
        return self.stack.pop()

stack=Stack()
ahoj = InToPos("12 * ( 57 + ( 33 / 23 ) * 4 ) - 1213 / 3 + 7")
print(ahoj.transform())
mafs = QiucMafs(ahoj.transform())
print(mafs.letsgo())
print(stack.lenght())