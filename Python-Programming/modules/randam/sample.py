#random.sample(iterable_obj,no.of samples)
import random as r
l=[-1,23,-475,0,98,'python',-89]
t=10,-20,30,300,-400
print(r.sample(l,3))
print(r.sample(t,2))
print(r.sample(l,4))
print(r.sample(l,2))
print(r.sample(t,3))
print(r.sample(l[-2],3))
print(r.sample(l[-2],2))
