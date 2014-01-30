from django.utils.html import mark_safe, strip_tags
from django_tables2 import tables, Column
from django.core.urlresolvers import reverse_lazy
from .models import *

class ThumbnailColumn(Column):
    def render(self, value):
        html = """
        <img src='%s' style='width: 100px; height: auto' />
        """ % value
        return mark_safe(html)

class BaseActionColumn(object):

    def __init__(self):
        self.new_path = "#"
        self.delete_path = "#"
        self.update_path = "#"

    def action_group(self):
        html = """
        <div class='btn-group'>
            <button type='button' class='btn btn-xs btn-info dropdown-toggle btn-animate-demo' data-toggle='dropdown'>
                Options <span class='caret'></span>
            </button>
            <ul class='dropdown-menu' role='menu'>
                %s
            </ul>
        </div>
        """ % self.action_menu()
        return mark_safe(html)

    def action_menu(self):
        menu = ""
        if self.new_path is not "#":
            menu += "<li>%s</li>" % self.new_btn()
        if self.delete_path is not "#":
            menu += "<li>%s</li>" % self.delete_btn()
        if self.update_path is not "#":
            menu += "<li>%s</li>" % self.update_btn()
        return menu

    def new_btn(self):
        html = """
        <a href='%s'><i class="fa fa-gear"></i> Add Item</a>
        """ % self.new_path
        return html

    def delete_btn(self):
        html = """
        <a href='%s'><i class="fa fa-trash-o"></i> Delete</a>
        """ % self.delete_path
        return html

    def update_btn(self):
        html = """
        <a href='%s'><i class='fa fa-pencil'></i> Update</a>
        """ % self.update_path
        return html

class SlideActionColumn(Column, BaseActionColumn):
    def render(self, value):
        self.new_path = reverse_lazy("dashboard_slides_new_item", args=(value,))
        self.update_path = reverse_lazy("dashboard_slide_update", args=(value,))
        self.delete_path = reverse_lazy("dashboard_slides_delete", args=(value,))
        return self.action_group()

class SlidesTable(tables.Table):
    id = SlideActionColumn(verbose_name="actions")
    background = ThumbnailColumn(accessor="background.url")
    class Meta:
        model = Slide
        attrs = {"class": "table table-bordered table-hover table-striped display",
                 "id": "eventTable"}




class SlideItemActionColumn(Column, BaseActionColumn):
    def render(self, value):
        self.new_path = "#"
        self.update_path = reverse_lazy("dashboard_slides_update_item", kwargs={"pk": value})
        self.delete_path = reverse_lazy("dashboard_slides_delete_item", args=(value,))

        return self.action_group()

class SlidesItemsTables(tables.Table):

    id = SlideItemActionColumn(verbose_name="Actions")

    class Meta:
        model = SlideItem
        attrs = {"class": "table table-bordered table-hover table-striped display",
                 "id": "eventTable"}
