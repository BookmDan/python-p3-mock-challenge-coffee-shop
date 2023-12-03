class Order: 
  all = []
  def __init__(self, customer, coffee, price):
    self.customer = customer
    self.coffee = coffee
    self.price = price

    self.coffee._orders.append(self)
    self.coffee._customers.append(self.customer)

    self.customer._orders.append(self)
    self.customer._coffees.append(self.coffee)

    Order.all.append(self)


  @property
  def price(self):
    return self._price
  
  @price.setter
  def price(self, price):
    if type(price)== float and 1.0 <= price <= 10.0 and not hasattr(self, "price"):
      self._price = price 
    else :
      raise Exception("Price must be a float between 1 and 10!")
    
    @property
    def customer(self):
      return self._customer
    
    @customer.setter
    def customer(self,customer):
      from classes.Customer import Customer
      if isinstance(customer, Customer):
        self._customer = customer
      else: 
        raise Exception("Customer must be instance of class Customer!")
      
    @property
    def coffee(self):
      return self._coffee
    
    @coffee.setter
    def coffee(self, coffee):
      from classes.Coffee import Coffee
      if isinstance(coffee, Coffee):
        self._coffee = coffee
      else: 
        raise Exception("Coffee must be instance of class Coffee")
