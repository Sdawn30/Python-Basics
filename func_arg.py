#Basic function with one argument

def hello_world(greeting):
    return '{} Function'.format(greeting)

print(hello_world('GM!'))


# function with multiple argument if nothing pass as value in arg, default will take place.

def hello_func_withdefault(greeting, name='Sumi'):
    return '{}, {}'.format(greeting, name)

print(hello_func_withdefault('Hi'))

def without_Default(greeting,name='sumi'):
    return '{},{}'.format(greeting,name)

print(without_Default('Hi','kuchi'))
