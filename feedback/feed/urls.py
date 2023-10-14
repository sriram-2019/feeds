from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from feed import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("",views.index,name=""),
    path("second/",views.second_page,name="second"),
    path("seconds/",views.second_pages,name="seconds"),
    path("seconds/seconds",views.second_pages,name="seconds"),
    path("seconds/log",views.logout,name="seconds"),
    path("survey/",views.surveypage,name="survey"),
    path("seconds/survey2",views.surveypages,name="survey2"),
    path("getdata/",views.getdata,name="getdata"),
    path("getdata/",views.getdata,name="getdata"),
    path("seconds/bar/",views.bars,name="bar"),
    path("seconds/bar/bar",views.bars,name="bar"),
    path("seconds/bar/survey2",views.surveypages,name="bar"),
    path("seconds/bar/seconds",views.second_pages,name="bar"),
    path("seconds/bar/goto",views.disp,name="seconds/goto"),
    path("display_data/display_data/goto",views.disp,name="seconds/goto"),
    path("display_data/goto",views.disp,name="seconds/goto"),
    path("display_data1/goto",views.disp,name="seconds/goto"),
    path("display_overall2/goto",views.disp,name="seconds/goto"),
    path("display_overall3/goto",views.disp,name="seconds/goto"),
    path("display_overall4/goto",views.disp,name="seconds/goto"),
    path("display_overall/goto",views.disp,name="seconds/goto"),
    path("administrator/",views.disp,name="second/admin"),
    path("display_data/",views.display,name="display_data"),
    path("display_data1/",views.display1,name="display_data"),
    path("display_overall/",views.bars,name="display_overall"),
    path("display_overall2/",views.display2,name="display_overall"),
    path("display_overall3/",views.display3,name="display_overall"),
    path("display_overall4/",views.display4,name="display_overall"),
    path("exc",views.excel,name="exc")

]