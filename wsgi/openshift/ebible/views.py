from event.views import EventIndex
from django.conf import settings
from django.utils import simplejson
from django.http import HttpResponse
import requests

class BibleApi(object):
    
    def __init__(self):
        self.key = settings.BIBLE_API_KEY
        self.endpoint = settings.BIBLE_API_ENDPOINT
        self.version = settings.BIBLE_API_VERSION
        self.book = None
        self.chapter = None
        self.verse = None
        self.url = None
    
    def get_response(self, url):
        s = requests.Session()
        s.auth=(self.key,'X')
        headers = {'content-type': 'application/json'}
        try:
            r = s.get(url, headers=headers)
            data = r.json()
        except Exception as e:
            data = {"error":e}
        return data
        
    #GET /versions/#{version_id}/books.js?include_chapters=false
    def get_all_books(self):
        self.url = "%s/versions/%s/books.js?include_chapters=true" % (self.endpoint,
                                                                      self.version)
        return self.get_response(self.url)
    
    #GET https://bibles.org/v2/versions/eng-KJVA/books.js?testament=NT
    def get_all_books_by_testament(self, testament):
        self.url = "%s/versions/%s/books.js?testament=%s" % (self.endpoint,
                                                             self.version,
                                                             testament)
        return self.get_response(self.url)
    
    #GET /books/#{version_id}:#{book_name}.js
    #GET https://bibles.org/v2/books/eng-GNTD:Rev.js
    def get_book(self, book_name):
        self.url = "%s/books/%s.js" % (self.endpoint,
                                       book_name)
        return self.get_response(self.url)
    
    #GET /books/#{version_id}:#{book_id}/chapters.js
    #GET https://bibles.org/v2/books/eng-GNTD:2Tim/chapters.js
    def get_book_chapters(self, book_id):
        self.url = "%s/books/%s/chapters.js" % (self.endpoint,
                                                   book_id)
        return self.get_response(self.url)
    
    
    #GET /chapters/#{version_id}:#{book_id}.#{chapter_number}.js?include_marginalia=true
    #GET https://bibles.org/v2/chapters/eng-KJVA:Acts.8.js
    def get_book_chapter_by_chapter_number(self, chapter_id):
        self.url = "%s/chapters/%s.js" % (self.endpoint,
                                          chapter_id)
        return self.get_response(self.url)
    
    #GET /chapters/#{version_id}:#{book_id#     url(r'^$', Book.as_view(), name='ebible_book'),}.#{chapter_number}/verses.js?start=1&end=14
    #GET https://bibles.org/v2/chapters/eng-KJVA:1Cor.2/verses.js?start=5&end=6
    def get_verse_by_range(self,book_name, chapter_number, verse_start, verse_end):
        self.url = "%s/chapters/%s:%s.%s/verses.js?start=%s&end=%s" % (self.endpoint,
                                                                       self.version,
                                                                       book_name,
                                                                       chapter_number,
                                                                       verse_start,
                                                                       verse_end)
        return self.get_response(self.url)

def apiviewer(request):
    api = BibleApi()
    data = simplejson.dumps(api.get_book_chapter_by_chapter_number("eng-KJVA:Gen.1"))
    return HttpResponse(data, mimetype='application/json')

class Books(EventIndex):
    template_name = "books.djhtml"
    title = "Holy Bible - King James Version"
    api = BibleApi()
    chapter_id = "eng-KJVA:Gen.1"
    
    def get_content(self):
        try:
            self.chapter_id = self.args[0]
            data = self.api.get_book_chapter_by_chapter_number(self.chapter_id)
        except:
            data = self.api.get_book_chapter_by_chapter_number(self.chapter_id)
        return data
        
    def get_context_data(self, *args, **kwargs):
        context = super(Books, self).get_context_data(*args, **kwargs)
        context['books'] = self.api.get_all_books()
        context['chapter'] = self.get_content()
        return context
    
    
    
