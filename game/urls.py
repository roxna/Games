from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'game.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'snake.views.home', name='home'),
    url(r'^profile/$', 'snake.views.profile', name='profile'),
    url(r'^snake/$', 'snake.views.snake', name='snake'),
    url(r'^memory_game/$', 'snake.views.memory_game', name='memory_game'),

    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
)
