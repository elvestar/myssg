# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

app_name = 'tms'
urlpatterns = [
    url(r'^clock_items/$', views.ClockItemList.as_view()),
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.calendar, name='about'),

    url(r'^project/$', views.project, name='project'),
    url(r'^project/analyzer/$', views.time_analyzer, name='time_analyzer'),
    url(r'^project/all/$', views.all_projects, name='all_projects'),

    url(r'^calendar/$', views.calendar, name='calendar'),
    url(r'^report/$', views.report, name='report'),
    url(r'^report/week/$', views.week_report, name='week_report'),
    url(r'^report/day/$', views.day_report, name='day_report'),
    url(r'^report/year/$', views.year_report, name='year_report'),
    url(r'^report/custom/$', views.custom_report, name='custom_report'),

    url(r'^api/v1/week_stats/$', views.week_stats, name='week_stats'),
    url(r'^api/v1/year_stats_step_by_month_and_week/$', views.year_stats_step_by_month_and_week,
        name='year_stats_step_by_month_and_week'),
]
