# -*- coding: utf-8 -*-
from django.db import models


class Student(models.Model):
    """Student model"""

    class Meta:
        verbose_name = u'Студент'
        verbose_name_plural = u'Студенти'

    first_name = models.CharField(max_length=256, blank=False,
                                  verbose_name=u'Ім’я')
    last_name = models.CharField(max_length=256, blank=False,
                                 verbose_name=u'Прізвище')
    middle_name = models.CharField(max_length=256, blank=False,
                                   verbose_name=u'По-батькові', default='')
    birthday = models.DateField(blank=False, verbose_name=u'Дата народження',
                                null=True)
    photo = models.IntegerField(blank=True, verbose_name=u'Фото', null=True)
    ticket = models.CharField(max_length=256, blank=False,
                              verbose_name=u'Білет')
    notes = models.TextField(blank=True, verbose_name=u'Додаткові нотатки')

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Group(models.Model):
    """Group model"""

    class Meta:
        verbose_name = u'Група'
        verbose_name_plural = u'Групи'

    title = models.CharField(max_length=256, blank=False)
    leader = models.OneToOneField('Student', verbose_name=u'Староста',
                                  blank=True, null=True,
                                  on_delete=models.SET_NULL)
    notes = models.TextField(blank=True)

    def __unicode__(self):
        if self.leader:
            return u'%s (%s %s)' % (self.title, self.leader.first_name,
                                    self.leader.last_name)
        return u'%s' % (self.title,)
