from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import bug_item
from .forms import AddBugForm

# Create your views here.
def get_bugs(request):
    bugs = bug_item.objects.all()
    return render(request, "bugs.html", {"bugs": bugs})
    
@login_required()
def add_new_bug(request):
    """
    Renders AddBugForm saves its contents and returns to main page (user dependant yet to be implemented)
    """
    if request.method == 'POST':
        item_form = AddBugForm(request.POST)
        if item_form.is_valid():
            bug = item_form.save(commit=True)
            bug.save()
            return redirect(get_bugs)
            
    else:
        item_form = AddBugForm()
    return render(request, 'new-bug.html', {"item_form": item_form})


def get_current_bug(request, id):
    bug = get_object_or_404(bug_item, id=id)
    print(bug)
    return render(request, 'bug-details.html', {'bug': bug})


