import random

# Creates a simple string that can be used to verify ajax requests

characters = "aAlLsSkKdDjJfFhHgGqQpPwWoOeEiIrRuUtTyYzZmMxXnNcCbBvV1029384756"
characters_2 = "mnbvcxzlkj3hgfds1aqwerty2uio8pASDFG4HJK5LMNB7VCX9ZQWER6TY0UPOI"
# Make sure its a large prime number
special_numbers = [3267000013,5915587277,1500450271] # Make sure its a large prime number

def encode(text):
	length = len(text)
	numbers = []
	alphabet_sum = 0
	encoded_string = ""
	for i in range(length):
		for j in range(len(characters)):
			if text[i] == characters[j]:
				numbers.append(i*j)
				alphabet_sum += j
	random.seed(alphabet_sum)
	extra_number = random.randint(random.randint(0,10),random.randint(10,20))
	for i in range(extra_number):
		random.seed(length+i^i)
		numbers.append(random.randint(0,alphabet_sum))
	random.seed((alphabet_sum*random.randint(0,length)-length)*random.randint(0,alphabet_sum)^3)
	for i in range(len(numbers)):
		numbers[i] *= length^3
		numbers[i] -= length^2 - length
		for n in special_numbers:
			numbers[i] *= n + alphabet_sum + length + random.randint(0,length+alphabet_sum)
		indice = numbers[i] % len(characters_2)
		encoded_string += characters_2[indice]
	return encoded_string

