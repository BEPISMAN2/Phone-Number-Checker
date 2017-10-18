from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import sys

POSSIBLENUM1 = "ew find your own phone number you weeb"

def main():
	client = Client()

	out = open("valid-numbers.txt", "w")

	validNumbers = 0
	invalidNumbers = 0
	
	for pNumber in [POSSIBLENUM1]:
		for i in range(1000):
			ext = str(i).zfill(3)
			num = pNumber.format(ext)

			try:
				numResponse = client.lookups.phone_numbers(num).fetch()
				print("Valid Number Found: {}\n".format(numResponse.national_format))
				out.write("Valid Number Found: {}\n".format(numResponse.national_format))
				validNumbers += 1
			except TwilioRestException as e:
				if e.code == 20404:
					print("{} is not a valid phone number.".format(num))
					invalidNumbers += 1
					continue
				else:
					raise e
				
	print("\n\n\nValid Numbers Found: {}\nInvalid Numbers Found: {}".format(str(validNumbers), str(invalidNumbers)))
	out.close()

if __name__ == "__main__":
	main()
