from abc import ABCMeta,abstractmethod
class BaseClass(object):
    __metaclass__=ABCMeta

    @abstractmethod
    def printHam(self):
        pass
class InClass(BaseClass):
    def printHam(self):
        print 'ham'
x=InClass()
