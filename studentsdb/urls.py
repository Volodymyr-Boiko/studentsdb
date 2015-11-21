from django.conf.urls import patterns, include, url
from django.contrib import admin
from students.views import students_list


urlpatterns = patterns('',
    url(r'^$', students_list, name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
