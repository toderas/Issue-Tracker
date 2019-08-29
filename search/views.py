from django.shortcuts import render
from django.contrib.auth.models import User
from bugs.models import bug_item
from features.models import Feature
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def search_bugs(request):
    """ A views that returns a list of bugs based on search criteria """
    bugs = bug_item.objects.filter(name__icontains=request.GET['search']).order_by('-date_reported')
    count = bugs.count()
    page = request.GET.get('page', 1)

    paginator = Paginator(bugs, 5)
    try:
        bugs = paginator.page(page)
    except PageNotAnInteger:
        bugs = paginator.page(1)
    except EmptyPage:
        bugs = paginator.page(paginator.num_pages)
    return render(request, "filtered-bugs.html", {'bugs': bugs, 'query': request.GET['search'], 'count': count})


def search_author_bugs(request):
    """ A view that returns a certains's author posted bugs """
    bugs = bug_item.objects.filter(author_id=request.GET['bug-author']).order_by('-date_reported')
    count = bugs.count()
    user = User.objects.get(id=request.GET['bug-author']).username
    
    page = request.GET.get('page', 1)

    paginator = Paginator(bugs, 5)
    try:
        bugs = paginator.page(page)
    except PageNotAnInteger:
        bugs = paginator.page(1)
    except EmptyPage:
        bugs = paginator.page(paginator.num_pages)
    return render(request, "filtered-bugs.html", {'bugs': bugs, 'query': user, 'count': count})


def search_pending_review(request):
    """ A view that returns all bugs which are 'Pending review' """
    bugs = bug_item.objects.filter(status__icontains='Pending-review')
    count = bugs.count()
    query = 'Pending review'
    page = request.GET.get('page', 1)

    paginator = Paginator(bugs, 5)
    try:
        bugs = paginator.page(page)
    except PageNotAnInteger:
        bugs = paginator.page(1)
    except EmptyPage:
        bugs = paginator.page(paginator.num_pages)
    return render(request, "bugs.html", {'bugs': bugs, 'query': query, 'count': count})


def search_in_progress(request):
    """ A view that returns all bugs which are 'In progress' """
    bugs = bug_item.objects.filter(status__icontains='In-progress')
    count = bugs.count()
    query = 'In Progress'
    page = request.GET.get('page', 1)

    paginator = Paginator(bugs, 5)
    try:
        bugs = paginator.page(page)
    except PageNotAnInteger:
        bugs = paginator.page(1)
    except EmptyPage:
        bugs = paginator.page(paginator.num_pages)
    return render(request, "bugs.html", {'bugs': bugs, 'query': query, 'count': count})
    

def search_resolved(request):
    """ A view that returns all bugs which are 'Resolved' """
    bugs = bug_item.objects.filter(status__icontains='Resolved')
    count = bugs.count()
    query = 'Resolved'
    page = request.GET.get('page', 1)

    paginator = Paginator(bugs, 5)
    try:
        bugs = paginator.page(page)
    except PageNotAnInteger:
        bugs = paginator.page(1)
    except EmptyPage:
        bugs = paginator.page(paginator.num_pages)
    return render(request, "bugs.html", {'bugs': bugs, 'query': query, 'count': count})


def search_features(request):
    """ A views that returns a list of Features based on search criteria """
    features = Feature.objects.filter(name__icontains=request.GET['search'])
    count = features.count()
    print(features)
    page = request.GET.get('page', 1)

    paginator = Paginator(features, 5)
    try:
        features = paginator.page(page)
    except PageNotAnInteger:
        features = paginator.page(1)
    except EmptyPage:
        features = paginator.page(paginator.num_pages)
    return render(request, "features.html", {'features': features, 'query': request.GET['search'], 'count': count})