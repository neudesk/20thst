import requests, os
from django.template.loader import get_template
from django.template import Context
from django.conf import settings

class MailGun(object):

    def __init__(self, subject=None, message=None, fr=None, recipients=[]):
        self.html = get_template("htmlmail.djhtml")
        self.txt = get_template("textmail.txt")
        self.message = message
        self.fr = fr
        self.recipients = recipients
        self.subject = subject
        self.dir = settings.PROJECT_DIR

    def get_context_data(self):
        data = Context({"message": self.message})
        return data

    def render(self):
        html = self.html.render(self.get_context_data())
        text = self.txt.render(self.get_context_data())
        return text, html

    def send(self):
        text, html = self.render()
        r = requests.post(settings.MAIL_API_ENDPOINT,
                          auth=("api", settings.MAIL_API_KEY),
                          data={"from": self.fr,
                                "to": [self.recipients],
                                "subject": self.subject,
                                "text": text,
                                "html": html})
        return r.status_code

    # def send(self):
    #     text, html = self.render()
    #     r = requests.post(
    #         settings.MAIL_API_ENDPOINT,
    #         auth=("api", settings.MAIL_API_KEY),
    #         files=MultiDict([("inline", "/var/www/churchofchrist/20thst/wsgi/static/logo.png")]),
    #         data={"from": "Excited User <%s>" % self.fr,
    #               "to": self.recipients,
    #               "subject": self.subject,
    #               "text": text,
    #               "html": html})
    #     return r.status_code

