from django.views.generic import TemplateView, DetailView
from .models import Word

class HomeView(TemplateView):
    template_name = 'words/home.html'

    def get_context_data(self):
        all_words = Word.objects.all().order_by('word')
        words = {}
        for word in all_words:
            words.setdefault(word.alignment, []).append(word)

        return {
            'words': words,
            #'random': Word.objects.order_by('?')[0],
        }

class WordView(DetailView):
    model = Word

    def get_context_data(self, object):
        return {
            'object': object,
            'words': Word.objects.all(),
        }
