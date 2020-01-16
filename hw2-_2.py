#Создаем базовый класс животных

import random

class Animal: 
    """Базовый класс домашних животных"""

    animal_count = 0
    animal_hunger = 0
    resourse_complit = 0

    def __init__(self, animal_name, animal_voice, animal_type, animal_resource):

        self.animal_resource = animal_resource
        self.animal_type = animal_type
        self.animal_voice = animal_voice
        self.animal_name = animal_name
        self.animal_hunger = random.randint(False, True)
        self.resourse_complit = random.randint(0, 5)
        Animal.animal_count += 1
        

    def feed(self):

        if self.animal_hunger:
            return f'{self.animal_type} {self.animal_name} насытился и говорит {self.animal_voice}'
        
        else:
            return f'{self.animal_type} {self.animal_name} пока не хочет есть'

    def farm(self):

        if self.resourse_complit > 0:
            return f'{self.resourse_complit} единиц {self.animal_resource} получено от {self.animal_type} {self.animal_name}'
    
    def display_count(self):

        return f'\nВсего животных на ферме: {Animal.animal_count}\n'

#На основе родительского класса создаем подклассы животных по виду ресурса

class Dairy(Animal):
    """Подкласс молочных животных"""
    
    def farm(self):

        if self.resourse_complit > 0:
            return f'{self.resourse_complit} литров {self.animal_resource} надоено с {self.animal_type} {self.animal_name}'
        
        else:
            return f'{self.animal_resource} пока нет у {self.animal_type} {self.animal_name}'

class Woolen(Animal):
    """Подкласс шерстяных животных"""

    def farm(self):

        if self.resourse_complit > 0:
            return f'{100*self.resourse_complit} грамм {self.animal_resource} настрижено с {self.animal_type} {self.animal_name}'
        
        else:
            return f'{self.animal_resource} пока нет у {self.animal_type} {self.animal_name}'


class Egg(Animal):
    """Подкласс яичных животных"""
    def farm(self):

        if self.resourse_complit > 0:
            return f'{self.resourse_complit} штук {self.animal_resource} получено от {self.animal_type} {self.animal_name}'
        
        else:
            return f'{self.animal_resource} пока нет у {self.animal_type} {self.animal_name}'

## На основе имеющихся подклассов создаем подклассы по виду животных

animals = {'Goose': [['Серый', 'Белый'], 'яйцо', 'Га-га', 'Гусь', [5, 8]], 
          'Cow': [['Манька'],'молоко', 'Мму-мму', 'Корова', [350, 500]], 
          'Sheep': [['Барашек', 'Кудрявый'], 'шерсть', 'Бе-бе', 'Овца', [25, 70]], 
          'Chicken': [['Ко-Ко', 'Кукареку'], 'яйцо', 'Ко-ко-ко', 'Курица', [1, 3]], 
          'Goat': [['Рога', 'Копыта'], 'молоко', 'Ме-ме', 'Коза', [30, 55]],
          'Duck': [['Кряква'], 'яйцо', 'Кря-кря', 'Утка', [3, 5]],
          'Horse': [['Лошадка', 'Пони', 'Коняшка', 'Рохля'], 'молоко', 'Иго-го', 'Лошадь', [250, 400]],
          'Bee': [['Майя'], 'мед', 'Жжжжж', 'Пчела', [1, 2]]}

def class_creator(name, parent, class_attr1, class_attr2, class_attr3):

    if class_attr3 == 'молоко':
        parent = Dairy
    
    elif class_attr3 == 'шерсть':
        parent = Woolen

    elif class_attr3 == 'яйцо':
        parent = Egg

    else:
        parent = Animal

    class New_class(parent):
        pass
        def __init__(self, animal_name):
            super().__init__(animal_name, class_attr1, class_attr2, class_attr3)
    
    New_class.__name__ = name
    
    return New_class

for variety in animals.items():

    animals[variety[0]].append(class_creator(variety[0], Dairy, variety[1][2], variety[1][3], variety[1][1]))
        
pet = {}

# На основе имеющихся подклассов создаем экземпляры каждого животно

for variety in animals.items():
   for individual in variety[1][0]:
      pet[individual]=[variety[1][5](individual), variety[0]]

#Получаем список животных на ферме:

for individual in pet.items():
    print(f'Вид животного:{individual[1][0].animal_type} Имя животного:{individual[1][0].animal_name}')

print(pet['Серый'][0].display_count())

#Собираем полезные ресурсы:

for individual in pet.items():
    print(individual[1][0].farm())

#Кормим животных и слушаем их голоса:

for individual in pet.items():
    print(individual[1][0].feed())

#Введем параметр веса животного

class Animal_with_weight(Animal):

    sum_animal_weight = 0
    max_animal_weight = 0
    max_weight_type = 0
    max_weight_name = 0

    def __init__(self, animal_name, animal_voice, animal_type, animal_resource, animal_weight):
        super().__init__(animal_name, animal_voice, animal_type, animal_resource)
        self.animal_weight = animal_weight
        Animal_with_weight.sum_animal_weight += self.animal_weight
        
        if Animal_with_weight.max_animal_weight < self.animal_weight:
            Animal_with_weight.max_animal_weight = self.animal_weight
            Animal_with_weight.max_weight_type = self.animal_type
            Animal_with_weight.max_weight_name = self.animal_name
            

    def display_sum_weight(self):

        return f'\nСуммарный вес всех животных: {Animal_with_weight.sum_animal_weight} кг\n'

    def display_max_weight(self):
           
        return f'\nСамое тяжелое животное на ферме: {Animal_with_weight.max_weight_type} {Animal_with_weight.max_weight_name} весит {Animal_with_weight.max_animal_weight} кг\n'


pet_with_weight = []

Animal.animal_count = 0

#Создадим экземпляры животных на основе вновь созданного класса

for variety in pet.items():
      
      pet_with_weight.append(Animal_with_weight(variety[1][0].animal_name, variety[1][0].animal_voice, variety[1][0].animal_type, variety[1][0].animal_resource, random.randint(animals[variety[1][1]][4][0], animals[variety[1][1]][4][1])))


for individual in pet_with_weight:
    print(f'Вид животного:{individual.animal_type} Имя животного:{individual.animal_name} Вес животного: {individual.animal_weight} кг')

print(pet_with_weight[0].display_count())
print(pet_with_weight[0].display_sum_weight())
print(pet_with_weight[0].display_max_weight())


    