# OOP Homework Assignment - JX Game System

## 📋 Overview

Create a JX game character management system that demonstrates all four OOP concepts:
- Classes and Objects
- Inheritance
- Encapsulation
- Polymorphism

---

## 🎯 Assignment Requirements

### Part 1: Classes and Objects (25 points)

Create a `JXCharacter` class with the following requirements:

**Attributes:**
- `name` - Character's name
- `sect` - Sect name (Shaolin, Wudang, Emei, Tianshan, etc.)
- `level` - Current level (starts at 1)
- `health` - Current health points
- `max_health` - Maximum health points
- `experience` - Experience points (starts at 0)

**Methods:**
- `__init__(name, sect)` - Constructor
- `display_info()` - Display character information
- `gain_exp(amount)` - Add experience points
- `level_up()` - Increase level (requires 100 XP per level)
- `take_damage(damage)` - Reduce health
- `heal(amount)` - Restore health (cannot exceed max_health)

**Test your class by:**
- Creating at least 2 different characters
- Making them gain experience and level up
- Testing damage and healing

---

### Part 2: Inheritance (25 points)

Create **THREE** sect-specific classes that inherit from `JXCharacter`:

**1. ShaolinWarrior (Shaolin Sect)**
- Additional attribute: `inner_strength` (default: 50)
- Special skill: `dragon_strike()` - Powerful melee attack
- Special skill: `iron_body()` - Temporarily increase defense

**2. WudangSwordsman (Wudang Sect)**
- Additional attribute: `sword_mastery` (default: 60)
- Special skill: `tai_chi_sword()` - Balanced attack
- Special skill: `cloud_step()` - Dodge ability

**3. EmeiHealer (Emei Sect)**
- Additional attribute: `chi` (default: 100)
- Special skill: `healing_light()` - Heal self or ally (costs 30 chi)
- Special skill: `restore_chi()` - Restore chi points

**Requirements:**
- Use `super()` to call parent constructor
- Each sect must have at least 2 unique methods
- Demonstrate that inherited methods still work

---

### Part 3: Encapsulation (25 points)

Create a `PlayerInventory` class with **private attributes**:

**Private Attributes:**
- `__gold` - Player's gold (starts at 100)
- `__items` - List of items (starts empty)
- `__max_capacity` - Maximum items (default: 20)

**Public Methods:**
- `get_gold()` - Return current gold amount
- `earn_gold(amount)` - Add gold (only positive amounts)
- `spend_gold(amount)` - Subtract gold (check if enough gold)
- `add_item(item_name)` - Add item to inventory (check capacity)
- `remove_item(item_name)` - Remove item from inventory
- `get_items()` - Return copy of items list
- `display_inventory()` - Show all items and gold

**Requirements:**
- Gold and items must be private (use `__` prefix)
- Validate all inputs (no negative gold, check capacity, etc.)
- Prevent direct access to private attributes
- Show why encapsulation prevents cheating

---

### Part 4: Polymorphism (25 points)

Create a combat system demonstrating polymorphism:

**Create a base `Skill` class:**
- Method: `use_skill(user_name)` - Returns skill description

**Create at least 4 different skill types:**
1. `MeleeAttack` - Physical damage skill
2. `RangedAttack` - Distance attack skill
3. `HealingSkill` - Restoration skill
4. `BuffSkill` - Enhancement skill

**Requirements:**
- All skills inherit from `Skill` class
- Each skill has different implementation of `use_skill()`
- Create a list of different skills
- Loop through and use each skill (polymorphism in action)
- Each skill should return different output

**Example:**
```python
skills = [MeleeAttack(), RangedAttack(), HealingSkill(), BuffSkill()]
for skill in skills:
    print(skill.use_skill("Zhang Wei"))
```

---

## 🎁 Bonus Challenges (Extra 20 points)

### Bonus 1: Party System (10 points)
Create a `Party` class that can:
- Add up to 5 characters
- Display all party members
- Calculate total party level
- Heal all party members

### Bonus 2: Boss Battle (10 points)
Create a `Boss` class with:
- Much higher health than normal characters
- Special attack that damages all party members
- Loot system (drops items when defeated)

---

## 📝 Submission Requirements

**Your submission must include:**

1. **Python file(s)** with all your code
2. **Comments** explaining your code
3. **Test output** showing all features working
4. **README** explaining how to run your program

**File naming:**
- `homework_yourname.py` (or split into multiple files)
- Include your name in comments at the top

---

## ✅ Grading Rubric

| Category | Points | Criteria |
|----------|--------|----------|
| Part 1: Classes & Objects | 25 | Correct class structure, all methods work |
| Part 2: Inheritance | 25 | 3 sect classes, proper use of super() |
| Part 3: Encapsulation | 25 | Private attributes, validation, getters/setters |
| Part 4: Polymorphism | 25 | Base class, 4+ skill types, proper override |
| Code Quality | 10 | Comments, naming, organization |
| Testing | 10 | Comprehensive tests, clear output |
| **Bonus** | 20 | Party system and/or Boss battle |
| **Total** | **120** | (100 base + 20 bonus) |

---

## 💡 Tips for Success

1. **Start with Part 1** - Get the base class working first
2. **Test frequently** - Run your code after each part
3. **Use comments** - Explain what your code does
4. **Follow examples** - Review the tutorial files (1.class.py, 2.inheritance.py, etc.)
5. **Ask questions** - If stuck, review the OOP_GUIDE.md
6. **Be creative** - Add your own sects, skills, or features!

---

## 📅 Due Date

**[Instructor: Fill in due date]**

---

## ❓ Common Questions

**Q: Can I use different sect names?**
A: Yes! Feel free to use any JX game sects you know.

**Q: Can I add more features?**
A: Absolutely! Creativity is encouraged.

**Q: How much code is expected?**
A: Approximately 200-300 lines for base requirements, more with bonuses.

**Q: Can I work in groups?**
A: [Instructor: Specify your policy]

---

## 🎮 Example Output

Your program should produce output similar to:

```
=== JX Game Character System ===

Creating Characters...
Zhang Wei - Level 1 Shaolin | HP: 100/100 | XP: 0
Li Mei - Level 1 Emei | HP: 100/100 | XP: 0

Testing Combat...
Zhang Wei performs Dragon Strike for 75 damage!
Li Mei casts Healing Light, restored 50 HP!

Inventory System...
Gold: 100
Added: Health Potion
Spent 50 gold on weapon
Gold: 50

Polymorphism Demo...
[Melee Attack] Zhang Wei strikes with sword!
[Ranged Attack] Zhang Wei shoots arrow!
[Healing] Zhang Wei uses healing spell!
[Buff] Zhang Wei gains strength boost!
```

---

**Good luck! Remember: Practice makes perfect! 加油！(Jiā yóu!)**

