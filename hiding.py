class JustCounter:
    __secretCount = 0 #strongly private
    _a=10 #private
  
    def count(self):
        self.__secretCount += 1
        print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print(JustCounter._a)
print(counter._JustCounter__secretCount,counter._a)