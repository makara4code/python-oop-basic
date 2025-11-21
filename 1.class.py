"""
CLASSES AND OBJECTS
===================
A class is like a blueprint or template for creating objects.
An object is an instance (actual copy) created from a class.

JX GAME ANALOGY:
- Class = Hero character sheet (defines what a hero can be)
- Object = Your actual hero character (a specific hero you created)

Think of it like JX game character creation:
- The class defines what attributes a hero has (name, sect, level, health, etc.)
- Each object is YOUR unique hero with specific values
- You can create heroes and join different sects like Shaolin, Wudang, Emei, etc.
"""

# ============================================================================
# EXAMPLE 1: Hero Class
# ============================================================================


class Hero:
    """A class representing a JX game hero/character"""

    # __init__ is a special method called a "constructor"
    # It runs automatically when you create a new Hero object
    def __init__(self, name, sect, level):
        # 'self' refers to the specific object being created
        # These are called "attributes" or "properties"
        self.name = name
        self.sect = sect  # Martial arts sect (Shaolin, Wudang, Emei, etc.)
        self.level = level
        self.health = level * 100  # Health scales with level
        self.experience = 0

    # This is a "method" - a function that belongs to the class
    def attack(self):
        damage = self.level * 10
        return f"{self.name} attacks for {damage} damage!"

    def gain_experience(self, xp):
        self.experience += xp
        return f"{self.name} gained {xp} XP! Total: {self.experience} XP"

    def level_up(self):
        self.level += 1
        self.health = self.level * 100
        return f"{self.name} leveled up to {self.level}! Health: {self.health}"

    def get_stats(self):
        return f"{self.name} - Level {self.level} {self.sect} | HP: {self.health} | XP: {self.experience}"


# ============================================================================
# CREATING AND USING OBJECTS
# ============================================================================

print("=" * 60)
print("JX GAME - HERO CHARACTER CREATION")
print("=" * 60)

# Creating hero objects (instances) from the Hero class
# Each hero is a unique object with its own attributes
# In JX game, you create a hero and join a sect
hero1 = Hero("Zhang Wei", "Shaolin", 5)  # Shaolin sect - martial arts masters
hero2 = Hero("Li Mei", "Emei", 10)  # Emei sect - known for healing and support

# Using the objects - each hero has its own data and behaviors
print(hero1.get_stats())
print(hero1.attack())
print(hero1.gain_experience(150))
print()
print(hero2.get_stats())
print(hero2.attack())
print(hero2.level_up())
print(hero2.get_stats())
print()

# ============================================================================
# EXAMPLE 2: Weapon Class
# ============================================================================


class Weapon:
    """A class representing a weapon in the game"""

    def __init__(self, name, weapon_type, damage, durability=100):
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.durability = durability  # Default value

    def use(self):
        if self.durability > 0:
            self.durability -= 10
            return f"{self.name} deals {self.damage} damage! Durability: {self.durability}%"
        else:
            return f"{self.name} is broken and needs repair!"

    def repair(self):
        self.durability = 100
        return f"{self.name} has been fully repaired!"

    def get_info(self):
        return f"{self.name} ({self.weapon_type}) - Damage: {self.damage}, Durability: {self.durability}%"


# Creating weapon objects
print("=" * 60)
print("WEAPON SYSTEM EXAMPLE")
print("=" * 60)

sword = Weapon("Excalibur", "Sword", 75)
staff = Weapon("Staff of Power", "Magic Staff", 90, 80)

print(sword.get_info())
print(sword.use())
print(sword.use())
print(sword.repair())
print()
print(staff.get_info())
print(staff.use())

# ============================================================================
# EXAMPLE 3: Quest Class
# ============================================================================


class Quest:
    """A class representing a game quest/mission"""

    def __init__(self, title, difficulty, reward):
        self.title = title
        self.difficulty = difficulty
        self.reward = reward
        self.completed = False
        self.progress = 0

    def update_progress(self, amount):
        if not self.completed:
            self.progress += amount
            if self.progress >= 100:
                self.progress = 100
                self.completed = True
                return f"Quest '{self.title}' completed! Reward: {self.reward} gold"
            return f"Quest progress: {self.progress}%"
        return "Quest already completed!"

    def get_status(self):
        status = "Completed" if self.completed else f"In Progress ({self.progress}%)"
        return f"[{self.difficulty}] {self.title} - {status}"


print("=" * 60)
print("QUEST SYSTEM EXAMPLE")
print("=" * 60)

quest1 = Quest("Defeat the Dragon", "Hard", 1000)
quest2 = Quest("Gather Herbs", "Easy", 50)

print(quest1.get_status())
print(quest1.update_progress(50))
print(quest1.update_progress(30))
print(quest1.update_progress(25))
print(quest1.get_status())
print()
print(quest2.get_status())
print(quest2.update_progress(100))
print(quest2.get_status())
print()

# ============================================================================
# KEY POINTS:
# ============================================================================
"""
1. A CLASS is a blueprint that defines:
   - Attributes (data/properties) - like hero stats, weapon damage
   - Methods (functions/behaviors) - like attack(), level_up()

2. An OBJECT is created from a class using:
   hero = Hero("Aragorn", "Warrior", 5)

   Think: Creating a specific character from a character template

3. __init__ method:
   - Called automatically when creating an object
   - Used to initialize attributes (set starting values)
   - Like setting up a new character's initial stats

4. self parameter:
   - Refers to the current object (this specific hero, weapon, quest)
   - Must be the first parameter in methods
   - Used to access attributes and methods

5. Attributes:
   - Variables that belong to an object (name, level, health, damage)
   - Accessed using: hero.name, weapon.damage
   - Each object has its own copy of these values

6. Methods:
   - Functions that belong to a class (attack(), repair(), level_up())
   - Called using: hero.attack(), weapon.use()
   - Define what actions an object can perform

REAL-WORLD PARALLEL:
- In a game, you create multiple heroes from the same Hero class
- Each hero has unique stats but shares the same abilities
- This is exactly how classes and objects work in programming!
"""
