from event.views import EventIndex, SingleEvent
from event.models import PostType

class NewsIndex(EventIndex):
    
    template_name = "newsindex.djhtml"
    postType = PostType.objects.filter(type="news")
    title = "News and Updates"
    
    def get_post(self):
        if self.postType:
            return self.model.objects.filter(is_pub=True,
                                                 post_type=self.postType[0]).order_by('-id')
        else:
            return None
    
class SingleNews(SingleEvent):
    template_name = "newssingle.djhtml"