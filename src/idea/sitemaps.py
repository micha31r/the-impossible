from django.contrib.sitemaps import Sitemap
from django.db.models import Count

from .models import Idea

class IdeaSitemap(Sitemap):    
	changefreq = "monthly"
	priority = 0.8

	def items(self):
		# Return the most viewed ideas
		return Idea.objects.annotate(p_count=Count('viewed_user')).order_by('-p_count')[:20]

	# Last edited
	def lastmod(self, obj):
		return obj.last_edit