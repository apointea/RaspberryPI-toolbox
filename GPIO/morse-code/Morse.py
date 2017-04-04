from gpiozero import LED
from time import sleep

class Morse:

	def __init__ (self, pin):
		self.alpha = {
			'a': [1, 2], 'b': [2, 1, 1, 1], 'c': [2, 1, 2, 1], 'd': [2, 1, 1],
			'e': [1], 'f': [1, 1, 2, 1], 'g': [2, 2, 1], 'h': [1, 1, 1, 1],
			'i': [1, 1], 'j': [1, 2, 2, 2], 'k': [2, 1, 2], 'l': [1, 2, 1, 1],
			'm': [2, 2], 'n': [2, 1], 'o': [2, 2, 2], 'p': [1, 2, 2, 1],
			'q': [2, 2, 1, 2], 'r': [1, 2, 1], 's': [1, 1, 1], 't': [2],
			'u': [1, 1, 2], 'v': [1, 1, 1, 2], 'w': [1, 2, 2], 'x': [2, 1, 1, 2],
			'y': [2, 1, 2, 2], 'z': [2, 2, 1, 1], '1': [1, 2, 2, 2, 2],
			'2': [1, 1, 2, 2, 2], '3': [1, 1, 1, 2, 2], '4': [1, 1, 1, 1, 2],
			'5': [1, 1, 1, 1, 1], '6': [2, 1, 1, 1, 1], '7': [2, 2, 1, 1, 1],
			'8': [2, 2, 2, 1, 1], '9': [2, 2, 2, 2, 1], '0': [2, 2, 2, 2, 2]
		}
		self.pin = LED(pin)
		self.timeUnit = 0.5

	def setPin(self, pin):
		self.pin = LED(pin)

	def setTimeUnit(self, time = 0.5):
		self.timeUnit = time

	def write_letter(self, letter):
		letter = letter.lower()
		frames = self.alpha[letter]
		for t in frames:
			self.pin.on()
			sleep(t * self.timeUnit)
			self.pin.off()
			sleep(t * self.timeUnit / 2)

	def write_string(self, string):
		for letter in string:
			if letter.isalnum():
				self.write_letter(letter)
				sleep(self.timeUnit)
			else:
				sleep(4 * self.timeUnit)
