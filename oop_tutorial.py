"""
OBJECT-ORIENTED PROGRAMMING (OOP) TUTORIAL
==========================================
A beginner-friendly guide to understanding OOP concepts with practical examples.
"""

# ============================================================================
# 1. CLASSES AND OBJECTS
# ============================================================================
"""
WHAT IS A CLASS?
- A class is like a blueprint or template for creating objects
- Think of it like a cookie cutter - it defines the shape and properties

WHAT IS AN OBJECT?
- An object is an instance (actual copy) created from a class
- Think of it like the actual cookie made from the cookie cutter
"""

class Dog:
    """A simple class representing a Dog"""
    
    # __init__ is a special method called a "constructor"
    # It runs automatically when you create a new Dog object
    def __init__(self, name, age, breed):
        # 'self' refers to the specific object being created
        # These are called "attributes" or "properties"
        self.name = name
        self.age = age
        self.breed = breed
    
    # This is a "method" - a function that belongs to the class
    def bark(self):
        return f"{self.name} says: Woof! Woof!"
    
    def get_info(self):
        return f"{self.name} is a {self.age}-year-old {self.breed}"


# Creating objects (instances) from the Dog class
print("=" * 60)
print("1. CLASSES AND OBJECTS EXAMPLE")
print("=" * 60)

dog1 = Dog("Buddy", 3, "Golden Retriever")
dog2 = Dog("Max", 5, "German Shepherd")

print(dog1.get_info())  # Buddy is a 3-year-old Golden Retriever
print(dog1.bark())      # Buddy says: Woof! Woof!
print()
print(dog2.get_info())  # Max is a 5-year-old German Shepherd
print(dog2.bark())      # Max says: Woof! Woof!
print()


# ============================================================================
# 2. INHERITANCE
# ============================================================================
"""
WHAT IS INHERITANCE?
- Inheritance allows a class to inherit properties and methods from another class
- The "parent class" (or "base class") is the class being inherited from
- The "child class" (or "derived class") is the class that inherits
- Think of it like a child inheriting traits from their parents
"""

class Animal:
    """Parent class - represents any animal"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        return f"{self.name} is eating"
    
    def sleep(self):
        return f"{self.name} is sleeping"


class Cat(Animal):
    """Child class - inherits from Animal"""
    
    def __init__(self, name, age, color):
        # Call the parent class constructor using super()
        super().__init__(name, age)
        self.color = color  # Additional attribute specific to Cat
    
    def meow(self):
        return f"{self.name} says: Meow!"


class Bird(Animal):
    """Another child class - also inherits from Animal"""
    
    def __init__(self, name, age, can_fly):
        super().__init__(name, age)
        self.can_fly = can_fly
    
    def chirp(self):
        return f"{self.name} says: Chirp chirp!"


print("=" * 60)
print("2. INHERITANCE EXAMPLE")
print("=" * 60)

cat = Cat("Whiskers", 2, "Orange")
bird = Bird("Tweety", 1, True)

# Cat and Bird can use methods from Animal class
print(cat.eat())      # Whiskers is eating (inherited from Animal)
print(cat.meow())     # Whiskers says: Meow! (specific to Cat)
print()
print(bird.sleep())   # Tweety is sleeping (inherited from Animal)
print(bird.chirp())   # Tweety says: Chirp chirp! (specific to Bird)
print()


# ============================================================================
# 3. ENCAPSULATION
# ============================================================================
"""
WHAT IS ENCAPSULATION?
- Encapsulation means hiding internal details and protecting data
- We use private attributes (prefix with __) to restrict direct access
- We provide public methods (getters/setters) to control how data is accessed
- Think of it like a capsule - the medicine is protected inside
"""

class BankAccount:
    """Demonstrates encapsulation with private attributes"""
    
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder
        # __ prefix makes this attribute "private"
        self.__balance = initial_balance
    
    # Getter method - allows reading the balance safely
    def get_balance(self):
        return self.__balance
    
    # Method to deposit money with validation
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        else:
            return "Invalid deposit amount"
    
    # Method to withdraw money with validation
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds"


print("=" * 60)
print("3. ENCAPSULATION EXAMPLE")
print("=" * 60)

account = BankAccount("John Doe", 1000)

# We can't directly access __balance (it's private)
# print(account.__balance)  # This would cause an error!

# Instead, we use the public methods
print(f"Current balance: ${account.get_balance()}")
print(account.deposit(500))
print(account.withdraw(200))
print(f"Final balance: ${account.get_balance()}")
print()


# ============================================================================
# 4. POLYMORPHISM
# ============================================================================
"""
WHAT IS POLYMORPHISM?
- Polymorphism means "many forms"
- It allows different classes to have methods with the same name
- Each class can implement the method differently
- Think of it like a "speak" command - dogs bark, cats meow, birds chirp
"""

class Shape:
    """Parent class for all shapes"""

    def __init__(self, name):
        self.name = name

    def area(self):
        # This is meant to be overridden by child classes
        pass

    def describe(self):
        return f"I am a {self.name}"


class Rectangle(Shape):
    """Rectangle - implements area() its own way"""

    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    """Circle - implements area() differently"""

    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius


class Triangle(Shape):
    """Triangle - another implementation of area()"""

    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


print("=" * 60)
print("4. POLYMORPHISM EXAMPLE")
print("=" * 60)

# Create different shape objects
shapes = [
    Rectangle(5, 10),
    Circle(7),
    Triangle(6, 8)
]

# Polymorphism in action: same method name, different behavior
for shape in shapes:
    print(f"{shape.describe()}")
    print(f"Area: {shape.area()}")
    print()


# ============================================================================
# 5. PUTTING IT ALL TOGETHER - REAL WORLD EXAMPLE
# ============================================================================
"""
Let's create a simple game character system that uses all OOP concepts!
"""

class GameCharacter:
    """Base class for all game characters (Inheritance)"""

    def __init__(self, name, health):
        self.name = name
        self.__health = health  # Private attribute (Encapsulation)
        self.__max_health = health

    # Encapsulation: getter methods
    def get_health(self):
        return self.__health

    def is_alive(self):
        return self.__health > 0

    # Encapsulation: controlled modification
    def take_damage(self, damage):
        self.__health = max(0, self.__health - damage)
        return f"{self.name} took {damage} damage! Health: {self.__health}/{self.__max_health}"

    def heal(self, amount):
        self.__health = min(self.__max_health, self.__health + amount)
        return f"{self.name} healed {amount}! Health: {self.__health}/{self.__max_health}"

    # Polymorphism: will be overridden by child classes
    def attack(self):
        pass

    def special_ability(self):
        pass


class Warrior(GameCharacter):
    """Warrior class - high damage, melee attacks"""

    def __init__(self, name):
        super().__init__(name, health=150)
        self.attack_power = 25

    def attack(self):
        return f"{self.name} swings sword for {self.attack_power} damage!"

    def special_ability(self):
        return f"{self.name} uses SHIELD BASH - stuns enemy!"


class Mage(GameCharacter):
    """Mage class - magic attacks, lower health"""

    def __init__(self, name):
        super().__init__(name, health=80)
        self.attack_power = 35
        self.__mana = 100

    def attack(self):
        return f"{self.name} casts fireball for {self.attack_power} damage!"

    def special_ability(self):
        if self.__mana >= 50:
            self.__mana -= 50
            return f"{self.name} casts METEOR STORM - massive area damage!"
        return f"{self.name} doesn't have enough mana!"


class Archer(GameCharacter):
    """Archer class - ranged attacks, medium health"""

    def __init__(self, name):
        super().__init__(name, health=100)
        self.attack_power = 20
        self.__arrows = 30

    def attack(self):
        if self.__arrows > 0:
            self.__arrows -= 1
            return f"{self.name} shoots arrow for {self.attack_power} damage! Arrows left: {self.__arrows}"
        return f"{self.name} is out of arrows!"

    def special_ability(self):
        return f"{self.name} uses MULTI-SHOT - hits 3 enemies!"


print("=" * 60)
print("5. COMPLETE EXAMPLE - GAME CHARACTER SYSTEM")
print("=" * 60)

# Create different character types (Objects from Classes)
warrior = Warrior("Conan")
mage = Mage("Gandalf")
archer = Archer("Legolas")

characters = [warrior, mage, archer]

# Demonstrate all OOP concepts together
for character in characters:
    print(f"\n{character.name}'s turn:")
    print(f"Health: {character.get_health()}")
    print(character.attack())  # Polymorphism - same method, different behavior
    print(character.special_ability())  # Polymorphism
    print(character.take_damage(30))  # Encapsulation - controlled access
    print(character.heal(15))  # Encapsulation

print("\n" + "=" * 60)
print("TUTORIAL COMPLETE!")
print("=" * 60)

