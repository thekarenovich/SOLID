# Принцип открытости/закрытости

from enum import Enum
from abc import ABCMeta, abstractmethod

# class Products(Enum):
#   SHIRT = 1
#   TSHIRT = 2
#   PANT = 3

# class DiscountCalculator():
#   def __init__(self, product_type, cost):
#     self.product_type = product_type
#     self.cost = cost

#   def get_discounted_price(self):
#     if self.product_type == Products.SHIRT:
#       return self.cost - (self.cost * 0.10)
#     elif self.product_type == Products.TSHIRT:
#       return self.cost - (self.cost * 0.15)
#     elif self.product_type == Products.PANT:
#       return self.cost - (self.cost * 0.25)

class DiscountCalculator():

  @abstractmethod
  def get_discounted_price(self):
    pass

class DiscountCalculatorShirt(DiscountCalculator):
  def __init__(self, cost):
    self.cost = cost

  def get_discounted_price(self):
      return self.cost - (self.cost * 0.10)

class DiscountCalculatorTshirt(DiscountCalculator):
  def __init__(self, cost):
    self.cost = cost

  def get_discounted_price(self):
      return self.cost - (self.cost * 0.15)

class DiscountCalculatorPant(DiscountCalculator):
  def __init__(self, cost):
    self.cost = cost

  def get_discounted_price(self):
      return self.cost - (self.cost * 0.25)

# dc_Shirt = DiscountCalculatorShirt(100)
# print(dc_Shirt.get_discounted_price())
# dc_TShirt = DiscountCalculatorTshirt(100)
# print(dc_TShirt.get_discounted_price())
# dc_Pant = DiscountCalculatorPant(100)
# print(dc_Pant.get_discounted_price())
