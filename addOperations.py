class AddOperation:
    def __init__(self, list=[]):
        self.list = list
        self.sum = sum
    
    def prt(self):
        return str(self.list)

    def for_method(self, list):
        sum = 0
        print('\n*** FOR method ***')
        for item in self.list:
            print('%i  +  %i  =  %i' % (sum, item, (sum+item)))
            sum += item
        print('\n*** the sum is: %i\n' % sum)

    def while_method(self, list):
        sum = 0
        i = 0
        print('\n*** WHILE method ***')
        while i < len(self.list):
            print('%i + %i = %i' % (sum, self.list[i], (sum+self.list[i])))
            sum += self.list[i]
            i += 1
        print('\n*** the sum is: %i\n' % sum)











list = [3, 7, 14, 20, 31, 44, 57, 60, 78, 86, 98, -3, 56, 2, -103]
a = AddOperation(list)
print('Operational List: %s' % a.prt())

#a.for_method(list)

a.while_method(list)