# RaspberryPI-GPIO-Morse-code

A simple class for translating a string into morse code through the pins.
It's write to be used with LED.

## INSTALL

The class require gpiozero (https://pypi.python.org/pypi/gpiozero) :

`sudo apt-get install python-gpiozero`

## EXAMPLE

- Instantiate with a pin number (https://www.raspberrypi.org/documentation/usage/gpio-plus-and-raspi2/)

`m = Morse(17)`

- Then just call the write method

`m.write_string("Hello World")`

## METHODS

- `setPin(pin)` - int pin - Change the pin to activate
- `setTimeUnit(time)` - float time - Change the timer unit to go faster or lower
- `write_letter(character)` - char character - For write only one char (used by write_string)
- `write_string(string)` - string() string - For write an entire string
