# WARNING !! DONT RUN THIS ON A LIVE SERVER !!
# On my Macbook it takes 34 seconds to create 5000 idea objects

from idea.models import Idea
from usermgmt.models import Profile

def create_ideas(number):
	for i in range(number):
		obj = Idea.objects.create(
			name="Auto",
			short_description="example and example and ...",
			full_description=f"Scale test {number}",
			author=profile,
			publish_status=3
		)
		obj.save()
		if i % 5000 == 0:
			print(f"Loop: {i}")

profile = Profile.objects.get(id=1)
create_ideas(1)