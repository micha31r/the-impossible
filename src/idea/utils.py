def at_filter(data):
	usernames = []
	for word in data.split(" "):
		if "@" in word:
			usernames.append(word.split("@")[-1])
	return usernames