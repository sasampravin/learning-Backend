import gc
print('program starts')
print('\nis gc enable in third line :',gc.isenabled())
print("it's time to test gc is enabled or not")
gc.disable()
print('\nis gc enable after disabling :',gc.isenabled())
print('python program is going on executing')
