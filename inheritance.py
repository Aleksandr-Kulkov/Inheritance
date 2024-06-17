from cat import Cat

cat1 = Cat("Барон", "мальчик", 2)

print("Имя cat1 -", cat1.name)
print("Пол cat1 -", cat1.gender)
print("Возраст cat1 -", cat1.age)

print("Количество лап cat1 -", cat1.count_of_paws)

print("Имя cat1 -", cat1.getName())
print("Пол cat1 -", cat1.getGender())
print("Возраст cat1 -", cat1.getAge())

cat2 = Cat("Муська", "девочка", 3)

print("Имя cat2 -", cat2.name)
print("Пол cat2 -", cat2.gender)
print("Возраст cat2 -", cat2.age)

print("Количество лап cat2 -", cat1.count_of_paws)

print("Имя cat2 -", cat2.getName())
print("Пол cat2 -", cat2.getGender())
print("Возраст cat2 -", cat2.getAge())
