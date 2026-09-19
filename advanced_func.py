#args and kwargs 
# args --> when we print prints values from our list 
# kwargs -->  when we print prints values from our dictionary

def student_inf(*args,**kwargs):
   print(args)
   print(kwargs)


courses = ['CN', 'OS' , 'OOPS']
info = {'name':'sumi', 'age':30}


student_inf(courses, info) # not a correct one
student_inf(*courses,**info)
