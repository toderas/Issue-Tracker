from django.shortcuts import render
from bugs.models import bug_item
from django.core.paginator import Paginator

# Create your views here.

def search_bugs(request):
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
