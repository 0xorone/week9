from django.shortcuts import render
from website.forms.timesheetForm import TimesheetForm
from website.models.timesheet import Timesheet
from datetime import date, datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def getTimesheetById(request, id):
    timesheet = Timesheet.objects.get(id=id)
    form = TimesheetForm(initial=timesheet.__dict__)
    return render(request, "website/timesheet.html", {"form": form})

@csrf_exempt
@login_required(login_url='/login')
def timesheet(request):
    if request.method == "POST":
        return postTimesheet(request)

    now = datetime.now()
    form = TimesheetForm(initial=
        {
            'userId':request.user.id, 
            'approved': False, 
            'date': date.today(),
            'timeFrom': (now + timedelta(hours=-1)).strftime("%H:%M"),
            'timeTo': now.strftime("%H:%M"),
            'totalMinutes': 0
        })
    return render(request, "website/timesheet.html", {"form": form})

@login_required(login_url='/login')
def postTimesheet(request):
    form = TimesheetForm(request.POST)
    if form.is_valid():
        if allowApprove(request):
            form.save()
        else:
            timesheet = form.save(commit=False)
            timesheet.approved = False
            timesheet.save()

    return render(request, "website/timesheet.html", {"form": form})

def allowApprove(request):
    permissions = request.COOKIES.get('permissions')
    allowed = True

    try:
        if permissions.contains('allowApprove'):
            allowed = True
        else:
            allowed = False
    except:
        print('Ignore this error')
        
    return allowed
