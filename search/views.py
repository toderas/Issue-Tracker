from django.shortcuts import render
from bugs.models import bug_item
from django.core.paginator import Paginator

# Create your views here.

def search_bugs(request):
    """ A views that returns a list of bugs based on search criteria """
    bugs = bug_item.objects.filter(name__icontains=request.GET['search'])
    page = request.GET.get('page', 1)

    paginator = Paginator(bugs, 5)
    try:
        bugs = paginator.page(page)
    except PageNotAnInteger:
        bugs = paginator.page(1)
    except EmptyPage:
        bugs = paginator.page(paginator.num_pages)
    return render(request, "bugs.html", {'bugs': bugs})

def search_user_bugs(request):
    """ A view that returns the user's posted bugs """
    bugs = bug_item.objects.filter(author__icontains=request.user.username)
    page = request.GET.get('page', 1)

    paginator = Paginator(bugs, 5)
    try:
        bugs = paginator.page(page)
    except PageNotAnInteger:
        bugs = paginator.page(1)
    except EmptyPage:
        bugs = paginator.page(paginator.num_pages)
    return render(request, "bugs.html", {'bugs': bugs})
    
    
def search_author_bugs(request):
    """ A view that returns a certains's author posted bugs """
    bugs = bug_item.objects.filter(author__icontains=request.GET['bug-author'])
    page = request.GET.get('page', 1)

    paginator = Paginator(bugs, 5)
    try:
        bugs = paginator.page(page)
    except PageNotAnInteger:
        bugs = paginator.page(1)
    except EmptyPage:
        bugs = paginator.page(paginator.num_pages)
    return render(request, "bugs-by-user.html", {'bugs': bugs})


def search_pending_review(request):
    """ A view that returns all bugs which are 'Pending review' """
    bugs = bug_item.objects.filter(status__icontains='Pending-review')
    page = request.GET.get('page', 1)

    paginator = Paginator(bugs, 5)
    try:
        bugs = paginator.page(page)
    except PageNotAnInteger:
        bugs = paginator.page(1)
    except EmptyPage:
        bugs = paginator.page(paginator.num_pages)
    return render(request, "bugs-by-status.html", {'bugs': bugs})


def search_in_progress(request):
    """ A view that returns all bugs which are 'In progress' """
    bugs = bug_item.objects.filter(status__icontains='In-progress')
    page = request.GET.get('page', 1)

    paginator = Paginator(bugs, 5)
    try:
        bugs = paginator.page(page)
    except PageNotAnInteger:
        bugs = paginator.page(1)
    except EmptyPage:
        bugs = paginator.page(paginator.num_pages)
    return render(request, "bugs-by-status.html", {'bugs': bugs})
    

def search_resolved(request):
    """ A view that returns all bugs which are 'Resolved' """
    bugs = bug_item.objects.filter(status__icontains='Resolved')
    page = request.GET.get('page', 1)

    paginator = Paginator(bugs, 5)
    try:
        bugs = paginator.page(page)
    except PageNotAnInteger:
        bugs = paginator.page(1)
    except EmptyPage:
        bugs = paginator.page(paginator.num_pages)
    return render(request, "bugs-by-status.html", {'bugs': bugs})
    