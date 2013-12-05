from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _


ALIGNMENTS = (
    (u'lawful', u'Lawful'),
    (u'neutral', u'Neutral'),
    (u'chaotic', u'Chaotic'),
)


class Word(models.Model):
    word = models.CharField(_('word'), max_length=255, db_index=True)
    slug = models.SlugField(_('slug'), unique=True)
    alignment = models.CharField(_('alignment'), max_length=64, choices=ALIGNMENTS)
    examples = models.TextField(_('examples'))
    usage = models.TextField(_('usage'))
    recommendations = models.TextField(_('recommendations'))

    class Meta:
        verbose_name = _('word')
        verbose_name_plural = _('words')
        ordering = ('word',)

    def __unicode__(self):
        return self.word

    def get_absolute_url(self):
        return reverse('words_word', args=[self.slug])
