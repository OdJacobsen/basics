# Create minimum 4 classes
# Each class contains a few attributes
# Each class has at least one method defining behavior
# Adding vowel checking for string(s)


class Animal:
    type = 'Farm Animal'

    def __init__(self, animal_type, name, lives):
        self.animal_type = animal_type
        self.name = name
        self.lives = lives

    def __str__(self):
        # Checking is first letter of two types of string are vowels or not
        if 'aeoui'.find(
                self.animal_type[0].lower()) != -1 and 'aeoui'.find(
                self.name[0].lower()) != -1:
            article = 'an'
        else:
            article = 'a'

        return f'{article} {self.name} is {article} {self.animal_type} and ' \
            f'lives on the farm and lives in the {self.lives}'

    def feed(self, food):
        if 'aeoui'.find(self.animal_type[0]) != -1:
            article = 'an'
        else:
            article = 'a'

        return f'{article} {self.animal_type} eats {food}'

    # Defined speaker method
    def speak(self, sound):
        return f'{self.name} says {sound}'


class Horse(Animal):
    skin = 'brown'

    def feed(self, food='grass'):
        return super().feed(food)


class Duck(Animal):
    skin = 'feather'

    def speak(self, sound='Quack Quack'):
        return super().speak(sound)


horse = Horse('iorse', 'Albert', 'Stable')
duck = Duck('Duck', 'Thomas', 'Pound')
print(duck.speak())


