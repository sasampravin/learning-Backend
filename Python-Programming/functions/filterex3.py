line=input("Enter a line text:")
print("given line of text=",line)
vlist=list(filter(lambda ch: ch in ['a','e','i','o','u','A','E','I','U','O'],line))
clist=tuple(filter(lambda ch: ch not in ['a','e','i','o','u','A','E','I','U','O'] and ch.isalpha(),line))
dlist=list(filter(lambda ch: ch.isdigit(),line))
slist=list(filter(lambda ch: not(ch.isalpha()) and not(ch.isdigit()),line))
print("Vowels list=",vlist)
print("consonent list=",clist)
print("digit list=",dlist)
print("special symble list=",slist)