from django.conf.urls import patterns, include, url
from django.conf import settings
from words.views import HomeView, WordView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
)

# Admin stuff, if necessary.
if 'django.contrib.admin' in settings.INSTALLED_APPS:
    from django.contrib import admin
    admin.autodiscover()

    urlpatterns += patterns('',
        url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
        url(r'^admin/', include(admin.site.urls)),
    )

urlpatterns += patterns('',
    url(r'^(?P<slug>[^/]+)/$', WordView.as_view(), name='words_word'),
)

# Auth stuff, if necessary
if 'django_cas' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        (r'^accounts/login/$', 'django_cas.views.login'),
        (r'^accounts/logout/$', 'django_cas.views.logout'),
    )

# Media in DEBUG mode
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
