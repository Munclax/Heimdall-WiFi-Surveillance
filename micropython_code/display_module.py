# display_module.py - OLED Display Module
# Handles all OLED screen rendering

class Display:
    def __init__(self):
        self.width = 128
        self.height = 64
        self.buffer = [0] * (self.width * self.height)
    
    def init(self):
        # Initialize OLED I2C connection
        # This is placeholder code - actual SPI/I2C setup needed
        print("Display initialized")

    def show_image(self, image_path):
        # Load and render image to buffer
        print(f"Displaying image: {image_path}")
    
    def clear(self):
        # Clear the display buffer
        self.buffer = [0] * (self.width * self.height)
    
    def show_text(self, text="HEIMDALL WiFi Scanner"):
        # Render text to buffer
        print(f"Displaying: {text}")
    
    def update(self):
        # Send buffer to OLED screen
        print("Updating display")
    
    def pixel(self, x, y, color):
        if 0 <= x < self.width and 0 <= y < self.height:
            idx = y * self.width + x
            self.buffer[idx] = color

# Singleton instance
_display = None

def get_display():
    global _display
    if _display is None:
        _display = Display()
    return _display
