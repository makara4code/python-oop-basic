"""
OOP Homework - JX Game Character System
Student Name: [YOUR NAME HERE]
Date: [DATE]

This file contains the template for the OOP homework assignment.
Complete each section according to the requirements in HOMEWORK.md
"""

# ============================================================================
# PART 1: CLASSES AND OBJECTS (25 points)
# ============================================================================


class JXCharacter:
    """Base class for JX game characters"""

    def __init__(self, name, sect):
        """
        Initialize a JX character

        Args:
            name: Character's name
            sect: Sect name (Shaolin, Wudang, Emei, etc.)
        """
        # TODO: Initialize all attributes
        # - name
        # - sect
        # - level (starts at 1)
        # - health and max_health (100 * level)
        # - experience (starts at 0)
        pass

    def display_info(self):
        """Display character information"""
        # TODO: Print character stats in a nice format
        pass

    def gain_exp(self, amount):
        """Add experience points"""
        # TODO: Add experience
        # TODO: Check if enough XP to level up (100 XP per level)
        pass

    def level_up(self):
        """Increase character level"""
        # TODO: Increase level
        # TODO: Update max_health
        # TODO: Restore health to max
        # TODO: Reset experience
        pass

    def take_damage(self, damage):
        """Reduce health by damage amount"""
        # TODO: Reduce health
        # TODO: Make sure health doesn't go below 0
        pass

    def heal(self, amount):
        """Restore health"""
        # TODO: Increase health
        # TODO: Make sure health doesn't exceed max_health
        pass


# ============================================================================
# PART 2: INHERITANCE (25 points)
# ============================================================================


class ShaolinWarrior(JXCharacter):
    """Shaolin sect - powerful melee martial arts"""

    def __init__(self, name):
        # TODO: Call parent constructor with sect="Shaolin"
        # TODO: Add inner_strength attribute (default: 50)
        pass

    def dragon_strike(self):
        """Shaolin special skill - powerful melee attack"""
        # TODO: Calculate damage based on level and inner_strength
        # TODO: Return attack description
        pass

    def iron_body(self):
        """Shaolin special skill - increase defense"""
        # TODO: Implement defense boost
        pass


class WudangSwordsman(JXCharacter):
    """Wudang sect - sword techniques and agility"""

    def __init__(self, name):
        # TODO: Call parent constructor with sect="Wudang"
        # TODO: Add sword_mastery attribute (default: 60)
        pass

    def tai_chi_sword(self):
        """Wudang special skill - balanced sword attack"""
        # TODO: Implement sword attack
        pass

    def cloud_step(self):
        """Wudang special skill - dodge ability"""
        # TODO: Implement dodge mechanic
        pass


class EmeiHealer(JXCharacter):
    """Emei sect - healing and support"""

    def __init__(self, name):
        # TODO: Call parent constructor with sect="Emei"
        # TODO: Add chi attribute (default: 100)
        pass

    def healing_light(self, target=None):
        """Emei special skill - heal self or ally"""
        # TODO: Check if enough chi (costs 30)
        # TODO: Heal target or self
        # TODO: Reduce chi
        pass

    def restore_chi(self):
        """Emei special skill - restore chi points"""
        # TODO: Restore chi (maybe 50 points)
        pass


# ============================================================================
# PART 3: ENCAPSULATION (25 points)
# ============================================================================


class PlayerInventory:
    """Manages player's inventory with private attributes"""

    def __init__(self, starting_gold=100):
        # TODO: Initialize PRIVATE attributes (use __ prefix)
        # - __gold (starts at starting_gold)
        # - __items (empty list)
        # - __max_capacity (20 items)
        pass

    def get_gold(self):
        """Return current gold amount"""
        # TODO: Return __gold
        pass

    def earn_gold(self, amount):
        """Add gold (only positive amounts)"""
        # TODO: Validate amount is positive
        # TODO: Add to __gold
        pass

    def spend_gold(self, amount):
        """Subtract gold (check if enough gold)"""
        # TODO: Check if enough gold
        # TODO: Subtract from __gold
        # TODO: Return True/False for success
        pass

    def add_item(self, item_name):
        """Add item to inventory"""
        # TODO: Check if inventory is full
        # TODO: Add item to __items list
        pass

    def remove_item(self, item_name):
        """Remove item from inventory"""
        # TODO: Check if item exists
        # TODO: Remove from __items list
        pass

    def get_items(self):
        """Return copy of items list"""
        # TODO: Return a COPY of __items (not the original)
        pass

    def display_inventory(self):
        """Display all items and gold"""
        # TODO: Print gold amount
        # TODO: Print all items
        # TODO: Print capacity (current/max)
        pass


# ============================================================================
# PART 4: POLYMORPHISM (25 points)
# ============================================================================


class Skill:
    """Base class for all skills"""

    def use_skill(self, user_name):
        """Use the skill - to be overridden by child classes"""
        # TODO: Return basic skill description
        pass


class MeleeAttack(Skill):
    """Physical melee attack skill"""

    def use_skill(self, user_name):
        # TODO: Return melee attack description
        pass


class RangedAttack(Skill):
    """Distance ranged attack skill"""

    def use_skill(self, user_name):
        # TODO: Return ranged attack description
        pass


class HealingSkill(Skill):
    """Restoration/healing skill"""

    def use_skill(self, user_name):
        # TODO: Return healing description
        pass


class BuffSkill(Skill):
    """Enhancement/buff skill"""

    def use_skill(self, user_name):
        # TODO: Return buff description
        pass


# ============================================================================
# TESTING SECTION
# ============================================================================


def test_part1():
    """Test Classes and Objects"""
    print("=" * 60)
    print("PART 1: CLASSES AND OBJECTS TEST")
    print("=" * 60)
    # TODO: Create 2 characters
    # TODO: Test all methods (gain_exp, level_up, take_damage, heal)
    # TODO: Display character info
    pass


def test_part2():
    """Test Inheritance"""
    print("\n" + "=" * 60)
    print("PART 2: INHERITANCE TEST")
    print("=" * 60)
    # TODO: Create one character from each sect
    # TODO: Test inherited methods (take_damage, heal)
    # TODO: Test sect-specific skills
    pass


def test_part3():
    """Test Encapsulation"""
    print("\n" + "=" * 60)
    print("PART 3: ENCAPSULATION TEST")
    print("=" * 60)
    # TODO: Create inventory
    # TODO: Test earning and spending gold
    # TODO: Test adding and removing items
    # TODO: Try to access private attributes (should fail)
    pass


def test_part4():
    """Test Polymorphism"""
    print("\n" + "=" * 60)
    print("PART 4: POLYMORPHISM TEST")
    print("=" * 60)
    # TODO: Create list of different skills
    # TODO: Loop through and use each skill
    # TODO: Show polymorphism in action
    pass


# ============================================================================
# MAIN PROGRAM
# ============================================================================

if __name__ == "__main__":
    print("JX GAME CHARACTER SYSTEM - OOP HOMEWORK")
    print("Student: [YOUR NAME]")
    print()

    # Run all tests
    test_part1()
    test_part2()
    test_part3()
    test_part4()

    print("\n" + "=" * 60)
    print("ALL TESTS COMPLETED!")
    print("=" * 60)
