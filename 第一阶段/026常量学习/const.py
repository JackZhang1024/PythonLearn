#coding=GBK
class _const(object):
    class ConstError(TypeError):pass
    def __setattr__(self, name, value):
        if self.__dict__.has_key(name):
           raise self.ConstError,"Can't rebind const(%s)" % name
        self.__dict__[name]=value
    def __delattr__(self, name):
        if name in self.__dict__:
            raise self.ConstError,"Can't unbind const(%s)" % name
        raise NameError,name
#注意是 __name__ 是左右各两个下划线
import sys
sys.modules[__name__]=_const()



