from event.models import *
from openshift.views import AdminBaseView
from .tables import AdminFellowshipTable

class AdminFellowship(AdminBaseView):
    template_name = "adminfellowship.djhtml"
    postType = "fellowship"
    title = "Fellowship"
    pagedesc = "You can create fellowship group page in this section."
    model = Event
    page_name = "fellowship"
    table_class = AdminFellowshipTable