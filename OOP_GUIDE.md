# Object-Oriented Programming (OOP) Tutorial

## 📚 What You'll Learn

This tutorial covers the **4 fundamental pillars of OOP**:

1. **Classes and Objects** - The building blocks
2. **Inheritance** - Reusing and extending code
3. **Encapsulation** - Protecting and hiding data
4. **Polymorphism** - Same interface, different behaviors

---

## 📁 Files in This Tutorial

Each concept has its own file with multiple examples:

- **`1.class.py`** - Classes and Objects (Dog & Car examples)
- **`2.inheritance.py`** - Inheritance (Animal, Vehicle, Employee examples)
- **`3.encapsulation.py`** - Encapsulation (Bank Account, User Account, Temperature Sensor)
- **`4.polymorphism.py`** - Polymorphism (Shapes, Animals, Payments, File Handlers)
- **`oop_tutorial.py`** - Complete tutorial with all concepts + Game Character System

---

## 🚀 How to Run

Run each file individually to learn one concept at a time:

```bash
python 1.class.py
python 2.inheritance.py
python 3.encapsulation.py
python 4.polymorphism.py
```

Or run the complete tutorial:

```bash
python oop_tutorial.py
```

---

## 📖 Concepts Explained Simply

### 1️⃣ Classes and Objects

**Think of it like:**

- **Class** = Hero template/character sheet (blueprint for creating heroes)
- **Object** = Actual hero character (a specific hero created from the template)

**JX Game Example:**

```python
class Hero:
    def __init__(self, name, sect):
        self.name = name
        self.sect = sect  # Shaolin, Wudang, Emei, etc.

hero1 = Hero("Zhang Wei", "Shaolin")  # hero1 is an object
hero2 = Hero("Li Mei", "Emei")        # hero2 is another object
```

---

### 2️⃣ Inheritance

**Think of it like:**

- Base hero template that all JX game heroes share
- Specialized sects (Shaolin, Wudang, Emei) inherit common features

**JX Game Example:**

```python
class Hero:                    # Parent class
    def take_damage(self):
        return "took damage"

class ShaolinHero(Hero):       # Child class inherits from Hero
    def dragon_strike(self):
        return "dragon strike!"

shaolin = ShaolinHero()
shaolin.take_damage()    # Can use parent's method
shaolin.dragon_strike()  # Can use sect-specific martial arts
```

---

### 3️⃣ Encapsulation

**Think of it like:**

- Game anti-cheat protection
- Players can't directly modify their gold or stats
- Must use game mechanics to earn/spend resources

**Game Example:**

```python
class PlayerInventory:
    def __init__(self, gold):
        self.__gold = gold  # Private (protected from cheating)

    def get_gold(self):     # Public method to check gold
        return self.__gold

    def earn_gold(self, amount):  # Controlled way to gain gold
        self.__gold += amount

player = PlayerInventory(100)
# player.__gold = 999999  # ❌ Can't cheat!
player.earn_gold(50)        # ✅ Must earn it properly
```

---

### 4️⃣ Polymorphism

**Think of it like:**

- Same action button, different results based on character
- "Attack" → Warrior slashes, Mage casts spell, Archer shoots arrow

**Game Example:**

```python
class Warrior:
    def attack(self):
        return "Sword slash!"

class Mage:
    def attack(self):
        return "Fireball!"

heroes = [Warrior(), Mage()]
for hero in heroes:
    print(hero.attack())  # Same method, different attacks
```

---

## 🎮 Real-World Example

The tutorial includes a **Game Character System** that demonstrates all concepts:

- **Classes/Objects**: Different character types (Warrior, Mage, Archer)
- **Inheritance**: All characters inherit from GameCharacter
- **Encapsulation**: Health and mana are private, accessed through methods
- **Polymorphism**: Each character attacks differently

---

## 💡 Key Takeaways

| Concept | Purpose | Game Analogy |
|---------|---------|-------------------|
| **Classes & Objects** | Create reusable blueprints | Hero template & actual heroes |
| **Inheritance** | Reuse code from parent classes | Base character → Warrior/Mage/Archer |
| **Encapsulation** | Hide and protect data | Anti-cheat protection for stats/gold |
| **Polymorphism** | Same interface, different behavior | Attack button works for all heroes differently |

---

## 🎯 Practice Exercises

Try creating your own classes:

1. **Vehicle System**: Create a `Vehicle` parent class, then `Car`, `Bike`, `Truck` child classes
2. **School System**: Create `Person` parent, then `Student`, `Teacher` child classes
3. **Shopping Cart**: Create `Product` class with encapsulated price and inventory

---

## 📝 Notes

- `self` refers to the current object instance
- `__init__` is the constructor (runs when creating an object)
- `super()` calls the parent class
- `__` prefix makes attributes private
- Methods are functions inside a class

Happy Learning! 🎉
