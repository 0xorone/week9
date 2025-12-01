from django.contrib import admin
from django.urls import path
from website.views import logmein, logmeout, search, home
from website.views.user import myUser, createUser
from website.views.timesheet import timesheet, getTimesheetById

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', logmein, name="login"),
    path('home', home, name="home"),
    path('logout', logmeout, name="logout"),
    path('myUser', myUser, name="myUser"),
    path('createUser', createUser, name="createUser"),
    path('timesheets', timesheet, name="timesheets"),
    path('timesheets/<int:id>', getTimesheetById, name="getTimesheetById"),
    path('timesheets/search', search, name="searchResults"),
]
