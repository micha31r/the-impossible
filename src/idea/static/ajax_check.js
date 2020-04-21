// Creates a simple string that can be used to verify ajax requests

const characters = "aAlLsSkKdDjJfFhHgGqQpPwWoOeEiIrRuUtTyYzZmMxXnNcCbBvV1029384756";
const special_number = 24958931; // Make sure its a large prime number

function encode(text) {
	const length = text.length;
	var numbers = [];
	var encoded_string = "";
	for (var i=0; i<length; i++) {
		for (var j=0; j<characters.length; j++) {
			if (text[i] == characters[j]) {
				numbers.push(i*j);
			}
		}
	}
	for (var i=0; i<numbers.length; i++) {
		numbers[i] *= length;
		numbers[i] -= length^2 - length;
		numbers[i] *= special_number;
		var indice = numbers[i] % characters.length;
		encoded_string += characters[indice];
	}
	return encoded_string;
}
