class Human:
    def __init__(self, name, age, phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number

    def __str__(self):
        return self.name + "," + str(self.age) + "," + self.phone_number

    def __eq__(self, other):
        return (self.name == other.name) and (self.phone_number == other.phone_number)

    def __hash__(self):
        return hash(self.name + str(self.age) + self.phone_number)

    def __bool__(self):
        return True if self.age >= 20 else False

    def __len__(self):
        return len(self.name)


man = Human("Taro", 20, "0901111111")
man2 = Human("micheal", 18, "0901111111")
man3 = Human("Kimitoshi", 18, "0801111111")
man_str = str(man)
print(man_str)

print(man == man2)
set_men = {man, man2, man3}
dict_a = {}
dict_a[man] = "BB"
dict_a[man2] = "BB"
print(dict_a.keys())
for x in set_men:
    print(x)
# print(hash("Taro"))
# print(hash("Taro"))
# print(hash("Jiro"))

if man:
    print("manはTrue")
if man2:
    print("man2はTrue")

print(len(man))
print(len(man2))
