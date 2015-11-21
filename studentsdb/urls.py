from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from students.views import students_list
from students.views import students_add
from students.views import students_edit
from students.views import students_delete
from students.views import groups_list
from students.views import groups_add
from students.views import groups_edit
from students.views import groups_delete


urlpatterns = patterns('',
    url(r'^$', students_list, name='home'),
    url(r'^students/add/$', students_add, name='students_add'),
    url(r'^students/(?P<sid>\d+)/edit/$', students_edit, name='students_edit'),
    url(r'^students/(?P<sid>\d+)/delete/$', students_delete,
        name='students_delete'),

    url(r'^groups/$', groups_list, name='groups'),
    url(r'^groups/add/$', groups_add, name='groups_add'),
    url(r'^groups/(?P<gid>\d+)/edit/$', groups_edit, name='groups_edit'),
    url(r'^groups/(?P<gid>\d+)/delete/$', groups_delete, name='groups_delete'),
    url(r'^admin/', include(admin.site.urls)),
)
