class AddOperation:
    def __init__(self, list=[]):
        self.list=list
    
    def prt(self):
        return (str(self.list))

    def for_method(self, list):
        count = 0
        print('\n>>> Add Operation by FOR method Process,\n')
        for item in self.list:
            print(' %i + %i = %i' % (count, item, (count+item)))
            count += item
        print('\n>>> %i\nThe Sum is equal to %i\n' % (count, count))


list = [3, 7, 14, 20, 31, 44, 57, 60, 78, 86, 98, -3, 56, 2, -103]
a = AddOperation(list)
print(a.prt())


a.for_method(a)
