"""
ENCAPSULATION
=============
Encapsulation means hiding internal details and protecting data.

KEY CONCEPTS:
- Private attributes: Use __ prefix (double underscore)
- Public methods: Provide controlled access to private data
- Data protection: Prevent direct modification of sensitive data

GAME ANALOGY:
- Like a game's internal mechanics - players can't directly modify their stats
- Like an inventory system - you can't just set gold = 999999, you must earn it
- Like anti-cheat protection - game rules are enforced through controlled methods

Think of it as the game engine protecting critical data:
- Players interact through the UI (public methods)
- Internal calculations are hidden and protected (private attributes)
- Prevents cheating and maintains game balance
"""

# ============================================================================
# EXAMPLE 1: Player Inventory System
# ============================================================================

class PlayerInventory:
    """Demonstrates encapsulation with private attributes"""

    def __init__(self, player_name, starting_gold=100):
        self.player_name = player_name
        # __ prefix makes this attribute "private" - can't be directly modified
        self.__gold = starting_gold
        self.__max_capacity = 20
        self.__items = []

    # Getter method - allows reading gold safely
    def get_gold(self):
        return self.__gold

    # Method to earn gold with validation
    def earn_gold(self, amount):
        if amount > 0:
            self.__gold += amount
            return f"{self.player_name} earned {amount} gold! Total: {self.__gold}g"
        else:
            return "Invalid gold amount"

    # Method to spend gold with validation
    def spend_gold(self, amount):
        if amount > 0 and amount <= self.__gold:
            self.__gold -= amount
            return f"Spent {amount} gold. Remaining: {self.__gold}g"
        else:
            return "Insufficient gold or invalid amount!"

    def add_item(self, item):
        if len(self.__items) < self.__max_capacity:
            self.__items.append(item)
            return f"Added {item} to inventory ({len(self.__items)}/{self.__max_capacity})"
        return "Inventory full!"

    def get_inventory_status(self):
        return f"Gold: {self.__gold}g | Items: {len(self.__items)}/{self.__max_capacity}"


print("=" * 60)
print("ENCAPSULATION EXAMPLE - PLAYER INVENTORY")
print("=" * 60)

player = PlayerInventory("Aragorn", 500)

# We can't directly access __gold (it's private and protected)
# player.__gold = 999999  # This won't work - prevents cheating!

# Instead, we use the public methods - the game controls gold flow
print(f"Player: {player.player_name}")
print(player.get_inventory_status())
print(player.earn_gold(150))
print(player.spend_gold(100))
print(player.spend_gold(10000))  # This will fail - not enough gold
print(player.add_item("Health Potion"))
print(player.add_item("Legendary Sword"))
print(player.get_inventory_status())
print()


# ============================================================================
# EXAMPLE 2: Character Stats System
# ============================================================================

class CharacterStats:
    """Demonstrates encapsulation for game balance"""

    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        # Private stats - can't be directly modified to prevent cheating
        self.__strength = 10
        self.__agility = 10
        self.__intelligence = 10
        self.__stat_points = 5  # Points available to spend

    def get_stats(self):
        return {
            "Strength": self.__strength,
            "Agility": self.__agility,
            "Intelligence": self.__intelligence,
            "Available Points": self.__stat_points
        }

    def increase_strength(self, points):
        if points > 0 and points <= self.__stat_points:
            self.__strength += points
            self.__stat_points -= points
            return f"Increased Strength by {points}! New STR: {self.__strength}"
        return "Not enough stat points or invalid amount!"

    def increase_agility(self, points):
        if points > 0 and points <= self.__stat_points:
            self.__agility += points
            self.__stat_points -= points
            return f"Increased Agility by {points}! New AGI: {self.__agility}"
        return "Not enough stat points or invalid amount!"

    def increase_intelligence(self, points):
        if points > 0 and points <= self.__stat_points:
            self.__intelligence += points
            self.__stat_points -= points
            return f"Increased Intelligence by {points}! New INT: {self.__intelligence}"
        return "Not enough stat points or invalid amount!"

    def level_up_reward(self):
        self.__stat_points += 3
        return f"Level up! Gained 3 stat points. Total available: {self.__stat_points}"


print("=" * 60)
print("ENCAPSULATION EXAMPLE - CHARACTER STATS")
print("=" * 60)

hero = CharacterStats("Legolas", "Archer")

# Can't directly modify stats - prevents cheating!
# hero.__strength = 999  # This won't work!

print(f"Character: {hero.name} ({hero.character_class})")
print(f"Stats: {hero.get_stats()}")
print(hero.increase_agility(3))
print(hero.increase_strength(2))
print(hero.increase_strength(5))  # Not enough points!
print(hero.level_up_reward())
print(hero.increase_intelligence(2))
print(f"Final Stats: {hero.get_stats()}")
print()


# ============================================================================
# EXAMPLE 3: Skill Cooldown System
# ============================================================================

class Skill:
    """Demonstrates encapsulation with cooldown management"""

    def __init__(self, name, damage, cooldown_turns):
        self.name = name
        self.damage = damage
        self.__cooldown_turns = cooldown_turns
        self.__current_cooldown = 0  # Private - prevents cooldown manipulation

    def use_skill(self):
        # Validate skill is ready before using
        if self.__current_cooldown == 0:
            self.__current_cooldown = self.__cooldown_turns
            return f"Used {self.name}! Dealt {self.damage} damage. Cooldown: {self.__cooldown_turns} turns"
        else:
            return f"{self.name} is on cooldown! {self.__current_cooldown} turns remaining"

    def advance_turn(self):
        if self.__current_cooldown > 0:
            self.__current_cooldown -= 1
            if self.__current_cooldown == 0:
                return f"{self.name} is ready!"
            return f"{self.name} cooldown: {self.__current_cooldown} turns remaining"
        return f"{self.name} is ready to use"

    def get_status(self):
        if self.__current_cooldown == 0:
            return f"{self.name} - READY (Damage: {self.damage})"
        return f"{self.name} - ON COOLDOWN ({self.__current_cooldown} turns)"


print("=" * 60)
print("ENCAPSULATION EXAMPLE - SKILL COOLDOWN SYSTEM")
print("=" * 60)

ultimate = Skill("Dragon Strike", 500, 3)

# Can't directly reset cooldown - prevents spamming powerful skills!
# ultimate.__current_cooldown = 0  # This won't work!

print(ultimate.get_status())
print(ultimate.use_skill())      # Use the skill
print(ultimate.use_skill())      # Try to use again - on cooldown!
print()
print(ultimate.advance_turn())   # Turn 1
print(ultimate.advance_turn())   # Turn 2
print(ultimate.advance_turn())   # Turn 3 - ready!
print()
print(ultimate.use_skill())      # Can use again!
print(ultimate.get_status())
print()


# ============================================================================
# KEY POINTS:
# ============================================================================
"""
1. PRIVATE ATTRIBUTES:
   - Use __ prefix: self.__gold, self.__strength, self.__cooldown
   - Cannot be accessed directly from outside the class
   - Protects sensitive data from cheating/manipulation

2. PUBLIC METHODS:
   - No __ prefix: def earn_gold(self), def use_skill(self)
   - Can be called from outside the class
   - Provide controlled access to private data

3. GETTER METHODS:
   - Allow reading private attributes safely
   - Example: def get_gold(self), def get_stats(self)
   - Players can see their stats but can't directly modify them

4. SETTER METHODS:
   - Allow modifying private attributes with validation
   - Example: def spend_gold(self, amount), def increase_strength(self, points)
   - Ensures game rules are followed (can't spend more gold than you have)

5. BENEFITS:
   - Data protection (prevent invalid values like negative gold)
   - Security (hide sensitive information, prevent cheating)
   - Game balance (enforce cooldowns, stat limits, resource costs)
   - Control (validate data before accepting it)

6. WHY USE ENCAPSULATION IN GAMES?
   - Prevent cheating (can't set gold = 999999 directly)
   - Enforce game rules (must earn gold, can't spam powerful skills)
   - Maintain balance (stat increases cost points, skills have cooldowns)
   - Hide complexity (players don't need to know internal calculations)
   - Make code maintainable (change internal logic without breaking game)

REAL-WORLD GAME DEVELOPMENT:
- All professional games use encapsulation extensively
- Prevents hacking and maintains fair gameplay
- Separates game logic from player interface
- This is a fundamental anti-cheat mechanism!
"""
