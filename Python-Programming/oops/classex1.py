class studentinfo:pass
s1=studentinfo()
s2=studentinfo()
print('content of s1 obj before adding info :',s1.__dict__)
print('id of s1 obj :',id(s1))
print('length of s1 obj is :',len(s1.__dict__))
s1.sno=111
s1.sname='sadrak'
s1.grade='B+'
s1.clg='arts'

print('\n content of s1 obj after adding the info :',s1.__dict__)
print('id of s1 obj:',id(s1))
print('length of s1 obj is :',len(s1.__dict__))
print('\ncontent of s2 obj before adding info:',s2.__dict__)
print('id of s2 obj :',id(s2))
print('length of s2 obj is :',len(s2.__dict__))
s2.sno=112
s2.sname='sandeep'
s2.grade='A+'

print('\ncontent of s2 obj after adding the info :',s2.__dict__)
print('id of s2 obj :',id(s2))
print('length of s2 obj is :',len(s2.__dict__))
