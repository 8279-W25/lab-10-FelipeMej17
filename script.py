import time
from adafruit_circuitplayground import cp

# Morse dictionary
MORSE = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
    'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
    'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
    'z': '--..', ' ': '/', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----'
}


#LED Control Functions ON/OFF and color
def leds_on(color):
    cp.pixels.fill(color)
    cp.pixels.show()


def leds_off():
    cp.pixels.fill((0, 0, 0))
    cp.pixels.show()


# User Input Functions: 1: color
def get_color():
    print("Enter RGB color (3 numbers 0-255 separated by spaces):")
    while True:
        try:
            r, g, b = map(int, input().split())
            if all(0 <= val <= 255 for val in (r, g, b)):
                return (r, g, b)
            print("Values must be 0-255. Try again.")
        except:
            print("Invalid input. Enter 3 numbers separated by spaces.")

# User Input Functions: 2: timing

def get_unit_time():
    print("Enter unit time in seconds (0.1-1.0):")
    while True:
        try:
            unit = float(input())
            if 0.1 <= unit <= 1.0:
                return unit
            print("Please enter between 0.1 and 1.0")
        except:
            print("Invalid number. Try again.")


#cleaner: pass the text through a loop and sort it by looking the key in the dictionary
def clean_text(text):
    return ''.join(c for c in text.lower() if c in MORSE)

#converter:the cleaned text is sorted by its size and properties (words,letters or letter(single))
def text_to_morse(text):
    cleaned = clean_text(text)
    morse_words = []
    for word in cleaned.split(' '):
        morse_letters = []
        for letter in word:
            morse_letters.append(MORSE[letter])
        morse_words.append(' '.join(morse_letters))
    return ' / '.join(morse_words)


# 5.Display Function (gets all the parameters and display everything by turning on and off the leds according to its timing and symbol)
def display_morse(morse_code, unit_time, color):
    for symbol in morse_code:
        print(symbol) #security measure to ensure everything works as is intended to.
        if symbol == '.':
            leds_on(color)
            time.sleep(unit_time)
            leds_off()
            time.sleep(unit_time)
        elif symbol == '-':
            leds_on(color)
            time.sleep(unit_time * 3)
            leds_off()
            time.sleep(unit_time)
        elif symbol == ' ':
            time.sleep(unit_time * 2)
        elif symbol == '/':
            time.sleep(unit_time * 6)


# Main Function: call all the functions and set the basics parameters
def main():
    cp.pixels.brightness = 0.2

    # Get all user inputs
    print("\n=== Morse Code Display ===")
    color = get_color()
    unit_time = get_unit_time()
    text = input("Enter message to convert: ").strip() #sort all the spaces

    # display the morse code obtained
    morse_code = text_to_morse(text)
    print(f"\nMorse Code: {morse_code}")
    print("Displaying...")

    display_morse(morse_code, unit_time, color)

    # Completion indicator (extra)
    leds_on((0, 255, 0))
    time.sleep(1)
    leds_off()
    print("Done!")


if __name__ == "__main__":
    main()
