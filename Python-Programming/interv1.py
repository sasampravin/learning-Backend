import re

print("we use re module")
for me in re.finditer("4*","334444333121122344"):
    print("si={} ei={} val={}".format(me.start(),me.end(),me.group()))
mat=re.finditer("\S+4\S+","334444333121122344")
for me in mat:
    print("value={}".format(me.group()))
