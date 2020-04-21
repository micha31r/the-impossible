# Creates a simple string that can be used to verify ajax requests

characters = "aAlLsSkKdDjJfFhHgGqQpPwWoOeEiIrRuUtTyYzZmMxXnNcCbBvV1029384756"
special_number = 24958931 # Make sure its a large prime number

def encode(text):
	length = len(text)
	numbers = []
	encoded_string = ""
	for i in range(length):
		for j in range(len(characters)):
			if text[i] == characters[j]:
				numbers.append(i*j)
	for i in range(len(numbers)):
		numbers[i] *= length
		numbers[i] -= length^2 - length
		numbers[i] *= special_number
		indice = numbers[i] % len(characters)
		encoded_string += characters[indice]
	return encoded_string
