class Order:
  def __init__(self, id, nazwa, cena):
    self.id = id
    self.nazwa = nazwa
    self.cena = cena

class Manager:
  orders = {}
  def add_new_order(self, nazwa, cena, stan):
    is_on_list = False
    if self.orders:
      for order in self.orders:
        if order.nazwa==nazwa:
          self.orders[order] +=stan
          is_on_list = True
          print(f'Stan produktu o nazwie {nazwa} został powiększony o {stan}')
    if not is_on_list:
   
      self.orders.update({Order(len(self.orders), nazwa, cena) : stan})
      print(f'Dodano nowy produkt o nazwie {nazwa}')

  def reduce_stock(self, id):
    for order in self.orders:
      if order.id == id:
        if self.orders[order]:
          self.orders[order] -= 1
          print(f'Stan magazynu: {self.orders[order]} dla produktu {order.nazwa}')
        else: print(f'Stan magazynu = 0 dla produktu {order.nazwa}')

def main():
  manager1 = Manager()
  manager1.add_new_order('lodówka', 2340.44, 0 )
  manager1.add_new_order('tv', 2340.44, 0 )
  manager1.reduce_stock(0)



if __name__ == '__main__':
  main()