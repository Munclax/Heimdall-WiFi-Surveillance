# main.py - Heimdall WiFi Scanner Entry Point
# Entry point for the ESP32 WiFi network scanner

from esp32 import run_micropython
import wifi_module
import display_module
import buttons_module

def main():
    # Initialize OLED display
    display = display_module.Display()
    display.init()
    display.clear()
    display.show_image("C:\\Users\\prema\\Downloads\\Weathered Heimdall Eye Emblem.png")
    display.update()
    
    # Initialize WiFi
    wifi = wifi_module.WiFi()
    wifi.init()
    wifi.connect()
    
    # Initialize buttons
    buttons = buttons_module.Buttons()
    buttons.init()
    
    # Main loop
    while True:
        # Update display with current network info
        display.update()
        
        # Check for button presses
        buttons.poll()

if __name__ == "__main__":
    main()
