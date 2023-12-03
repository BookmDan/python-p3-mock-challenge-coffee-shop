class Customer:
  all = []
  def __init__(self, name):
    self.name = name 
    self._orders =[]
    self._coffees = [ ]

    Customer.all.append(self)

  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, name):
    if type(name )== str and 1 <= len(name) <= 15:
      self._name = name
    else: 
      raise Exception("Name must be a string between 1 and 15 characters ")
    
  def orders(self ):
    return self._orders

  def coffees(self):
    return list(set(self._coffees))

  def create_order(self, coffee, price):
    from classes.Order import Order

    new_order = Order(self, coffee, price)
    return new_order

  @classmethod
  def most_aficionado(cls, coffee):
    customer_amount_spend = {}

    for customer in cls.all:
      for order in customer._orders:
        if order.coffee == coffee:
          if customer in customer_amount_spend:
            customer_amount_spend[customer] += order.price 
          else: 
            customer_amount_spend[customer] = order.price 
    if len(customer_amount_spend) == 0:
      return None 
    else: 
      return max(customer_amount_spend, key= customer_amount_spend.get)
