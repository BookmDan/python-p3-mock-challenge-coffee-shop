class Coffee:
  def __init__(self, name):
    self.name = name 
    self._orders = []
    self._customers = []


  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, name):
    if type(name )== str and len(name) > 2 and not hasattr(self,"name"):
      self._name = name
    else: 
      raise Exception("Name must be a string greater than 2 characters ")
    
  def orders(self ):
    return self._orders

  def customers(self):
    return list(set(self._customers))

  def num_order(self):
    return len(self._orders)

  def average_price(self):
    # return sum([order.plrice for order in self._orders]) / len(self._orders)
  
    total_price = 0 

    for order in self._orders:
      # print(order)
      total_price = total_price + order.price 

    avg = total_price / len(self._orders)
    return avg 