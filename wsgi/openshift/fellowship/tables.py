from django_tables2 import tables, Column
from openshift.tables import AdminBaseTable
from slider.tables import BaseActionColumn
from event.models import Event

class RowActions(Column, BaseActionColumn):
    def render(self, value):
        self.new_path = "#"
        self.update_path = "#test"
        self.delete_path = "#test"

        return self.action_group()

class AdminFellowshipTable(tables.Table):

    id = RowActions(verbose_name="actions")

    class Meta:
        model = Event
        exclude = ("post_type",
                   "youtube_video_id",
                   "parent_post",
                   "start_date",
                   "end_date",
                   "start_time",
                   "end_time",
                   "place")

        attrs = {"class": "table table-bordered table-hover table-striped display",
                 "id": "eventTable"}