class Pet:
    """Virtual pet class managing hunger, energy, happiness, and tricks."""
    
    def __init__(self, name):
        """Initialize pet with starting values and name."""
        self.name = name
        self.hunger = 1    # Range: 0 (full) to 10 (starving)
        self.energy = 10   # Range: 0 (tired) to 10 (energetic)
        self.happiness = 5 # Range: 0 (miserable) to 10 (ecstatic)
        self.tricks = []   # List of learned tricks

    def _clamp_values(self):
        """Keep all values within 0-10 range (internal helper method)."""
        self.hunger = max(0, min(10, self.hunger))
        self.energy = max(0, min(10, self.energy))
        self.happiness = max(0, min(10, self.happiness))

    def eat(self):
        """Handle eating action with status updates."""
        self.hunger -= 3
        self.happiness += 1
        self._clamp_values()
        print(f"{self.name} chomps down some kibble!")

    def sleep(self):
        """Handle sleeping action with status updates."""
        self.energy += 5
        self.happiness += 1
        self._clamp_values()
        print(f"{self.name} curls up for a nap...")

    def play(self):
        """Handle playing action with status updates."""
        self.energy -= 2
        self.hunger += 2
        self.happiness += 3
        self._clamp_values()
        print(f"{self.name} fetches the ball excitedly!")

    def get_status(self):
        """Display current status with visual indicators."""
        print(f"\n{self.name.upper()} STATUS:")
        print(f"🍖 Hunger: {'★' * self.hunger}{'☆' * (10 - self.hunger)}")
        print(f"⚡ Energy: {'★' * self.energy}{'☆' * (10 - self.energy)}")
        print(f"😊 Happiness: {'★' * self.happiness}{'☆' * (10 - self.happiness)}")

    def train(self, trick):
        """Handle training action with validation."""
        if not trick:
            print("Please specify a trick to teach!")
            return
            
        self.tricks.append(trick)
        self.energy -= 1
        self.happiness += 2
        self._clamp_values()
        print(f"{self.name} learns {trick.upper()}!")

    def show_tricks(self):
        """Display learned tricks with formatting."""
        if not self.tricks:
            print(f"{self.name} hasn't learned any tricks yet!")
            return
            
        print(f"{self.name}'s TRICK LIST:")
        for i, trick in enumerate(self.tricks, 1):
            print(f"{i}. {trick.capitalize()}")


def main():
    """Main interactive loop with input handling and status updates."""
    print("🐶 WELCOME TO VIRTUAL PET SIMULATOR! 🐾")
    pet_name = input("Name your pet: ").strip() or "Buddy"
    dog = Pet(pet_name)
    
    # Command registry with associated methods
    COMMANDS = {
        'feed': dog.eat,
        'sleep': dog.sleep,
        'play': dog.play,
        'status': dog.get_status,
        'tricks': dog.show_tricks,
        'help': lambda: print("\nAvailable commands: feed, sleep, play, status, teach [trick], tricks, quit"),
        'teach': None  # Special case handled separately
    }

    print("\nType 'help' for command list")
    dog.get_status()  # Show initial status

    while True:
        try:
            # Get and clean user input
            action = input("\nWhat would you like to do? ").strip().lower()
            
            if not action:
                continue  # Ignore empty inputs
                
            # Handle exit command
            if action in ('quit', 'exit'):
                print(f"\nThanks for playing with {pet_name}! 🐾")
                break
                
            # Handle training command
            if action.startswith('teach'):
                _, *trick = action.split(maxsplit=1)
                if not trick:
                    print("Please specify a trick to teach!")
                    continue
                dog.train(trick[0])
                dog.get_status()
                continue
                
            # Validate and execute standard commands
            if action in COMMANDS:
                if action == 'teach':  # Shouldn't reach here due to above handling
                    continue
                    
                COMMANDS[action]()  # Execute the command
                
                # Show updated status for actions that change state
                if action in ('feed', 'sleep', 'play'):
                    dog.get_status()
            else:
                print(f"⚠️ Unknown command: {action}. Type 'help' for options.")

        except Exception as e:
            print(f"⚠️ Error: {str(e)}. Please try again.")


if __name__ == "__main__":
    main()