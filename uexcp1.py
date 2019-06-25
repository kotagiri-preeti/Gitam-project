class abc(ZeroDivisionError):
    def __init__(self,args):
    #def __init__(self,args):
        self.args=args
try:
    raise abc("hello")
  #  raise TypeError("hello")
except abc as a:
    print(a.args)