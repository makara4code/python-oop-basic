"""
INHERITANCE
===========
Inheritance allows a class to inherit properties and methods from another class.

TERMINOLOGY:
- Parent class (Base class) = The class being inherited from
- Child class (Derived class) = The class that inherits

JX GAME ANALOGY:
- Parent class = Base hero template (all heroes share common features)
- Child class = Sect-specific hero (Shaolin, Wudang, Emei, etc.)
- All heroes can move and take damage (inherited from base)
- Each sect has unique martial arts skills (specialized)

Think of it like JX game sect system: all heroes start with basic abilities,
then join a sect to learn specialized martial arts techniques.
"""

# ============================================================================
# EXAMPLE 1: JX Game - Sect Inheritance System
# ============================================================================

class Hero:
    """Parent class - represents any JX game hero"""

    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.health = level * 100
        self.is_alive = True

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.is_alive = False
            return f"{self.name} has been defeated!"
        return f"{self.name} took {damage} damage. Health: {self.health}"

    def rest(self):
        heal_amount = self.level * 20
        self.health += heal_amount
        return f"{self.name} rested and recovered {heal_amount} health"


class ShaolinHero(Hero):
    """Child class - Shaolin sect (powerful melee martial arts)"""

    def __init__(self, name, level, inner_strength):
        # Call the parent class constructor using super()
        super().__init__(name, level)
        self.inner_strength = inner_strength  # Shaolin-specific attribute
        self.sect = "Shaolin"

    def dragon_strike(self):
        damage = self.level * 15 + self.inner_strength
        return f"{self.name} performs Dragon Strike for {damage} damage!"


class EmeiHero(Hero):
    """Another child class - Emei sect (healing and support)"""

    def __init__(self, name, level, chi):
        super().__init__(name, level)
        self.chi = chi  # Emei-specific attribute
        self.sect = "Emei"

    def healing_light(self):
        if self.chi >= 30:
            self.chi -= 30
            heal = self.level * 20
            self.health += heal
            return f"{self.name} casts Healing Light, restored {heal} HP! Chi: {self.chi}"
        return f"{self.name} doesn't have enough chi!"


# Using inheritance
print("=" * 60)
print("JX GAME - SECT INHERITANCE EXAMPLE")
print("=" * 60)

shaolin = ShaolinHero("Zhang Wei", 5, 50)
emei = EmeiHero("Li Mei", 5, 100)

# Shaolin and Emei can use methods from Hero class
print(shaolin.take_damage(80))      # Inherited from Hero
print(shaolin.dragon_strike())      # Specific to Shaolin sect
print(shaolin.rest())               # Inherited from Hero
print()
print(emei.take_damage(120))        # Inherited from Hero
print(emei.healing_light())         # Specific to Emei sect
print(emei.healing_light())         # Uses chi
print()


# ============================================================================
# EXAMPLE 2: Item Inheritance (Equipment System)
# ============================================================================

class Item:
    """Parent class for all game items"""

    def __init__(self, name, value, rarity):
        self.name = name
        self.value = value
        self.rarity = rarity

    def sell(self):
        return f"Sold {self.name} for {self.value} gold"

    def get_info(self):
        return f"[{self.rarity}] {self.name} - Value: {self.value}g"


class Weapon(Item):
    """Weapon inherits from Item"""

    def __init__(self, name, value, rarity, damage):
        super().__init__(name, value, rarity)
        self.damage = damage

    def attack_with(self):
        return f"Attacking with {self.name} for {self.damage} damage!"


class Potion(Item):
    """Potion inherits from Item"""

    def __init__(self, name, value, rarity, healing_power):
        super().__init__(name, value, rarity)
        self.healing_power = healing_power

    def consume(self):
        return f"Consumed {self.name}, restored {self.healing_power} health!"


print("=" * 60)
print("ITEM INHERITANCE EXAMPLE")
print("=" * 60)

sword = Weapon("Legendary Sword", 500, "Legendary", 85)
health_potion = Potion("Greater Health Potion", 50, "Rare", 150)

print(sword.get_info())          # Inherited from Item
print(sword.attack_with())       # Specific to Weapon
print(sword.sell())              # Inherited from Item
print()
print(health_potion.get_info())  # Inherited from Item
print(health_potion.consume())   # Specific to Potion
print()


# ============================================================================
# EXAMPLE 3: Method Overriding (Boss Enemies)
# ============================================================================

class Enemy:
    """Parent class for all enemies"""

    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self):
        return f"{self.name} attacks for {self.damage} damage"

    def get_loot(self):
        return f"{self.name} dropped 10 gold"


class BossEnemy(Enemy):
    """Child class that overrides parent methods"""

    def __init__(self, name, health, damage, special_ability):
        super().__init__(name, health, damage)
        self.special_ability = special_ability

    # Override the parent's attack method - bosses hit harder!
    def attack(self):
        boss_damage = self.damage * 2
        return f"{self.name} unleashes {self.special_ability} for {boss_damage} damage!"

    # Override the parent's get_loot method - bosses drop better loot!
    def get_loot(self):
        return f"{self.name} dropped 500 gold and a Legendary Item!"


print("=" * 60)
print("METHOD OVERRIDING EXAMPLE - BOSS BATTLES")
print("=" * 60)

goblin = Enemy("Goblin Scout", 50, 15)
dragon = BossEnemy("Ancient Dragon", 5000, 100, "Dragon's Breath")

print(goblin.attack())      # Normal enemy attack
print(goblin.get_loot())    # Normal loot
print()
print(dragon.attack())      # Boss attack (overridden - more powerful!)
print(dragon.get_loot())    # Boss loot (overridden - better rewards!)
print()


# ============================================================================
# KEY POINTS:
# ============================================================================
"""
1. INHERITANCE SYNTAX:
   class Warrior(GameCharacter):
       # Warrior inherits from GameCharacter

   Think: Warrior is a specialized type of GameCharacter

2. super() function:
   - Calls methods from the parent class
   - Commonly used in __init__ to initialize parent attributes
   - Example: super().__init__(name, level) sets up base character stats

3. BENEFITS:
   - Code reusability (all heroes share common features like health, level)
   - Logical hierarchy (GameCharacter → Warrior, Mage, Archer)
   - Easy to extend functionality (add new hero classes easily)

4. METHOD OVERRIDING:
   - Child class can replace parent's method with its own version
   - Same method name, different implementation
   - Example: Boss enemies attack differently than normal enemies

5. INHERITANCE CHAIN:
   - Child inherits everything from parent (all heroes can take_damage, rest)
   - Child can add new attributes/methods (Warrior has armor, Mage has mana)
   - Child can override parent's methods (Boss attack is stronger)

GAME DEVELOPMENT PARALLEL:
- Base GameCharacter class = Common features all characters share
- Warrior, Mage, Archer = Specialized classes with unique abilities
- This is exactly how real game engines organize character classes!
- Saves time: write common code once, specialize where needed
"""
