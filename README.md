# 🐾 Virtual Pet Simulator

A Python-based interactive virtual pet experience using Object-Oriented Programming (OOP) principles.

## 🎮 Features
- **Core Interactions**
  - 🍖 Feed your pet to reduce hunger
  - 💤 Put pet to sleep for energy recovery
  - 🎮 Play to increase happiness
  - 🎓 Teach custom tricks
- **Dynamic Status System**
  - Real-time hunger/energy/happiness tracking (0-10 scale)
  - Automatic status degradation/improvement
  - Visual star-based status display
- **Robust CLI Interface**
  - Natural language commands
  - Input validation and error handling
  - Contextual help system

## ⚙️ Installation
1. **Prerequisites**: Python 3.6+
2. Clone repository:
3. Run the simulator:
   ```bash
   python pet.py
   ```

## 🖥️ Usage
```plaintext
> Name your pet: Buddy

Type 'help' for command list

What would you like to do? feed
Buddy chomps down some kibble!

BUDDY STATUS:
🍖 Hunger: ★★☆☆☆☆☆☆☆☆
⚡ Energy: ★★★★★★☆☆☆☆
😊 Happiness: ★★★★★★★☆☆☆

What would you like to do? teach roll over
Buddy learns ROLL OVER!
```

**Available Commands**:
```
help        Show command list
feed        Give food to pet
sleep       Restore pet's energy
play        Engage in playtime
status      Show current stats
teach [trick]  Train new trick
tricks      List learned tricks
quit        Exit program
```
