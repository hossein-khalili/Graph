from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Graph.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('home.urls')),
	url(r'^login/', include('login.urls')),
	url(r'^home/', include('home.urls')),
	url(r'^create/', include('create.urls')),
	url(r'^vertex/', include('vertex.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
