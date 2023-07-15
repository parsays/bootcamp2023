class Payment:
    def __init__(self, value):
        self.value= value
    
    def bind(self, func):
        return func(self.value)
        