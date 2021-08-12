#zadanie 1

class Student:
  def __init__(self, name, surname, filed_of_study, year):
    self.name = name
    self.surname = surname
    self.field_of_study = filed_of_study
    self.year = year
  def printData(self):
    print(f'{self.name} {self.surname} uczęszcza na studia o kierunku {self.field_of_study} i jest na {self.year} roku')

#zadanie 2
class Vehicle:
  def __init__(self, max_speed, car_mileage):
    self.max_speed = max_speed
    self.car_mileage = car_mileage
  def increase_car_mileage(self, mileage):
    self.car_mileage += mileage

#zadanie 3
class Rectangle:
  def __init__(self, a, b):
    self.a = a
    self.b = b
  def calculate_area(self):
    return self.a * self.b
  def calculate_perimeter(self):
    return 2*self.a + 2*self.b



def main():
  #zadanie 1
  student1 = Student('Kasia', 'Nowak', 'Psychologia', 4)
  student1.printData()

  #zadanie 2
  vehicle1 =Vehicle(150, 10000)
  vehicle1.increase_car_mileage(40.5555)
  # print(vehicle1.car_mileage)

  #zadanie 3
  rectangle1 = Rectangle(1,2)
  print (f'Pole: {rectangle1.calculate_area()} obwód:{rectangle1.calculate_perimeter()} ')




if __name__ == '__main__':
  main()