# buttons_module.py - Button Input Module
# Handles physical button inputs for navigation

class Buttons:
    def __init__(self):
        self.button_states = [False, False, False, False]
        self.last_states = [False, False, False, False]
    
    def init(self):
        # Initialize button pins
        # This is placeholder code - actual GPIO setup needed
        print("Buttons initialized")
    
    def poll(self):
        # Check current button states
        # Placeholder - actual GPIO reading needed
        pass
    
    def get_state(self, button_index):
        if 0 <= button_index < len(self.button_states):
            return self.button_states[button_index]
        return False

# Singleton instance
_buttons = None

def get_buttons():
    global _buttons
    if _buttons is None:
        _buttons = Buttons()
    return _buttons
