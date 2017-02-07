#-*-coding:utf-8 -*-
from flask import Flask

__auther__ = "yagger"

#不带参数的装饰器

def father(fun):
    def kid():
        print("I am kid")
        return fun
    return kid

@father
def test():
    print("I am test")

#带参数的装饰器
def animal(name="dog"):
    def dog(func):
        def littledog(args):
            print("the nama is %s"%name)
            return func(args)
        return littledog
    return dog

@animal("cat")
def t(name):
    print("%s is ok "%(name))

class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print ('class decorator runing')
        self._func()
        print ('class decorator ending')

@Foo
def bar():
    print ('bar')

#当接受的参数不确定时，用*args数组来表示
def func_args(arg, *args):
    print("arg is %s"%arg)
    for i in args:
        print("args is %s"%i)

args = ["dog","cat"]
# func_args("pig", "dog", "cat")
# func_args("pig", *args)

#当接受的参数不确定时，用**kwargs字典来表示
def func_kwargs(arg, *args, **kwargs):
    print("arg is %s"%arg)

    for i in args:
        print("value is %s"%i)

    for i in kwargs:
        print("key is %s,value is %s"%(i,kwargs[i]))

kwargs = {"1":"cat", "2":"dog"}


# func_kwargs("pig",args1="cat",args2="dog")
func_kwargs("pig","aa","bb",**kwargs)