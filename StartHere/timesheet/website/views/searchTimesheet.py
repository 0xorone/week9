from django.shortcuts import render
from website.models.timesheet import Timesheet
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def search(request):
    searchText = request.GET.get('searchText')
    if not searchText is None:
        sqlString = "SELECT id, notes FROM website_timesheet WHERE notes LIKE '%" + searchText + "%'"
        searchTimesheets = Timesheet.objects.raw(sqlString)
        return render(request, 'website/searchTimesheet.html', {'searchResults': searchTimesheets})

    return render(request, 'website/searchTimesheet.html')
