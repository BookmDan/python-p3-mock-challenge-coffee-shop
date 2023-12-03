class Customer:
  def __init__(self, name):
    self.name = name 
    self._orders =[]
    self._coffees = [ ]

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
    pass