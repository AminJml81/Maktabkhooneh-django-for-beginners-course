from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Post


class LatestBlogsFeed(Feed):
    title = "BLog Newest Posts"
    link = "/rss/feed"
    description = "Best Blog Ever" 
    
    def items(self):
        return Post.objects.filter(status=True)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:100]
