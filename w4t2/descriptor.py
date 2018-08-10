class Value:   
    
    def __set__(self, obj, val):
        self.amount = val - val * obj.commission
        
    def __get__(self, obj, cls):
        return int(self.amount)
    


class Account:
    amount = Value()
    
    def __init__(self, commission):
        self.commission = commission
        
    def get_commission(self):
        return self.commission


new_account = Account(0.2)
new_account.amount = 10

print(new_account.amount)
