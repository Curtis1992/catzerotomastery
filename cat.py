class Cat:
  species = 'mammal'
  def __init__(self, name, age):
      self.name = name
      self.age = age

  cat1 = Cat('cat1', 5)
  cat2 = Cat('Cat2', 7)
  cat3 = Cat('Cat3', 3)


def oldest_cat(*args):
  return max(args)

print(f'Oldest Cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old.')