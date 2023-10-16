class sample:
    def __init__(self):
        print('\n this is from sample constructor')
class test(sample):
    def __init__(self):
        print('\nthis is fron test constructor')
        super().__init__()
class last(test):
    def __init__(self):
        print('\n this is from last constructor')
        super().__init__()

last()
        
