from .models import CoreFeed


# This creates private system feed
def create_corefeed(option,**kwargs):
	# A list of all system core feed messages:
	CORE_FEED = {
		# Auth
		"WELCOME":{
			"name":"Welcome to The Impossible",
			"description":f"""
				<a href="{kwargs["absolute_url"]}">@{kwargs["username"]}</a> Thanks for joining us. Create, share and explore fresh ideas. 
				As a social media platform, we want our service to be as transparent 
				as possible, therefore, here is the information we store about you:
				<ul>
					<li>Full Name</li>
					<li>Email</li>
					<li>Website</li>
					<li>Profilee Image</li>
					<li>Location</li>
					<li>Followers and Following</li>
				</ul>
				Lastly, if you wish to terminate your account, 
				please email \"hello@theimpossible.world\". (All data will be deleted)

			"""
		}
	}
	obj = CoreFeed.objects.create(
		name = CORE_FEED[option]["name"],
		description = CORE_FEED[option]["description"]
	)
	obj.save()
	return obj


