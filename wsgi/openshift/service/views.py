from event.views import *

class ServiceIndex(EventIndex):
    template_name = "serviceindex.djhtml"
    title = "Worship Service"
    postType = PostType.objects.filter(type="event")
    
    def get_post(self):
        if self.postType:
            try:
                return self.model.objects.filter(is_pub=True,
                                                 post_type=self.postType[0])
            except:
                return None
        else:
            return None
