from django_tables2 import tables, Column
from event.models import Event
from django.utils.safestring import mark_safe
from django.utils.html import escape, strip_tags
from django.http import HttpRequest
from django.contrib.sites.models import get_current_site
from django.core.urlresolvers import reverse_lazy

class SafeTextColumn(Column):

    def __init__(self, *args, **kwargs):
        super(SafeTextColumn, self).__init__()
        self.words = int(kwargs.get('words', None))

    def truncate_words(self, string, n):
        return ' '.join(string.split()[:n])

    def render(self, value):
        return "%s ..." % self.truncate_words(strip_tags(value), self.words)

class BannerColumn(Column):
    def render(self, value):
        return mark_safe("<img src='%s' style='width: 130px' />" % strip_tags(value))

class BoolColumn(Column):
    def render(self, value):
        hex = None
        if value:
            hex = "09ff04"
        else:
            hex = "CCCCCC"
        return mark_safe('<a style="color: #%s;"><i class="fa fa-check-circle"></i></a>' % hex)

class RowActionsColumn(Column):
    request = HttpRequest
    def render(self, value):
        return mark_safe('<div class="fb-share-button" data-href="%s%s" data-type="button_count"></div>' % (get_current_site(self.request),
                                                                                                            reverse_lazy('event_by_id', args=(value,)  )))

class AdminBaseTable(tables.Table):

    title = Column(verbose_name="Event Title")
    details = SafeTextColumn(verbose_name="Content", words=1)
    cover = BannerColumn(verbose_name="Feature Image", accessor="cover_thumbnail.url")
    is_pub = BoolColumn(verbose_name="Published")
    id = RowActionsColumn(verbose_name="actions")

    class Meta:
        model = Event
        exclude = ("post_type",
                   "youtube_video_id",
                   "parent_post")
        attrs = {"class": "table table-bordered table-hover table-striped display",
                 "id": "eventTable"}

class AdminEventTable(AdminBaseTable, tables.Table):
    class Meta:
        model = Event
        exclude = ("post_type",
                   "youtube_video_id",
                   "parent_post",
                   "id")
        attrs = {"class": "table table-bordered table-hover table-striped display",
                 "id": "eventTable"}