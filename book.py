class book:
    def __init__(self, a='malgudi days', b='r.k narayan', c='penguin classic', d='$200'):
        self.title=a
        self.author=b
        self.publisher=c
        self.price=d
    def get_price(self):
        return self.price
    def set_price(self, d):
        self.price=d
        return
    def ShowInfo(self):
        print('title:', self.title)
        print('author:', self.author)
        print('publisher:', self.publisher)
        print('price:', self.price)
    def royality(amount,copies,discount,retailprice):
        amount=(discount*copies*retailprice/100)
        return royality
        copies=1
        discount=10
        retailprice=200
        print("amount:")
        copies=1000
        discount=12.5
        retailprice=200
        print("amount:")
        copies+=1000
        discount=15
        retailprice=200
        print("amount:")
        
        
