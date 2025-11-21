"""
POLYMORPHISM
============
Polymorphism means "many forms" - same method name, different behaviors.

KEY CONCEPTS:
- Different classes can have methods with the same name
- Each class implements the method differently
- Allows treating different objects uniformly

GAME ANALOGY:
- Like an "attack" command: Warriors slash, Mages cast spells, Archers shoot arrows
- Like an "activate" button: Opens chests, triggers switches, talks to NPCs
- Like a "use" action: Drinks potions, equips weapons, reads scrolls

Think of it like a game controller:
- Same button (A/X) performs different actions based on context
- Attack button works for all heroes, but each hero attacks differently
- This makes game code flexible and easy to extend with new character types
"""

# ============================================================================
# EXAMPLE 1: Hero Classes with Different Attack Styles
# ============================================================================

class Hero:
    """Parent class for all heroes"""

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attack(self):
        # This is meant to be overridden by child classes
        pass

    def get_info(self):
        return f"{self.name} (Level {self.level})"


class Warrior(Hero):
    """Warrior - implements attack() with melee combat"""

    def __init__(self, name, level):
        super().__init__(name, level)

    def attack(self):
        damage = self.level * 15
        return f"{self.name} swings a mighty sword for {damage} damage!"


class Mage(Hero):
    """Mage - implements attack() with magic"""

    def __init__(self, name, level):
        super().__init__(name, level)

    def attack(self):
        damage = self.level * 20
        return f"{self.name} casts a devastating fireball for {damage} damage!"


class Archer(Hero):
    """Archer - implements attack() with ranged combat"""

    def __init__(self, name, level):
        super().__init__(name, level)

    def attack(self):
        damage = self.level * 12
        return f"{self.name} shoots a precise arrow for {damage} damage!"


print("=" * 60)
print("POLYMORPHISM EXAMPLE - HERO ATTACKS")
print("=" * 60)

# Create different hero objects
heroes = [
    Warrior("Conan", 5),
    Mage("Gandalf", 5),
    Archer("Legolas", 5)
]

# Polymorphism in action: same method name, different behavior
print("Battle begins! All heroes attack:")
for hero in heroes:
    print(f"{hero.get_info()}")
    print(hero.attack())  # Same method, different implementation!
    print()


# ============================================================================
# EXAMPLE 2: Enemy Types with Different Behaviors
# ============================================================================

class Enemy:
    """Parent class for all enemies"""

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def special_ability(self):
        pass  # To be overridden


class Goblin(Enemy):
    def special_ability(self):
        return f"{self.name} throws a poison dagger!"


class Dragon(Enemy):
    def special_ability(self):
        return f"{self.name} breathes devastating fire!"


class Necromancer(Enemy):
    def special_ability(self):
        return f"{self.name} summons undead minions!"


class Troll(Enemy):
    def special_ability(self):
        return f"{self.name} regenerates health rapidly!"


print("=" * 60)
print("POLYMORPHISM EXAMPLE - ENEMY ABILITIES")
print("=" * 60)

# Create a list of different enemies
enemies = [
    Goblin("Sneaky Goblin", 3),
    Dragon("Ancient Dragon", 20),
    Necromancer("Dark Sorcerer", 15),
    Troll("Mountain Troll", 10)
]

# Same method call, different results!
print("Enemies use their special abilities:")
for enemy in enemies:
    print(f"Level {enemy.level} {enemy.name}: {enemy.special_ability()}")

print()


# ============================================================================
# EXAMPLE 3: Item Types with Different Use Effects
# ============================================================================

class Item:
    """Parent class for all usable items"""

    def __init__(self, name):
        self.name = name

    def use(self):
        pass  # To be overridden


class HealthPotion(Item):
    def __init__(self):
        super().__init__("Health Potion")

    def use(self):
        return f"Used {self.name}: Restored 100 HP!"


class ManaPotion(Item):
    def __init__(self):
        super().__init__("Mana Potion")

    def use(self):
        return f"Used {self.name}: Restored 50 Mana!"


class ScrollOfFireball(Item):
    def __init__(self):
        super().__init__("Scroll of Fireball")

    def use(self):
        return f"Used {self.name}: Cast Fireball dealing 200 damage!"


class TeleportScroll(Item):
    def __init__(self):
        super().__init__("Teleport Scroll")

    def use(self):
        return f"Used {self.name}: Teleported to town!"


print("=" * 60)
print("POLYMORPHISM EXAMPLE - ITEM USAGE")
print("=" * 60)

# Different item types in inventory
inventory = [
    HealthPotion(),
    ManaPotion(),
    ScrollOfFireball(),
    TeleportScroll()
]

# Use all items the same way - polymorphism handles the rest!
print("Using items from inventory:")
for item in inventory:
    print(item.use())  # Same method, different effects!

print()


# ============================================================================
# EXAMPLE 4: NPC Interactions
# ============================================================================

class NPC:
    """Parent class for all NPCs (Non-Player Characters)"""

    def __init__(self, name):
        self.name = name

    def interact(self):
        pass  # To be overridden


class Merchant(NPC):
    def interact(self):
        return f"{self.name}: 'Welcome! Browse my wares and make a purchase!'"


class QuestGiver(NPC):
    def interact(self):
        return f"{self.name}: 'I have a quest for you, brave adventurer!'"


class Guard(NPC):
    def interact(self):
        return f"{self.name}: 'Halt! State your business in this city.'"


class Innkeeper(NPC):
    def interact(self):
        return f"{self.name}: 'Rest here for 50 gold and restore your health.'"


print("=" * 60)
print("POLYMORPHISM EXAMPLE - NPC INTERACTIONS")
print("=" * 60)

# Different NPCs in the town
npcs = [
    Merchant("Trader Tom"),
    QuestGiver("Elder Sage"),
    Guard("Captain Marcus"),
    Innkeeper("Friendly Barkeep")
]

print("Walking through town and talking to NPCs:")
for npc in npcs:
    print(npc.interact())  # Same method, different dialogue!

print()


# ============================================================================
# KEY POINTS:
# ============================================================================
"""
1. POLYMORPHISM DEFINITION:
   - Same method name, different implementations
   - "Poly" = many, "morph" = forms
   - Example: attack() works for all heroes, but each attacks differently

2. HOW IT WORKS:
   - Parent class defines a method (Hero.attack())
   - Child classes override the method with their own version
   - Same method call produces different results
   - Warrior slashes, Mage casts, Archer shoots

3. BENEFITS:
   - Write flexible, reusable code (one battle system for all heroes)
   - Treat different objects uniformly (all heroes can attack)
   - Easy to add new types without changing existing code (add Paladin class easily)
   - Makes code more organized and maintainable

4. GAME EXAMPLES:
   - Different heroes attack differently (Warrior, Mage, Archer)
   - Different enemies use different abilities (Goblin, Dragon, Troll)
   - Different items have different effects (Potions, Scrolls)
   - Different NPCs respond differently (Merchant, Guard, Quest Giver)

5. KEY PATTERN:
   for hero in party:
       hero.attack()  # Each hero attacks in their own way!

   This is powerful because you can add new hero types without
   changing the battle system code!

6. POLYMORPHISM + INHERITANCE:
   - Usually used together in game development
   - Child classes inherit from parent (all heroes inherit from Hero)
   - Child classes override parent's methods (each implements attack differently)
   - Allows treating all children as the parent type (all are Heroes)

REAL GAME DEVELOPMENT:
- Every major game uses polymorphism extensively
- Makes it easy to add new characters, items, enemies
- Battle systems, inventory systems, quest systems all use this
- This is how games can have hundreds of different character types
  without writing separate code for each one!
"""
