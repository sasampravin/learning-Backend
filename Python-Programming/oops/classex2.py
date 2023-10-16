class studentinfo:
    course='python'
    course2='plsql'

s1=studentinfo()
s2=studentinfo()

s1.sno=100
s1.name='sad'
s1.marks=78.42
s2.sno=111
s2.name='sun'
s2.marks=89.79
s2.clg='dac'

print('s1 obj details as follows:')
print('student no:',s1.sno)
print('student name: ',s1.name)
print('student marks: ',s1.marks)
print('course1 : ',s1.course)
print('course2 : ',studentinfo.course2)
print('\n s2 obj details asfollowes:')
print('student no: ',s2.sno)
print('student name: ',s2.name)
print('student marks: ',s2.marks)
print('student college: ',s2.clg)
print('course1 : ',studentinfo.course)
print('course2 : ',s2.course2)
